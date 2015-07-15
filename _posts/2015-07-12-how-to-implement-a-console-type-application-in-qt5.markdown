---
layout: post2
title:  "How to Implement a Console-Type Application in Qt5"
date:   2015-07-12 10:34:04
tags: qt qt5 console windows
---

Qt5 is not only a great C++ library for writing GUI applications, but also a great library for writing console-type applications. It has the most extensive and consistent API for data structure, string, file system, networking, database, configuration, and many others, which are the core of every console-type applications. Today I'm going to talk about how to implement console-type applications in Qt5.

Instead of using QMake (the build system included in Qt5), I will use CMake as the build system for the examples. CMake is officially supported by Qt, so it means that you can get all the benefits from using CMake without having to implement many CMake scripts yourself.

There are two types of console-type applications in Qt5:
* A console-type application without the event loop
* A console-type application with the event loop

### A Console-Type Application without the Event Loop

The minimalist Qt5 console application looks like the following `main.cpp` sample code. All you have to do is including the header files of the Qt5 classes that you need.

```cpp
#include <QDebug>

int main(int argc, char *argv[])  
{
   qDebug() << "Hello World" << endl;
   return 0;
}
```

To build this application using CMake, you can use the following CMake script as the starting point:

```cmake
cmake_minimum_required(VERSION 2.8.11)
project(qt5-console-example)

# Find the Qt library
set(CMAKE_PREFIX_PATH "C:/Lib/Qt/5.4.2-win32-msvc2012-static/qtbase/lib/cmake")
# Find includes in corresponding build directories
set(CMAKE_INCLUDE_CURRENT_DIR ON)
# Instruct CMake to run moc automatically when needed.
set(CMAKE_AUTOMOC ON)

# Find the QtWidgets library
find_package(Qt5Core)

set(TARGET_BASE_NAME "${PROJECT_NAME}")
set(EXE_NAME "${TARGET_BASE_NAME}")
set(EXECUTABLE_OUTPUT_PATH "${PROJECT_BINARY_DIR}/bin")

# We statically link to reduce dependancies
if(MSVC)
    foreach(flag_var
        CMAKE_C_FLAGS
        CMAKE_C_FLAGS_DEBUG
        CMAKE_C_FLAGS_RELEASE
        CMAKE_C_FLAGS_MINSIZEREL
        CMAKE_C_FLAGS_RELWITHDEBINFO
        CMAKE_CXX_FLAGS
        CMAKE_CXX_FLAGS_DEBUG
        CMAKE_CXX_FLAGS_RELEASE
        CMAKE_CXX_FLAGS_MINSIZEREL
        CMAKE_CXX_FLAGS_RELWITHDEBINFO)
        if(${flag_var} MATCHES "/MD")
            string(REGEX REPLACE "/MD" "/MT" ${flag_var} "${${flag_var}}")
        endif(${flag_var} MATCHES "/MD")
        if(${flag_var} MATCHES "/MDd")
            string(REGEX REPLACE "/MDd" "/MTd" ${flag_var} "${${flag_var}}")
        endif(${flag_var} MATCHES "/MDd")
    endforeach(flag_var)
endif()

# List the source files for the project
set(SRC_FILES
    "main.cpp"
)

# Tell CMake to create the helloworld executable
add_executable(${EXE_NAME} ${SRC_FILES})

# Specify the libraries for the executable
target_link_libraries(${EXE_NAME}
    general ws2_32.lib
)

# Use the Core module from Qt 5.
target_link_libraries(${EXE_NAME} ${Qt5Core_LIBRARIES})
```

You can call the cmake command to generate the Visual Studio solution file and then compile the application in Visual Studio. However, to simplify the whole process, I've implemented a CMake wrapper batch file, which can automate compilation and execution of the project:

```batch
@echo off
setlocal

if not defined VCINSTALLDIR (
    echo Error: No Visual C++ environment found.
    echo Please run this script from a Visual Studio Command Prompt
    echo or run "%%VSnnCOMNTOOLS%%\vcvars32.bat" first.
    goto :EOF
)

echo.%VCINSTALLDIR%|findstr /C:"Visual Studio 9.0" >nul 2>&1
if not errorlevel 1 (
    set VC_VERSION=Visual Studio 9 2008
)

echo.%VCINSTALLDIR%|findstr /C:"Visual Studio 10.0" >nul 2>&1
if not errorlevel 1 (
    set VC_VERSION=Visual Studio 10
)

echo.%VCINSTALLDIR%|findstr /C:"Visual Studio 11.0" >nul 2>&1
if not errorlevel 1 (
    set VC_VERSION=Visual Studio 11
)

echo.%VCINSTALLDIR%|findstr /C:"Visual Studio 12.0" >nul 2>&1
if not errorlevel 1 (
    set VC_VERSION=Visual Studio 12
)

if "%1"=="" goto usage
set BUILD_CMD=%1

if "%BUILD_CMD%"=="all" (
    goto build_all
) else if "%BUILD_CMD%"=="type" (
    goto build_type
) else if "%BUILD_CMD%"=="run" (
    goto build_run
) else if "%BUILD_CMD%"=="cleanall" (
    goto build_cleanall
) else if "%BUILD_CMD%"=="help" (
    goto usage
) else (
    echo Unknown command: %BUILD_CMD%
    echo Type "build help" for available commands.
    goto :EOF
)


:usage
echo Generic Cross-Platform Build System 0.1.2.1 (build 20120221.1)
echo Copyright (C) 2012, Tom Huang Software Consultancy.
echo All rights reserved.
echo.
echo Usage: build ^<command^>
echo.
echo Available commands:
echo   all          build all configurations
echo   type ^<name^>  build the specified Win32 configuration
echo                name = (Debug ^| Release ^| MinSizeRel ^| RelWithDebInfo)
echo   run ^<name^>   build the specified Win32 configuration
echo                name = (Debug ^| Release ^| MinSizeRel ^| RelWithDebInfo)
echo   cleanall     delete all generated folders/files
echo   help         display usage information
goto :EOF


:build_all
if not exist .\build mkdir .\build
pushd .\build
if not exist *.sln ( cmake -G "%VC_VERSION%" .. )
for /F %%a in ('dir /b *.sln') do set SOLUTION_FILE=%%~nxa

devenv %SOLUTION_FILE% /build "Debug|Win32" /project ALL_BUILD
devenv %SOLUTION_FILE% /build "Release|Win32" /project ALL_BUILD
devenv %SOLUTION_FILE% /build "MinSizeRel|Win32" /project ALL_BUILD
devenv %SOLUTION_FILE% /build "RelWithDebInfo|Win32" /project ALL_BUILD
popd
goto :EOF


:build_type
if not exist .\build mkdir .\build
pushd .\build
if not exist *.sln ( cmake -G "%VC_VERSION%" .. )
for /F %%a in ('dir /b *.sln') do set SOLUTION_FILE=%%~nxa
if "%2"=="" (
    set BUILD_CONFIG=Debug
) else (
    set BUILD_CONFIG=%2
)

devenv %SOLUTION_FILE% /build "%BUILD_CONFIG%|Win32" /project ALL_BUILD
popd
goto :EOF


:build_run
if exist .\build (
    for /F %%a in ('dir /b .\build\*.sln') do set SOLUTION_NAME=%%~na
) else (
    echo The .\build folder is not found. You haven't build executables.
    echo Type "build help" for available commands to build the executables.
    goto :EOF
)

if "%2"=="" (
    set BUILD_CONFIG=Debug
) else (
    set BUILD_CONFIG=%2
)

if not exist .\build\bin\%BUILD_CONFIG%\%SOLUTION_NAME%.exe (
    echo Executable not found.
    echo Type "build help" for available commands to build the executables.
    goto :EOF
)

pushd .\build\bin\%BUILD_CONFIG%
%SOLUTION_NAME%.exe
popd
goto :EOF

:build_cleanall
if exist .\build rmdir /s /q .\build
goto :EOF

endlocal
```

You can download the sample project from my [Github repository](https://github.com/tomghuang/qt5-console-example).


### A Console-Type Application with the Event Loop

If you need the event loop in your console-type application, you can use the following `main.cpp` as the starting point:

```cpp
#include <QtCore>
#include <QDebug>

class Task : public QObject
{
    Q_OBJECT

public:
    Task(QObject *parent = 0) : QObject(parent) {}

public slots:
    void run()
    {
        qDebug() << "Hello World from the Event Loop" << endl;
        emit finished();
    }

signals:
    void finished();
};

#include "main.moc"

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    Task *task = new Task(&a);
    QObject::connect(task, SIGNAL(finished()), &a, SLOT(quit()));
    QTimer::singleShot(0, task, SLOT(run()));
    
    return a.exec();
}
```

You can download the sample project from my [Github repository](https://github.com/tomghuang/qt5-console-event-loop-example).

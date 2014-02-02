[Qt](http://qt.nokia.com/) is a cross-platform C++ library that allows you to develop CLI or GUI applications on Windows, Linux, Mac OS X, Windows CE, Symbian, and Maemo. If you want to develop Qt-based applications on Windows, you can use the following instructions to learn how to use Qt in Visual Studio 2008/2010.

1. Download the Qt source code package from [Qt SDK Downloads](http://qt.nokia.com/downloads).
2. Extract the source code to any folder you want. My best practice is putting all third-party libraries under the project folder, so you can get everything you need by checking out the entire project folder from your version control system.
3. Open Visual Studio 2008 Command Prompt. It is under Microsoft Visual Studio 2008 > Visual Studio Tools.
4. In the command prompt, change to the root folder of Qt.
5. Change qmake.conf under <QT-ROOT>\mkspecs\win32-msvc2008. For static linking, you have to change /MT and /NODEFAULTLIB:"MSVCRT"
5. Type the following command to generate the Debug build: c:\Projects\testqt\lib\Qt470>configure -opensource -debug -qt-libjpeg -qt-zlib -qt-libpng -nomake examples -nomake demos -no-exceptions -no-stl -no-rtti -no-qt3support -mmx -sse -static -platform win32-msvc2008
(*) To fix the "api\qscriptextensionplugin.h(43): Error: Undefined interface" problem, you have to delete the src/script/tmp/moc/debug_shared/mocinclude.tmp and the same file in release_shared.then nmake it.
6. Type nmake
7. Type the following command to generate the static linking Release build: c:\Projects\testqt\lib\Qt470>configure -opensource -release -qt-libjpeg -qt-zlib -qt-libpng -nomake examples -nomake demos -no-exceptions -no-stl -no-rtti -no-qt3support -no-scripttools -no-openssl -no-opengl -no-webkit -no-phonon -no-style-motif -no-style-cde -no-style-cleanlooks -no-style-plastique -no-sql-sqlite -mmx -sse -static -platform win32-msvc2008
8. Type nmake

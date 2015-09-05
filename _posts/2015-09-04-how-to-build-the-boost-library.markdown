---
layout: post2
title:  "How to Build the Boost Library"
date:   2015-09-04 16:50:00
tags: c++ boost library build
---

Boost is a set of cross-platform C++ libraries that can work very well with C++ Standard Library. When you cannot find what you want in C++ Standard Library, you can try Boost. In fact, the most useful, mature Boost libraries will eventually be included in C++ Standard Library.

To use Boost, you have to download the library from [the Boost website](http://www.boost.org), and unzip to the folder you want (for example, `C:\Lib\boost`). Some of the Boost libraries are header-only, meaning that to use those libraries, all you have to do is including the header files in your projects. However, some Boost libraries need to be built, and you can use the following steps to build those libraries.

First, go to the root folder of the Boost library and build `b2`:

```
$> bootstrap.bat
```

Then execute the following command to build Boost:

```
$> b2 --build-dir=..\build_1_59 --toolset=msvc-14.0 --build-type=complete stage
```

The `--build-dir` command-line option tells `b2` where to put all the intermediate files; the `--toolset` command-line option specifies the Visual Studio C++ version; the `--build-type=complete` command-line option causes `b2` to build all supported variants of the libraries; the special `stage` target places Boost library binaries in the stage\lib\ subdirectory of the Boost root folder.

After building the Boost library, you can delete the `..\build_1_59` build folder to remove all intermediate files.


#### Reference

* [Getting Started on Windows](http://www.boost.org/doc/libs/1_58_0/more/getting_started/windows.html#identify-your-toolset)

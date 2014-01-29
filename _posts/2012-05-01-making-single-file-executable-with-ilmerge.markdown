---
layout: post2
title:  "Making Single-File Executables with ILMerge"
date:   2012-05-01 10:34:04
tags: dotnet deployment
---

Single-file executable is the most portable application format. To install the application, all you have to do is copying the executable to a specific folder, for example, D:\Bin. If D:\Bin is already in the PATH environment variable, you can access the executable without modifying any system-wide configuration. Besides, there’s no more DLL Hell problems.

However, .NET Platform encourages using tons of DLLs (assemblies), which conflicts this old UNIX wisdom. In a typical project, you may divide your core functionality into a dozen assemblies. Then you may need some third-party libraries that contribute another dozens of assemblies. For a simple and single-purpose utility, this is really overkill.

If you want to create useful utilities in .NET Platform but hate this tons-of-assemblies phenomenon, you can use `ILMerge`. `ILMerge` is a tiny utility from Microsoft Research, which can link all of your application assemblies into a single-file executable. For example, when I ported my code review tool to C#, I ended up having three assemblies: `crvw.exe`, `crvcore.dll`, and `dotnetzip.dll`. In the last step in my build script, I use the following command to merge all these assemblies into a single `crvw.exe`:

```
$> ilmerge /target:winexe /out:..\crvw.exe crvw.exe crvcore.dll dotnetzip.dll
```

It’s that simple to create a single-file executable in .NET Platform.

With tons of .NET libraries and the C# programming language, you already know how to write short and elegant code to implement complicated features. With ILMerge, now you also know how to create an elegant single-file executable that can make our lives much easier.


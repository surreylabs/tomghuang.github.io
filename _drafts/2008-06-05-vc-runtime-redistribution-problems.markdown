http://blogs.msdn.com/nikolad/articles/427101.aspx
http://forums.msdn.microsoft.com/en-US/vcgeneral/thread/6d16ecce-f92b-4c53-a45b-40119c4566a6

I have the same problem:

Same error message,
Visual Studio 2005 Standard Edition, version 8.0.50727.42
Apparently only in debug,
Typically happens after a rebuild all.
The required files do exist in winsxs folder

I believe the problem is some sort of VS5 bug which corrupts the embedded manifest because it tends to not occur till the first rebuild, and the embedded manifest is shorter, ommiting reference to DebugCRT.

??There is a small chance it is also related to VS05 complaining once or twice that cpp files that it created lack correct CR/LF??

(Note: in the following, Ogre is a large open src graphics engine, tinyXML is a handful of c++ files and headers)

For example I have a running Ogre app

I include the tinyXML files and a function that calls them, and a line in main to call that function and press f5 
   (the application runs)
I select rebuild all, then press f5
   (the error occurs)
By removing tinyXML files and rebuilding, program runs again.
This worked 3 times in a row, but on fourth time bug did not reoccur by this method. It'll be back.


NOTE: You can open your EXE inside Visual Studio and examine the embedded manifest as described in (A) below

THIS IS HOW MY MANIFEST APPEARS IN MY EXE WHEN I HAVE THE PROBLEM:
------------------------------------------------------------------
<?xml version="1.0" encoding="UTF-8" standalone="yes"?><assembly manifestVersion="1.0" xmlns="urn:schemas-microsoft-com:asm.v1"></assembly> 
 

THIS IS HOW MY EMBEDDED MANIFEST APPEARS WHEN THINGS ARE WORKING
---------------------------------------------------------
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <dependency>
    <dependentAssembly>
      <assemblyIdentity type="win32" name="Microsoft.VC80.DebugCRT" version="8.0.50608.0" processorArchitecture="x86" publicKeyToken="1fc8b3b9a1e18e3b"></assemblyIdentity>
    </dependentAssembly>
  </dependency>
</assembly>   

Some extra info::
-----------------------------
locations of "MSVCP80D.dll" on my computer:

C:\WINDOWS\WinSxS\x86_Microsoft.VC80.DebugCRT_1fc8b3b9a1e18e3b_8.0.50727.42_x-ww_f75eb16c
C:\Program Files\Microsoft Visual Studio 8\VC\redist\Debug_NonRedist\x86\Microsoft.VC80.DebugCRT
(I also had dirs for amd64 versions)

Found this help at microsoft
 (Troubleshooting C/C++ Isolated Applications and Side-by-side Assemblies)
(A) http://msdn2.microsoft.com/en-us/library/ms235342.aspx

..which refers to
 (Understanding Dependencies of a Visual C++ Application)
(B) http://msdn2.microsoft.com/en-us/library/ms235265.aspx

..which told me about Depends.exe utility
(C) C:\Program Files\Microsoft Visual Studio 8\Common7\Tools\Bin\Depends.exe

I ran Depends.exe and used it to open my application.exe
Depends.exe told me essentially what I already knew, that MSVCP80D.DLL (and two others) could not be located. Not so much useful as comforting to know it shares my pain.



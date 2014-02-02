The following is the command line, which can execute a batch file and keep the console window open:

<pre>
%comspec% /k ""C:\Program Files\Microsoft Visual Studio 8\VC\vcvarsall.bat"" x86
</pre>


Batch files are very useful.

Here is a batch code snippet:

<pre lang="dos" line="1">
@echo off
REM
REM un-install script for SEE4C.
REM
if (%windir%) == () goto WIN31

if not exist %windir%\SEE16.DLL goto TEST2
echo Delete %windir%\SEE16.DLL ?
pause
del %windir%\SEE16.DLL

:TEST2
if not exist %windir%\SEE32.DLL goto DONE
echo Delete %windir%\SEE32.DLL ?
pause
del %windir%\SEE32.DLL
goto DONE

:WIN31

if not exist C:\WINDOWS\SEE16.DLL goto TEST4
echo Delete C:\WINDOWS\SEE16.DLL ?
pause
del C:\WINDOWS\SEE16.DLL

:TEST4
if not exist C:\WINDOWS\SEE32.DLL goto DONE
echo Delete C:\WINDOWS\SEE32.DLL ?
pause
del C:\WINDOWS\SEE32.DLL

:DONE
</pre>


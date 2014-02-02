Sometimes you want to put everything in the module's directory.

<pre lang="cpp" line="1">
CString GetModuleDir()
{
	char drive[_MAX_DRIVE];
	char dir[_MAX_DIR];
	char fname[_MAX_FNAME];
	char ext[_MAX_EXT];
   	char lpFilename[MAX_PATH];

	GetModuleFileName(GetModuleHandle(NULL), lpFilename, MAX_PATH);
	_splitpath( lpFilename, drive, dir, fname, ext );
	dir[strlen(dir)-1] = '\0';

	return CString(drive) + CString(dir);
}
</pre>


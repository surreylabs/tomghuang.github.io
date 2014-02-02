When you write a makefile, you'd like to echo the following line:

<pre lang="text">
    Usage: app.exe <TARGET> [OPTION...]
</pre>

However, when you execute this makefile under Windows, you will get the following error message:

<pre lang="text">
    The syntax of the command is incorrect.
</pre>

This is because that '<' and '>' are special characters. They mean input and output redirect, so that they can't be echoed directly in the command prompt. If you want to output these two characters, you have to use '^' to escape. For example:

<pre lang="text">
    Usage: app.exe ^<TARGET^> [OPTION...]
</pre>

http://blogs.msdn.com/junfeng/archive/2004/05/14/131579.aspx

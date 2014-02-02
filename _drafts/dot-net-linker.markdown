When you want to write a WinForm application, deployment is always a big trouble. That's because you have to package the whole .NET runtime into your installation package, which is more than 30MB.

Now, you can use the following tools (call .NET linker) to link all the necessary assemblies into your application, and make your application much smaller. For example, some one has reported that a small WinForm application only takes about 3MB disk space. Wow, what a improvement!

<ul>
    <li>XenoCode Postbuild 2007</li>
    <li>Thinstall - http://www.thinstall.com</li>
    <li>Salamander .NET Linker, Native Compiler and Mini-Deployment Tool - Salamander .NET Linker, Native Compiler and Mini-Deployment Tool</li>
    <li></li>
</ul>

<a href="http://discuss.techinterview.org/default.asp?biz.5.446479.13">Source</a>
http://discuss.joelonsoftware.com/default.asp?biz.5.563055.31

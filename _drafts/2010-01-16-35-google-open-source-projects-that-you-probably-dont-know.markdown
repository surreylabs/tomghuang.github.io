27Dec2009
35 Google open-source projects that you probably don't know 
Author: 0x1fff 27 Dec 2009 o 14:01:00 Permalink 
Update: 
Currently list is longer than 35 projects, during change from Polish to English I have added one new project - and this is why title says 35 instead 34 ;). After updates there are even more! Sorry for your confusion.
Google is one of the biggest companies supporting OpenSource movement, they released more than 500 open source projects(most of them are samples showing how to use their API). In this article I will try to write about most interesting and free releases from Google, some of them might be abandoned. 

Update: 
List of projects developed at Google and released as opensource (thanks @dobs from reddit) can be displayed also here
Text File processing
Google CRUSH (Custom Reporting Utilities for SHell)
CRUSH is a collection of tools for processing delimited-text data from the command line or in shell scripts. Tutorial how to use it is here
C++ libraries and sources
Google Breakpad
An open-source multi-platform crash reporting system. Breakpad is a minidump-generation library used for snapshotting processes out in the field for later analysis. The format is similar to core files but was developed by Microsoft for it's crash-uploading facility. A minidump-creation library for Mac/Linux has been implemented so that the crash-processing back-end only needs to understand one format.
Google GFlags
The gflags package contains a library that implements commandline flags processing. As such it's a replacement for getopt(). It has increased flexibility, including built-in support for C++ types like string. Here is introduction how to use it.
Google Glog
The glog library implements application-level logging. This library provides logging APIs based on C++-style streams and various helper macros. It can be used under Linux, BSD, and Windows. Here is introduction how to use Glog.
Google PerfTools
These tools are for use by developers so that they can create more robust applications. Especially of use to those developing multi-threaded applications in C++ with templates. Includes TCMalloc, heap-checker, heap-profiler and cpu-profiler. Instructions how to use PerfTools can be found here and here.
Google Sparse Hash
An extremely memory-efficient hash_map implementation. 2 bits/entry overhead. The SparseHash library contains several hash-map implementations, including implementations that optimize for space or speed. The Google sparsehash package consists of two hashtable implementations: sparse, which is designed to be very space efficient, and dense, which is designed to be very time efficient. For each one, the package provides both a hash-map and a hash-set, to mirror the classes in the common STL implementation. Docs are here.
Omaha - Google Update
Omaha, otherwise known as Google Update, is a program to install requested software and keep it up to date. So far, Omaha supports many Google products for Windows, including Google Chrome and Google Earth, but there is no reason for it to only support Google products. Here is Omaha Overview and Developers Setup Guide.
Protocol Buffers
Protocol Buffers are a way of encoding structured data in an efficient yet extensible format. Google uses Protocol Buffers for almost all of its internal RPC protocols and file formats. Here is developer guide, this protocol can be used in many languages and it is suported by few IDE - for example NetBeans
The Internet
Google Code Prettify
A Javascript module and CSS file that allows syntax highlighting of source code snippets in an html page. It supports: C/C++, Java, Python, Ruby, PHP, VisualBasic, AWK, Bash, SQL, HTML, XML, CSS, JavaScript, Makefiles and some Perl. Not supported: Smalltalk and all *CAML*. For example click here
SpriteMe - easy "CSS sprites"
SpriteMe makes it easy to create CSS sprites (connect many small images to one larger to reduce new connections to webserver when loading webpage). This projects is also available as service under: http://spriteme.org/.
Redacisaurus
Reducisaurus is a web service for minifying and serving CSS and JS files. Reducisaurus is based on YUI Compressor and runs on AppEngine.
JaikuEngine
JaikuEngine is a social microblogging platform that runs on AppEngine. JaikuEngine powers Jaiku.com. For the mobile client source, see: Jaiku Mobile client. Here is README for project
Selector Shell
The Selector Shell is a browser-based tool for testing what CSS becomes in different browsers. It works by taking some raw text, inserting a dynamic STYLE element into the HEAD with that raw text as its content, and then reading the CSSOM to see what the browser has parsed it into. It is written in Javascript. It can be tested here.
Google Feed Server
Google Feed Server is an open source Atom Publishing Protocol server based on the Apache Abdera framework. Google Feed Server provides a simple back end for data adapters, which allows developers to quickly deploy a feed for an existing data source such as a database. Google Feed Server also provides the Feed Server Client Tool (FSCT), which lets developers perform create, receive, update, and delete (CRUD) operations on a Feed Server feed. Here are links to start it up and get running.
Melange, the Spice of Creation
The goal of this project is to create a framework for representing Open Source contribution workflows, such as the existing Google Summer of Code TM (GSoC) program. Using this framework, it will be possible to host future Google Summer of Code programs (and other similar programs, such as the Google Highly Open Participation TM Contest, or GHOP) on Google App Engine. Here you can checkout Getting Started Guide
NameBench
This project hunts down the fastest DNS servers available for your computer to use. namebench runs a fair and thorough benchmark using your web browser history, tcpdump output, or standardized datasets in order to provide an individualized recommendation. namebench is completely free and does not modify your system in any way. This project began as a 20% project at Google. namebench runs on Mac OS X, Windows, and UNIX, and is available with a graphical user interface as well as a command-line interface. BTW: Google has own free public caching DNS servers at ip: 8.8.8.8 i 8.8.4.4.
Rat Proxy
A semi-automated, largely passive web application security audit tool, optimized for an accurate and sensitive detection, and automatic annotation, of potential problems and security-relevant design patterns based on the observation of existing, user-initiated traffic in complex web 2.0 environments. It detects and prioritizes broad classes of security problems, such as dynamic cross-site trust model considerations, script inclusion issues, content serving problems, insufficient XSRF and XSS defenses, and much more. Docs are here. Project is written and maintained by MichaÅ‚ Zalewski (lcamtuf).
TopDraw
Top Draw is an image generation program. By using simple text scripts, based on the JavaScript programming language, Top Draw can create surprisingly complex and interesting images. The cool part is that the program has built in support for taking your image and installing it as your desktop image. There's even a Viewer application that can be installed in the menubar to automatically run with the parameters (such as the selected script, update interval) that you've specified. The projects is developed in XCode, and runs on: Mac OS X 10.5 (Leopard) or later.
etherpad
Open source release of EtherPad, a web-based realtime collaborative document editor. This project exists mainly as an exhibition of the code, to help support those who want to run or modify their own etherpad servers, or for those who are curious about how etherpad's algorithms make realtime collaboration possible. Here are some instructions how to build etherpad, and screencast what is all about. Etherpad uses JavaScript, Java and Comet server for make real time collaboration make working.
Chromium
Chromium is the open-source project behind Google Chrome. Chromoium project is about create a powerful platform for developing a new generation of web applications. There are not so many differences between Chrome and Chromium. Here are instructions how to build Chromium on Linux. Tere are also official releases of Chrome for Windows, Mac and Linux.
V8 Google's open source JavaScript engine
V8 is Google's open source JavaScript engine. V8 is written in C++ and is used in Google Chrome, the open source browser from Google. V8 implements ECMAScript as specified in ECMA-262, 3rd edition, and runs on Windows XP and Vista, Mac OS X 10.5 (Leopard), and Linux systems that use IA-32 or ARM processors. V8 can run standalone, or can be embedded into any C++ application, here are some helpfull docs how to begin.
Chromium OS
Chromium OS is an open-source project that aims to build an operating system that provides a fast, simple, and more secure computing experience for people who spend most of their time on the web. Sources are available on: http://git.chromium.org/ src
Android
Android is the first free, open source, and fully customizable mobile platform. Android offers a full stack: an operating system, middleware, and key mobile applications. It also contains a rich set of APIs that allows third-party developers to develop great applications.
Tools for MySQL
Google MySQL Tools
Various tools for managing, maintaining, and improving the performance of MySQL databases, originally written by Google. This includes: 
â€¢	mypgrep.py - a tool, similar to pgrep, for managing mysql connections
â€¢	compact_innodb.py - compacts innodb datafiles by dumping and reloading all tables
Google mMAIM
mMAIM's purpose is to make it easy to monitor and analyze MySQL servers and to easily integrate itself into any environment. It can show Master/Slave sync stats, some efficiency stats, can return statistics from most of the "show" command, and more!
Other projects
Stressful Application Test (stressapptest)
Stressful Application Test (or stressapptest, its unix name) tries to maximize randomized traffic to memory from processor and I/O, with the intent of creating a realistic high load situation in order to test the existing hardware devices in a computer. It has been used at Google for some time and now it is available under the apache 2.0 license. Here are some docs: Introduction, Installation Guide and User Guide
Pop and IMAP Troubleshooter
The POP and IMAP troubleshooter serves to diagnose and solve connection problems from client machines to email services. It reads the client configuration files (Outlook, Windows Mail, Thunderbird, etc.), checks the individual settings, and then attempts to create POP, IMAP, and SMTP connections using these settings. The troubleshooter is coded in C++ using the Qt environment. It can be used generically, or can be customized for the demands of a particular email service. 
OpenDuckBill
Openduckbill is a simple command line backup tool for Linux, which is capable of monitoring the files/directories marked for backups for any changes and transferring these changes either to a local backup directory or a remote NFS exported partition or to a remote ssh server using the very common, rsync command. Here is installation guide. 
ZXing
ZXing (pronounced "zebra crossing") is an open-source, multi-format 1D/2D barcode image processing library implemented in Java. Our focus is on using the built-in camera on mobile phones to photograph and decode barcodes on the device, without communicating with a server. As far I know it can be found on Android Platform. Checkout Getting stared guide, and chackout list of supported devices (My SonyEricson device is capable!).
Tesseract OCR Engine
The Tesseract OCR engine was one of the top 3 engines in the 1995 UNLV Accuracy test. Between 1995 and 2006 it had little work done on it, but it is probably one of the most accurate open source OCR engines available. The source code will read a binary, grey or color image and output text. A tiff reader is built in that will read uncompressed TIFF images, or libtiff can be added to read compressed images. Here is: Readme and FAQ
Neatx - Open Source NX server
Neatx is an Open Source NX server, similar to the commercial NX server from NoMachine. For more information checkout Project Homeppage. NX protocol is way more roboust than VNC (it can be usefull when having slow Internet connection). Major differences between NX and VNC: 
â€¢	NX is X11 client it doesn't send bitmaps
â€¢	NX works with X, VNC and Remote Desktop (Windows)
â€¢	NX buffers data
â€¢	NX is easy to install (link in Polish)
Alternative to Google project can be FreeNx (not tested).
PSVM
It is the code of the following paper: http://books.nips.cc/papers/files/nips20/NIPS2007_0435.pdf. This is an all-kernel-support version of SVM, which can parallel run on multiple machines. Here is usage. 
The GO programming language
New programming language developed in Google. It is released using this slogan: "GO a systems programming language expressive, concurrent, garbage-collected"
The Google Collections Library for Java
The Google Collections Library is a set of new collection types, implementations and related goodness for Java 5 and higher, brought to you by Google. It is a natural extension of the Java Collections Framework you already know and use.
Google styleguide
Every major open-source project has its own style guide: a set of conventions (sometimes arbitrary) about how to write code for that project. It is much easier to understand a large codebase when all the code in it is in a consistent style. "Style" covers a lot of ground, from â€œuse camelCase for variable namesâ€ to â€œnever use global variablesâ€ to â€œnever use exceptions.â€ This project holds the style guidelines we use for Google code. If you are modifying a project that originated at Google, you may be pointed to this page to see the style guides that apply to that project. This is worth reading.
Summary
Google is one of the most active companies releasing open source software, on top of that Google 5 times organized Summer Of Code - project where students from all over the world start working for OpenSource and Google pays them scholarship for few months of hard work. 
Update
Guice a lightweight dependency injection framework for Java 5 and above
Thanks JavaBeat for summary.Google Guice is a Dependency Injection Framework that can be used by Applications where Relation-ship/Dependency between Business Objects have to be maintained manually in the Application code. Since Guice support Java 5.0, it takes the benefit of Generics and Annotations thereby making the code type-safe.Documentation is here: Getting stared guide
Google Sitebrics - web framework powered by Guice
Sitebricks is a simple development layer for web applications built on top of Google Guice. Sitebricks focuses on early error detection, low-footprint code, and fast development. Like Guice, it also balances idiomatic Java with an emphasis on concise code.
Here is Getting Started guide and 5 minute tutorial. 
Google ctemplate
CTemplate is a simple but powerful template language for C++. It emphasizes separating logic from presentation: it is impossible to embed application logic in this template language. Here is some documentation. 

Thanks nostrademons from reddit.com
Google C++ Mocking Framework
This project was inspired by jMock, EasyMock, and Hamcrest, and designed with C++'s specifics in mind, Google C++ Mocking Framework (or Google Mock for short) is a library for writing and using C++ mock classes. Google Mock: 
â€¢	lets you create mock classes trivially using simple macros,
â€¢	supports a rich set of matchers and actions,
â€¢	handles unordered, partially ordered, or completely ordered expectations,
â€¢	is extensible by users, and
â€¢	works on Linux, Mac OS X, Windows, Windows Mobile, minGW, and Symbian.
Here is Getting Started guide, and Google C++ Mocking for dumies. 

Thanks richq from reddit.com
Google C++ Testing Framework
Google's framework for writing C++ tests on a variety of platforms (Linux, Mac OS X, Windows, Cygwin, Windows CE, and Symbian). Based on the xUnit architecture. Supports automatic test discovery, a rich set of assertions, user-defined assertions, death tests, fatal and non-fatal failures, value- and type-parameterized tests, various options for running the tests, and XML test report generation. Here is Google Test Primer and here is Google Test Dev Guide. 

Thanks richq from reddit.com
Google Toolbox for Mac
Is collection of source code from different Google projects, that may be useful to developers working on Macintosh. This package includes the Google Developer Spotlight Importers. The release notes can be found here. 

Thanks buffi from reddit.com 
OCRopus
This is not entirely Google Project but it is donated by Google. OCRopus(tm) is a state-of-the-art document analysis and OCR system, featuring pluggable layout analysis, pluggable character recognition, statistical natural language modelling, and multi-lingual capabilities. The OCRopus engine is based on two research projects: a high-performance handwriting recognizer developed in the mid-90's and deployed by the US Census bureau, and novel high-performance layout analysis methods. OCRopus is development is sponsored by Google and is initially intended for high-throughput, high-volume document conversion efforts. We expect that it will also be an excellent OCR system for many other applications. Here is usage guide and guide how to install development version 

Thanks 13xforever from from reddit.com 
Ganeti
Ganeti is a cluster virtual server management software tool built on top of existing virtualization technologies such as Xen or KVM and other Open Source software. Ganeti requires pre-installed virtualization software on your servers in order to function. Once installed, the tool will take over the management part of the virtual instances (Xen DomU), e.g. disk creation management, operating system installation for these instances (in co-operation with OS-specific install scripts), and startup, shutdown, failover between physical systems. 

Thanks Matt Brown and btgeekboy from reddit.com 
skia
Skia is a complete 2D graphic library for drawing Text, Geometries, and Images. 
â€¢	3x3 matrices w/ perspective
â€¢	antialiasing, transparency, filters
â€¢	shaders, xfermodes, maskfilters, patheffects
Projects using skia are: Android and Chrome. 

Thanks zxn0 from reddit.com
Google URL parsing and canonicalization library
A small library for parsing and canonicalizing URLs. You can find README here. 

Thanks pkasting 
libjingle
Libjingle, the Google Talk Voice and P2P Interoperability Library, is a set of components provided to interoperate with Google Talk's peer-to-peer file sharing and voice calling capabilities (in source are some samples how to build p2p app). The package includes source code for Google's implementation of Jingle and Jingle-Audio, two proposed extensions to the XMPP standard that are currently available in draft form both Windows and UNIX/Linux operating systems. Here is Developer Guide 

Thanks jbking 
WebDriver (Selenium)
Webdriver is sophisticated tool for automating web UI testing. It has a simple API designed to be easy to work with and can drive both real browsers, for testing javascript heavy applications, and a pure 'in memory' solution for faster testing of simpler applications. You can checkout the 5 minute introduction on GettingStarted page. Currently project is moved to http://selenium.googlecode.com/ For the latest source, please go there. 

Thanks ittiam 
Google Gears
Gears is an open source project that enables more powerful web applications, by adding new features to your web browser: 
â€¢	Let web applications interact naturally with your desktop
â€¢	Store data locally in a fully-searchable database
â€¢	Run JavaScript in the background to improve performance 
Gears are the fastest way to make your web app more like desktop app 

Thanks Anonymous. 
Google Web Toolkit (GWT)
Google Web Toolkit (GWT) is a development toolkit for building and optimizing complex browser-based applications. GWT is used by many products at Google, including Google Wave and Google AdWords. It's open source, completely free, and used by thousands of developers around the world. 

Thanks Anonymous. 
Native Client
Native Client is an open-source technology for running native code in web applications, with the goal of maintaining the browser neutrality, OS portability, and safety that people expect from web apps. It has been released at an early stage to get feedback from the open-source community. Probably Native Client technology will help web developers to create richer and more dynamic browser-based applications. Native Client runs on 32-bit x86 systems that use Windows, Vista, Mac OS X, or Linux. Some ARM and x86-64 support is implemented in the source base, and we hope to make it available for application developers later this year. Here is Getting started guide and FAQ. 

zxn0 and ptman from reddit.com 

Currently Native Client can run Quake in your browser! :) 
Google Gadgets for Linux
Google Gadgets for Linux provides a platform for running desktop gadgets under Linux, catering to the unique needs of Linux users. It's compatible with the gadgets written for Google Desktop for Windows as well as the Universal Gadgets on iGoogle. Following Linux norms, this project is open-sourced under the Apache License. Here is Getting Started Guide and instructions how to build project. 

Thanks Tiger Dong
Google Caja
Caja allows websites to safely embed DHTML web applications from third parties, and enables rich interaction between the embedding page and the embedded applications. 

Thanks phosphorescente from from reddit.com 
scarcity
Scarcity is a framework for concurrent garbage collection in C++. The framework is organized around the principle of "policy-based design", meaning that behavior are customized and extended via template parameters. Policy-based design facilitates seamless integration with a broad set of VMs and other runtime environments by allowing the host environment to replace any aspect of the framework, such as thread synchronization primitives, atomic data types, error logging facilities, tracing strategies and so on.
Google concurrency library
A concurrency library for C++. Here is getting started guide.
Cppclean
CppClean attempts to find problems in C++ source that slow development particularly in large code bases. It is similar to lint; however, CppClean focuses on finding global inter-module problems rather than local problems similar to other static analysis tools. The goal is to find problems that slow development in large code bases that are modified over time leaving unused code. This code can come in many forms from unused functions, methods, data members, types, etc to unnecessary #include directives. Unnecessary #includes can cause considerable extra compiles increasing the edit-compile-run cycle. 

Here are some details about implementation 
Unladen swallow
An optimized branch of CPython, intended to be fully compatible and significantly faster. Unladen Swallow is Google-sponsored, but not Google-owned. The engineers on the project are full-time Google engineers, but ultimately this an open-source project, not really that different from Chrome or Google Web Toolkit. Here is Getting Started Guide. 



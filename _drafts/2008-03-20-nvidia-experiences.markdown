I've learned a lot from NVIDIA. Here are something that I want to keep in mind.

NVIDIA is a bug-driven company. You work on bugs everyday, and keep on receiving more bugs everyday. The bugs that we mentioned here are not all "real" bugs. Some of the bugs are actually feature requests. So maybe "task" is a more appropriate term than "bug". To achieve that, NVIDIA has its own bug tracking system: NVBug. You can create, edit, and search bugs in the web-based system. Management folks heavily rely on this system to generate analysis data, so that they can keep track of each employee's performance and status. We, as poor engineers, have to keep tracking our own bugs and try to solve bugs ASAP. NVIDIA evaluates its employees every six months, and how many bugs have you solved during the six months is the major factor of your performance (maybe the only one factor).

To support such a large company and extremely comlex software development, NVIDIA has all the necessary software engineering intrastructure. NVBug (issue tracking) is only one of them. One of the tools we have to use everyday is the Wiki system. You can get most of the technical information from Wiki systems. In NVIDIA, we have several Wiki systems. Each group has its own Wiki, and each Wiki has different focus. In the software engineering wiki, you can find out all kinds of information about driver debugging, hard-to-learn experience. Anyway, this is how NV collects the intellectual property from all the employees, and it is a very efficient way. Of course, there are some documents are in other formats, such as Word, PDF, Excel, and pure text. All these documents are stored on a central file server. To search both Wiki and files on the server, we have a internal Google search engine, which can index all the information in NVIDIA. Google search engine is much better than the one in the wiki system. So, to make knowledge base a useful tools for everyone, you have to provide something like wiki, and also a powerful search engine.

Besides the wiki system, there are other kinds of web-based tools. To be brief, most of the tools we use everyday have web interface, so that we can easily access the systems. For example, the Buildmeister system automatically builds the driver and all kinds of tools everyday. We can use http://buildweb to figure out build numbers and branches. The Concure system, which can process our travel expense, also use web interface. These systems not only use web interface to provide services, they also use email system to notify people. That's why we always receive lots of email messages from all kinds of system, such as Buildmeister, Concour, NVBug, DVS, NVInfo, etc. To categorize messages, we have to use filters in Outlook. After setting filters, messages will go to their own folders automatically.

Next is one of the most important tools in software engineering, the version control system. In NVIDIA, we use Perforce as our version control system. This is a commercial product from Perforce (www.perforce.com). It is also a very expensive package (a single license requires about $280). I don't know why NVIDIA doesn't use Subversion, which I used before joining NVIDIA. One of the feature that is not implemented in Subversion yet, is changelist. You can group changed files and submit to the server separately. I know that someone already suggest to add this feature in Subversion, but I'm not sure when it will be finished.

Before you submit your changes to the server, you have to use P4Merge to create a diff package and send it to related engineers for reviewing. After everyone agrees your changes, you can submit to the server. Before you hit the submit button, you have to mention two things in the comment: the bug ID that the chagelist is for, and the engineers who approve this changelist. If you don't write these two things, the server will not allow you to submit the changelist. This is really a great mechanism, which force us to bind every changelist to a specific bug ID and reviewers. It can help us to track why we made a change severa months ago and who are involved with this change. Without this mechanism, in my experiences, there will be a lot of "ghost changelists", which are hard to find out the original intension to do the modification.

Before you submit your changes, you have to do what we called "virtual DVS", which means you have to submit the changelists to the DVS server. The DVS system is maintained by a group of engineers. It can build the driver and run automation test cases against the driver. If you can not pass virtual DVS, you can't submit your changelists. Test automation is a very important component is contemporary software engineering. It can maintain a baseline of code base. In NVIDIA, DVS is a huge system and very complex. For large system, test automation is really very important. Without it, you can not be confidence about the quality of your products.

Another important technique I learned from NVIDIA is kernel mode debugging using Windbg. I never used Windbg before joining NVIDIA. The most important things I want to mention about Windbg are its architecture and symbol/source server mechanism.

It is hard to find a good design for software engineering tools. In Afatech, I was resposible for designing and implementing variouis kinds of tools. The tools need to be powerful and flexible. It should not be too complicated. In the future, I will use Windbg as a good model, and develop something like Windbg. The plugin mechanism of Windbg is simple and powerful. By implementing a few interface and put the plugin dll in a specific folder, Windbg can automatically find out the plugin modules and load them into the workspace.



<server>/<build>/<product>/<os_build>/<version>/<customer>/<system>/...

At the same time, NV provides FTP to download binaries.
If you are confused about versions, you can use http://buildweb interface to search for the versions you want, and
download the versions from the interface directly.

It seems that VPN is a must-have in a coporate environment. When we are not in our cubes, we have to use VPN to access the intranet. At this time, web interface is very convenient. You don't need Outlook to access your email. We have another web interface, http://owa (Outlook Web Access, maybe).


NV is a big company. There are all kinds of software tools in this large IC design company.
<ul>
    <li>Stand-alone debug utilities (swak, ubercopy, nvflash, PerfHUD, balls, etc.)</li>
    <li>Windbg debug extensions (nvWatch, etc.)</li>
    <li>3D Modeling IDE (FX Composer 2)</li>
    <li>Test Automation (DVS, MODS, etc.)</li>
    <li>SDK (CUDA, etc.)</li>
    <li>Domain specific language (Cg)</li>
    <li>Issue tracking system (NVBug)</li>
    <li>Build automation (nvmake)</li>
</ul>


Another important thing I've learned is the format of weekly reports. Basically there're two kinds of weekly reports: one is for engineers, and the other is for managers. In engineers' weekly reports, there are four sections:

<ul>
    <li>Last Week's Plan</li>
    <li>Problem</li>
    <li>Progress</li>
    <li>Next Week's Plan</li>
</ul>

/////////////////////////////////////////////////////
Weekly Report Best Practice
From Gpuhwdept
Parent Page: ASIC_New_Hire_Orientation 
Owner: fawang 
Customer: customer_alias 
Feedback: please email fawang or file a bug here
The major purpose of a weekly report is to help management understand the healthy of the project. Please follow the format and guildelines presented below when drafting a weekly report. 

Issues 

This is where you bring up blocking items that prevent you from getting your job done, you should 

Let management know if a milestone is going to slip and be specific about the reasons (insufficient resources, unexpected complexities, dependancies and etc.) 
Complain if you think you are overloaded 
Prioritize and colorize your issues 
Bring up your issue as early as you can predicate 
Be proative, make suggestions about how to resolve your issues 
Theoretically, this is the only section that management cares. If you have no issues, that means you have no problem holding your commitments. 

Goals for the next 30 days 

List the milestones that you are working on 

In order of time 
Must align with project milestones 
Must be reviewed and agreed with your lead 
Must be a S-M-A-R-T goal 
Specific 
Measurable 
Achievable 
Result-Oriented 
Timed 
As part of the team, your personal goals must align with project plan. It's also important to be measurable and agreed upon. 

Tasks completed last week 

Briefly talk about what you have been achieved during the past week. Give some details as required by unit lead or project lead. The information given here should also back up your issues. 

Time & Vacation 

How do you spend your time? If you work on multiple projects, specify the percentage of the time you spend on each project. This becomes important when one of your issue is "overloaded" or "distracted". For example, if you are suppose to deliver something for gt218, but you spent 80% of time working on g98, that should be reflected here.

/////////////////////////////////////////////////////

Parent Page: ASIC_New_Hire_Orientation 
Owner: fawang 
Customer: customer_alias 
Feedback: please email fawang or file a bug here
The major purpose of a weekly report is to help management understand the healthy of the project. Please follow the format and guildelines presented below when drafting a weekly report. 

Issues 

This is where you bring up blocking items that prevent you from getting your job done, you should 

Let management know if a milestone is going to slip and be specific about the reasons (insufficient resources, unexpected complexities, dependancies and etc.) 
Complain if you think you are overloaded 
Prioritize and colorize your issues 
Bring up your issue as early as you can predicate 
Be proative, make suggestions about how to resolve your issues 
Theoretically, this is the only section that management cares. If you have no issues, that means you have no problem holding your commitments. 

Goals for the next 30 days 

List the milestones that you are working on 

In order of time 
Must align with project milestones 
Must be reviewed and agreed with your lead 
Must be a S-M-A-R-T goal 
Specific 
Measurable 
Achievable 
Result-Oriented 
Timed 
As part of the team, your personal goals must align with project plan. It's also important to be measurable and agreed upon. 

Tasks completed last week 

Briefly talk about what you have been achieved during the past week. Give some details as required by unit lead or project lead. The information given here should also back up your issues. 

Time & Vacation 

How do you spend your time? If you work on multiple projects, specify the percentage of the time you spend on each project. This becomes important when one of your issue is "overloaded" or "distracted". For example, if you are suppose to deliver something for gt218, but you spent 80% of time working on g98, that should be reflected here. 

Retrieved from "https://gpuhwdept:443/index.php/Weekly_Report_Best_Practice"

///////////////////////////////////////////////////////////////////


One day when I had to measure the performance of some part of the code, I found that the simplest way to do that in a kernel mode driver is to use KeQueryPerformanceCounter. If your platform support high resolution counter, than you can use this kernel mode API function to measure the time. Notice that, not all platforms support this API, only the one that has high resolution counter. When I used this API, I found it difficult to manipulate LARGE_INTEGER data type. LARGE_INTEGER is actually a union, so that there're some tricks to use this data type.

http://www.microsoft.com/taiwan/whdc/system/sysinternals/mm-timer.mspx

	LARGE_INTEGER ticks;
	LARGE_INTEGER tickfreq;
	ticks = KeQueryPerformanceCounter(&tickfreq);
	DbgPrintEx(0, 0, "setPowerState start: %I64d, %I64d\n", ticks.QuadPart, tickfreq.QuadPart);

Notice that, I64d is used to format 64-bit integers. If you want to get the 64-bit integer value, you have to use QuadPart of the LARGE_INTEGER union. DbgPrintEx is a DDK API. You can use this function to output any string to the Windbg console.


/////////////////////////////////////////////////////

Blog is used to post messages, and Wiki is used to organize messages/knowledge. They are two different kind of tools.


/////////////////////////////////////////////////////
There is only one driver binary, but there're a lot of different INF configuration, so that different customer has its own setup program.

http://msdn2.microsoft.com/en-us/library/cc305229.aspx

From the comment of bug 407232:

Tom, 

You could use a MSFT tool, xperf to get s3 enter time. 
the tool is downloadable from: http://www.microsoft.com/whdc/system/sysperf/perftools.mspx 

Run the following commands with the test driver installed 

1) xbootmgr -trace standby -numRuns 3 (runs 3 iterations) 
--> generates an etl file for each iteration. 

2) xperf -i "standby_BASE+CSWITCH_1.etl" -o s3_1.xml -a suspend 
--> convert etl file to xml stats. 

Look for suspenddevices stats in the xml, where you can find the overall suspend time and time taken by NV driver. 

This is a standard tool provided by MSFT. OEM's also use this tool to measure S3 perf. 

(From Chinmay Kale <ckale@nvidia.com>)


<pre lang="cpp" line="1">
LARGE_INTEGER ticks;
LARGE_INTEGER tickfreq;
ticks = KeQueryPerformanceCounter(&tickfreq);
DbgPrintEx(0, 0,
           â€œsetPowerState start: %I64d, %I64dnâ€,
           ticks.QuadPart, tickfreq.QuadPart);
</pre>


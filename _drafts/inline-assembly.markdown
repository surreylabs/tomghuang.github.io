A <strong>simple</strong> example. Please notice that, <code>0x72</code> and <code>0x73</code> are IO port addresses for <code>0x4F</code>. In my current case, I have to use <code>0x70</code> and <code>0x71</code> to read/write <code>0x3B</code>.

<pre name="code" class="c">
extern "C" void
myIoWriteByte(unsigned int uPort, unsigned char uData)
{
    __asm
    {
        push    edx
        push    eax
        mov     edx, uPort
        mov     al, uData
        out     dx,al
        pop     eax
        pop     edx
    }
}

extern "C" unsigned char
myIoReadByte(unsigned int uPort)
{
    U008    uData;
    __asm
    {
        push    edx
        push    eax
        mov     edx, uPort
        in      al, dx
        mov     uData, al
        pop     eax
        pop     edx
    }
    return( uData );
}


void WriteCMOS0x4F(unsigned char value)
{
    myIoWriteByte(0x72, 0x4F);
    myIoWriteByte(0x73, value);
}

unsigned char ReadCMOS0x4F(void)
{
    myIoWriteByte(0x72, 0x4F);
    return myIoReadByte(0x73);
}
</pre>


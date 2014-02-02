<pre lang="cpp" line="1">
#define isdigit(c)      (((c)>='0') && ((c)<='9'))


// Case insensitive version of strncmp(s1,s2,n);
static int strncasecmp(const char *s1, const char *s2, int n)
{
    int i;
    unsigned char c1, c2;

    if(s1==s2 || n==0) return 0;

    for(i=0;i<n;i++)
    {
        c1 = (unsigned char)tolower(s1[i]);
        c2 = (unsigned char)tolower(s2[i]);
        if (c1 == '\0' || c1 != c2)
            return c1 - c2;
    }
    return 0;
}

// The following snippet shows how to predefine an array
// of a specific type and the size of the array.

// list of all possible gpu offsprings
static GPUCHILDHANDLE gpuChildHandleList[] =
{
    {ENG_MC,     ODB_CLASS_MASTER_CONTROL,    ODB_NO_ID},
    {ENG_FB,     ODB_CLASS_FB,                ODB_NO_ID},
    {ENG_DAC,    ODB_CLASS_DISPLAY,           ODB_NO_ID},
    {ENG_VIDEO,  ODB_CLASS_VIDEO,             ODB_NO_ID},
    {ENG_TMR,    ODB_CLASS_TIMER,             ODB_NO_ID},
    {ENG_BUS,    ODB_CLASS_BUS,               ODB_NO_ID},
    {ENG_DMA,    ODB_CLASS_DMA,               ODB_NO_ID},
    {ENG_GR,     ODB_CLASS_GRAPHICS,          ODB_NO_ID},
    {ENG_FIFO,   ODB_CLASS_FIFO,              ODB_NO_ID},
    {ENG_MP,     ODB_CLASS_MEDIAPORT,         ODB_NO_ID},
    {ENG_ME,     ODB_CLASS_MOTION_ESTIMATION, ODB_NO_ID},
    {ENG_MPEG,   ODB_CLASS_MPEG,              ODB_NO_ID},
    {ENG_HBLOAT, ODB_CLASS_HBLOAT,            ODB_NO_ID},
    {ENG_BRDG,   ODB_CLASS_BRDG,              ODB_NO_ID},
    {ENG_SW,     ODB_CLASS_SPREAD_SPECTRUM,   ODB_NO_ID},
    {ENG_CLK,    ODB_CLASS_CLK,               ODB_NO_ID},
    {ENG_SW,     ODB_CLASS_SEQ,               ODB_NO_ID},
    {ENG_SW,     ODB_CLASS_PERF,              ODB_NO_ID},
    {ENG_THERMAL,ODB_CLASS_THERM,             ODB_NO_ID},
    {ENG_VP,     ODB_CLASS_VIDEO_PROCESSOR,   ODB_NO_ID},
    {ENG_CIPHER, ODB_CLASS_CIPHER,            ODB_NO_ID},
    {ENG_BSP,    ODB_CLASS_BSP,               ODB_NO_ID},
    {ENG_SW,     ODB_CLASS_VBIOS,             ODB_NO_ID},
    {ENG_SW,     ODB_CLASS_GPIO,              ODB_NO_ID},
    {ENG_SW,     ODB_CLASS_VOLT,              ODB_NO_ID},
    {ENG_SW,     ODB_CLASS_I2C,               ODB_NO_ID},
    {ENG_SW,     ODB_CLASS_RC,                ODB_NO_ID},
    {ENG_SW,     ODB_CLASS_STEREO,            ODB_NO_ID},
    {ENG_SW,     ODB_CLASS_INTR,              ODB_NO_ID},
    {ENG_DPAUX,  ODB_CLASS_DPAUX,             ODB_NO_ID},
    {ENG_PMU,    ODB_CLASS_PMU,               ODB_NO_ID},
    {ENG_PPP,    ODB_CLASS_PPP,               ODB_NO_ID},
    {ENG_CE,     ODB_CLASS_CE,                ODB_NO_ID}
};

#define GPU_NUM_CHILD_OBJECTS \
    ((sizeof (gpuChildHandleList) / sizeof (GPUCHILDHANDLE)))


// Use enumeration to define a set of constants.

typedef enum
{
    ODB_CLASS_UNKNOWN,
    ODB_CLASS_SYSTEM,
    ODB_CLASS_CORELOGIC,
    ODB_CLASS_GPUMGR,
    ODB_CLASS_SYSCON,
    ODB_CLASS_PLATFORM,
    ODB_CLASS_OS,
    ODB_CLASS_CPU,
    ODB_CLASS_HAL,
    ODB_CLASS_GPU,
    ODB_CLASS_SMU,
    ODB_CLASS_HBLOAT,
    ODB_CLASS_MASTER_CONTROL,
    ODB_CLASS_BUS,
    ODB_CLASS_BRDG,
    ODB_CLASS_BIF,
    ODB_CLASS_FB,
    ODB_CLASS_GRAPHICS,
    ODB_CLASS_FIFO,
    ODB_CLASS_DMA,
    ODB_CLASS_MPEG,
    ODB_CLASS_DISPLAY,
    ODB_CLASS_CAPTURE,
    ODB_CLASS_HEAD,
    ODB_CLASS_DAC,
    ODB_CLASS_SOR,
    ODB_CLASS_PIOR,
    ODB_CLASS_OD,
    ODB_CLASS_CRT,
    ODB_CLASS_DFP,
    ODB_CLASS_TVD,
    ODB_CLASS_TIMER,
    ODB_CLASS_MEDIAPORT,
    ODB_CLASS_VIDEO,
    ODB_CLASS_VBIOS,
    ODB_CLASS_DAC_Invalid,
    ODB_CLASS_DAC_Component,
    ODB_CLASS_DAC_CRTC,
    ODB_CLASS_DAC_DisplayEncoder,
    ODB_CLASS_DAC_Display,
    ODB_CLASS_DAC_AnalogEncoder,
    ODB_CLASS_DAC_DigitalEncoder,
    ODB_CLASS_DAC_TVEncoder,
    ODB_CLASS_DAC_AnalogDisplay,
    ODB_CLASS_DAC_DigitalDisplay,
    ODB_CLASS_DAC_TVDisplay,
    ODB_CLASS_DAC_Platform,
    ODB_CLASS_DAC_NVDigitalEncoder,
    ODB_CLASS_DAC_DisplayPath,
    ODB_CLASS_DAC_BootManagedPlatform,
    ODB_CLASS_DAC_MacP80Display,
    ODB_CLASS_DAC_ExternalDevice,
    ODB_CLASS_DAC_ExternalDevice_P154,
    ODB_CLASS_DAC_ExternalDevice_P207,
    ODB_CLASS_DAC_ExternalDevice_P209,
    ODB_CLASS_DAC_ExternalDevice_P294,
    ODB_CLASS_DAC_ExternalDevice_P358,
    ODB_CLASS_DAC_ExternalDevice_P359,
    ODB_CLASS_HEAP,
    ODB_CLASS_EHEAP,
    ODB_CLASS_SPREAD_SPECTRUM,
    ODB_CLASS_CLK,
    ODB_CLASS_SEQ,
    ODB_CLASS_PERF,
    ODB_CLASS_THERM,
    ODB_CLASS_FAN,
    ODB_CLASS_INSTMEM,
    ODB_CLASS_MOTION_ESTIMATION,
    ODB_CLASS_VIDEO_PROCESSOR,
    ODB_CLASS_GPIO,
    ODB_CLASS_VOLT,
    ODB_CLASS_I2C,
    ODB_CLASS_STEREO,
    ODB_CLASS_VGA,
    ODB_CLASS_RC,
    ODB_CLASS_GSYNC,
    ODB_CLASS_SOFTWARE,
    ODB_CLASS_CVE,
    ODB_CLASS_HDMI,
    ODB_CLASS_HDCP,
    ODB_CLASS_HDTV,
    ODB_CLASS_BSP,
    ODB_CLASS_CIPHER,
    ODB_CLASS_FUSE,
    ODB_CLASS_INTR,
    ODB_CLASS_PMU,
    ODB_CLASS_PPP,
    ODB_CLASS_DPAUX,
    ODB_CLASS_CE,

#ifdef AMODEL
    ODB_CLASS_AMODEL,
#endif

#ifdef RM_PROFILER
    ODB_CLASS_PROFILER
#endif // RM_PROFILER

} ODB_CLASS;



/* _NVRM_COPYRIGHT_BEGIN_
 *
 * Copyright 1993-2002 by NVIDIA Corporation.  All rights reserved.  All
 * information contained herein is proprietary and confidential to NVIDIA
 * Corporation.  Any use, reproduction, or disclosure without the written
 * permission of NVIDIA Corporation is prohibited.
 *
 * _NVRM_COPYRIGHT_END_
 */

#ifndef _RMRETVAL_H_
#define _RMRETVAL_H_

#include "nvtypes.h"

/*
 * ---------------------------------------------------------------------------
 *
 * Error codes.
 *
 * ---------------------------------------------------------------------------
 */

typedef NvU32 RM_STATUS;

#define RM_OK                           0x00000000
#define RM_ERROR                        0xFFFFFFFF

#define RM_ERR_CANT_CREATE_CLASS_OBJS   0x00000001
#define RM_ERR_DMA_IN_USE               0x00000002
#define RM_ERR_DMA_MEM_NOT_LOCKED       0x00000003
#define RM_ERR_DMA_MEM_NOT_UNLOCKED     0x00000004
#define RM_ERR_DUAL_LINK_INUSE          0x00000005
#define RM_ERR_FIFO_BAD_ACCESS          0x00000006
#define RM_ERR_GPU_NOT_FULL_POWER       0x00000007
#define RM_ERR_ILLEGAL_ACTION           0x00000008
#define RM_ERR_ILLEGAL_OBJECT           0x00000009
#define RM_ERR_INSERT_DUPLICATE_NAME    0x0000000A
#define RM_ERR_INSUFFICIENT_RESOURCES   0x0000000B
#define RM_ERR_INVALID_ADDRESS          0x0000000C
#define RM_ERR_INVALID_ARGUMENT         0x0000000D
#define RM_ERR_INVALID_BASE             0x0000000E
#define RM_ERR_INVALID_CHANNEL          0x0000000F
#define RM_ERR_INVALID_CLASS            0x00000010
#define RM_ERR_INVALID_CLIENT           0x00000011
#define RM_ERR_INVALID_COMMAND          0x00000012
#define RM_ERR_INVALID_DATA             0x00000013
#define RM_ERR_INVALID_DEVICE           0x00000014
#define RM_ERR_INVALID_DMA_SPECIFIER    0x00000015
#define RM_ERR_INVALID_EVENT            0x00000016
#define RM_ERR_INVALID_FLAGS            0x00000017
#define RM_ERR_INVALID_FUNCTION         0x00000018
#define RM_ERR_INVALID_HEAP             0x00000019
#define RM_ERR_INVALID_INDEX            0x0000001A
#define RM_ERR_INVALID_LIMIT            0x0000001B
#define RM_ERR_INVALID_METHOD           0x0000001C
#define RM_ERR_INVALID_OBJECT           0x0000001D
#define RM_ERR_INVALID_OBJECT_BUFFER    0x0000001E
#define RM_ERR_INVALID_OBJECT_ERROR     0x0000001F
#define RM_ERR_INVALID_OBJECT_HANDLE    0x00000020
#define RM_ERR_INVALID_OBJECT_OLD       0x00000021
#define RM_ERR_INVALID_OBJECT_PARENT    0x00000022
#define RM_ERR_INVALID_OFFSET           0x00000023
#define RM_ERR_INVALID_OWNER            0x00000024
#define RM_ERR_INVALID_PARAM_STRUCT     0x00000025
#define RM_ERR_INVALID_POINTER          0x00000026
#define RM_ERR_INVALID_READ             0x00000027
#define RM_ERR_INVALID_STATE            0x00000028
#define RM_ERR_INVALID_WRITE            0x00000029
#define RM_ERR_INVALID_XLATE            0x0000002A
#define RM_ERR_IRQ_NOT_FIRING           0x0000002B
#define RM_ERR_MULTIPLE_MEMORY_TYPES    0x0000002C
#define RM_ERR_NO_FREE_FIFOS            0x0000002D
#define RM_ERR_NO_FREE_MEM              0x0000002E
#define RM_ERR_NOT_SUPPORTED            0x0000002F
#define RM_ERR_OBJECT_NOT_FOUND         0x00000030
#define RM_ERR_OBJECT_TYPE_MISMATCH     0x00000031
#define RM_ERR_OPERATING_SYSTEM         0x00000032
#define RM_ERR_OTHER_DEVICE_FOUND       0x00000033
#define RM_ERR_CALLBACK_NOT_SCHEDULED   0x00000034
#define RM_ERR_PAGE_TABLE_NOT_AVAIL     0x00000035
#define RM_ERR_PROTECTION_FAULT         0x00000036
#define RM_ERR_STATE_IN_USE             0x00000037
#define RM_ERR_TIMEOUT                  0x00000038
#define RM_ERR_BUFFER_TOO_SMALL         0x00000039
#define RM_ERR_NO_SUCH_DOMAIN           0x0000003A

#define RM_WARN_NULL_OBJECT             0x00000100

#endif /* _RMRETVAL_H_ */


// How to design an object database that store objects.
</pre>


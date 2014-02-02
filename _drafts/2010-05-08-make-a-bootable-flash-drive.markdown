http://www.gamebeat.net/forum/showthread.php?t=5&highlight=bootable+flash+disk

Need to flash your BIOS but don't have a floppy drive handy? Don't waste a blank CD/DVD on attempts to make a bootable MS-DOS DVD, use my method instead!


----------------------------------


HOW TO: Create a bootable MS-DOS USB key



This post explains how to:

Create a bootable (MS-DOS) USB key 
Copy necessary flashing files to the USB key 
Boot to the USB key 


You will need:
Access to a PC with Installed operating system: Windows 2000, Windows XP (32-bit or 64-bit), Windows 2003 (32-bit or 64-bit), or Windows Vista (32-bit or 64-bit) 
A USB storage device of some kind. Common examples are: USB thumb drive, USB MP3 Player, USB memory card reader w/ memory card, etc 
HP USB Drive Key Software[CLICK TO DOWNLOAD] 
DOS Boot Disk Files [CLICK TO DOWNLOAD] 

NOTE: The files above are hosted on my personal server, and are meant for the [H]ardForums & BadassGeeks only.




Making a bootable DOS USB Key

1. Extract and then install the HP USB Drive Key program you downloaded earlier. 

2. Extract the DOS boot files somewhere, anywhere. Just remember where you extracted them. For the purposes of this howto let's say we extracted them to C:\bootme\

3. Now you need to run the HP Drive Key program by clicking the icon in your Start -> Programs menu. VISTA USERS: You need to start the HP Drive Key Program as an administrator by RIGHT CLICKING the icon and selecting "Run as Administrator" from the context menu.




4. Insert a USB storage device of your choosing and wait for it to be recognized by Windows and the HP Drive Key utility. (once recognized it will appear in the first pulldown menu). For our howto I'm using my favorite busted-ass solid state 256MB MP3 player, but it could be anything with any memory size really. Just remember that anything currently on the USB drive will be sent to data heaven, so make sure to copy anything you don't want to lose from it before continuing. Here is the old and busted MP3 player I'm using as my USB key:




5. Choose FAT as the filesystem. Set the volume label to anything you want, doesn't matter. Under "Format Options" check the box next to "Quick Format" and "Create a DOS startup disk" . Choose the button next to "Using DOS system files located at:" and click the little browse button "..." next to the blank and navigate to C:\bootme (or wherever you extracted the DOS boot files earlier). Click OK.

Now click "Start" and the HP Drive Key utility will turn your USB device into a bootable DOS disk! (It will popup a window asking you to confirm!)





So let's check out what's on our USB drive now:


Well now, what you have here is a bootable USB drive with the few basic files needed to start a basic DOS session. When selected as a boot device this baby will boot your PC to a classic DOS prompt perfect for flashing that motherboard BIOS, updating firmware on your CD/DVD drive, or even flashing your video card BIOS!

So later in this howto I want to flash my motherboard's BIOS and I have the files I need already downloaded. I just drag them from my download location to the USB flash drive (in my case drive G: ).




Booting to DOS with your new bootable USB key

OK so let's get going:

1. Insert your bootable USB key and reboot your machine. With any luck (ie the correct BIOS settings) after the POST screen you will see your DOS prompt:



If you don't see a DOS prompt and instead your PC boots directly to Windows again, you may need to enter your motherboard's boot device selection menu. Most AWARD and AMI BIOS for current motherboards have an on-the-fly boot selection menu that you can get to via hotkey at the POST screen. For most AWARD BIOS based systems you press the ESC key at the POST screen. For most AMI (American Megatrends) BIOS based systems it's another hotkey like F8 or F11. On my motherboard the magic hotkey is F11, so let's try that.

Here's my POST screen - quick press F11!


Pressing F11:


Well lookie there, a nice menu to select my boot device. Cool eh? 95% of people don't even know they can actually do this. 


So I make sure the USB key is highlighted in the menu and press enter, and I get:



But on the rare odd motherboard, there is no on-the-fly boot menu. Instead you must enter the BIOS and look for a setting that controls boot order. Here's an example of those settings on my motherboard - see how the USB device is set first?




OK so by now you've booted to your DOS formatted USB key and have a nice basic DOS prompt waiting for your input:






AN EXAMPLE: Using your bootable USB key to flash (update) your motherboard's BIOS

So what can you do with your new bootable USB key? Well you now have a handy way to flash your motherboard's BIOS without having to install and use one of those 'ancient' floppy drives. A USB memory key is a hell of a lot more reliable than a floppy diskette anyway.

So as an example let's flash the BIOS on my motherboard, an MSI P6N SLI Platinum. Please keep in mind that the routine and utilities for BIOS flashing will vary by motherboard manufacturer. In my case we are using a recent version of the AMI BIOS flash utility (AFUD408.EXE) and the latest beta BIOS for my P6N SLI Platinum. Those of you with award BIOS will need the Award BIOS flash utility (usually AWDFLASH.EXE) and of course the updated BIOS binary file for your motherboard. 

YOU MUST OBTAIN THE APPROPRIATE BIOS UPDATE FILE AND UTILITY FOR YOUR MOTHERBOARD - WHAT YOU SEE BELOW IS AN EXAMPLE PROCEDURE ONLY

Oh did I mention that if you flash the wrong BIOS you could render your motherboard inoperable? Yup, it's about time for a bold print WARNING, so listen up:


WARNING
Flashing your BIOS can be DANGEROUS! If you don't know what you are doing you can render your PC useless, ♥♥♥♥ up your neighbors cable reception, cause your wife to start her period early, let the dogs out, or cause a rip in the space-time continuum. I cannot and will not be held responsible if you break your ♥♥♥♥. Understand? Comprende? Capiche? 


At this point you should have made your USB drive bootable, figured out how to boot to it, and copied the files you need to update your BIOS. On with my example...

So let's boot to our DOS bootable USB key again:




So let's refresh our memory, whats on this disc again? Type "DIR" and press enter to get a list of files on the drive:



Oh yeah that's right. So here you see:

AFUD408.EXE - The BIOS update utility for my motherboard
A7350NMS.134 - The actual BIOS update file for my motherboard. In your case this might end in .BIN or .ROM. In my case it ends in 134 because it's BIOS version 1.34 and.... well.... that's how MSI named the file.

So now I'm going to update the BIOS on my motherboard using the commands specific to the flash utility I'm using. My command:

AFUD408.EXE A7350NMS.134 /P /B /C

Starts the AMI BIOS Update utility and tells it to program the BIOS on my board with the data in the file A7350NMS.134, and afterwards to clear the CMOS settings. (I'll have to re-enter them when I reboot after the BIOS update). Here is an example of how a sucessful BIOS update might look:



So now all that's left to do is reboot and re-enter all my BIOS settings. You'll have to do that on your own since that's a little out os the scope of this howto, and plus I'm tired of typing. 


Feel free to ask questions, make comments, etc. I'll do my best to answer anything I can. 






http://www.gamebeat.net/forum/showthread.php?t=1057

<a href='http://www.tomhuang.com/wp-content/uploads/sp27608.zip' title='HP utility'>HP utility</a>
<a href='http://www.tomhuang.com/wp-content/uploads/bootme.zip' title='DOS'>DOS</a>

---
layout: post2
title:  "Customize Windows 10 Installation Image with DISM"
date:   2016-10-03 09:40:00
tags: windows deployment it
---

Recently I need to install dozens of Windows 10 machines. I don't want to install Windows, drivers, applications, and change settings for every machine, so I need to figure out how to customize the standard Windows installation image so that I can setup a machine in one single step. Fortunately, Microsoft has prepared a useful tool, **Deployment Image Servicing and Management (DISM.exe)**, for exactly this purpose. Here is the complete process of how to make your own Windows 10 installation image.

1. **Install Windows 10**. At the first OOBE screen, press **`Ctrl+Shift+F3`** to reboot into **System Audit Mode**.
2. **Install drivers and programs**. d:Remember don't reboot the machine while installing drivers and programs. We need to keep the machine in System Audit Mode.
3. **Reboot with System Preparing Tool**. After everything is setup, check **Generalize** and select **Enter System Out-of-Box Experience (OOBE)** in the System Preparing Tool, and reboot into the installation media (such as a USB drive) that you used to install Windows in the first step.

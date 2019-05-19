# Blenduino User Guide

## Overview

Blenduino is an almost-plug-and-play solution for connection an Arduino (or other microcontroller!) to Blender, via Serial. This guide assumes that you are vaguely familiar with Ardunio Serial communication and comfortable with Blender (knowing what a [Driver](https://docs.blender.org/manual/en/dev/animation/drivers/index.html) is will help).

---

## Setting up Python
Blender runs its own installation of python so there's a tiny amount of frontloading to get the Serial library to play nice. [This guide](http://www.codeplastic.com/2019/03/12/how-to-install-python-modules-in-blender/) walks through how to install modules in Blender's python. The only change you need to make is in step 3 install '**pyserial**' instead of '**scikit-image**'

---

## Installing the Blender Addon
Once you have installed python Serial as shown above, follow these steps to set up the Blenduino add on:

### Download
Clone or download this repo, and take note of where it is located.

### User Preferences
Open up Blender, and go to File > User Preferences

![File Menu](img/001-file.JPG?raw=true "File")

![File - User Prefs](img/002-file-menu.JPG?raw=true "User Prefs")

In the **Add-ons** tab, click **Install Add-on from File**

![Add-ons](img/003-install.JPG?raw=true "Add-ons")

Point the file explorer to the Blenduino repo. Select the **blenduino.py** file from **Blendiuno/blender/addon/** and hit **Install Add-on from File**.

![Add-on Path](img/004-install-file.JPG?raw=true "Add-on Path")

Back in the **Add-on** tab, select **Testing** under Supported Level, and **User** under Categories. Then check the box next to **Tool: Blenduino** to activate the Add-on. Don't forget to **Save User Settings**.

![Add-on Settings](img/005-install-testing.JPG?raw=true "Add-on Settings")

Still in **User Preferences**, navigate to the **File** tab, and make sure **Auto Run Python Scripts** is checked. This ensures that we are able to customise our drivers later on. Don't forget to **Save User Settings**.

![Auto Run](img/005-auto-execute.JPG?raw=true "Auto Run")

## Serial Tab

Now you can exit User Preferences. There should be a new tab in your Tool Shelf called **Serial**.

![Serial Tab](img/006-serial-tab.JPG?raw=true "Serial Tab")

The Serial tab exposes all the options you need to open a Serial port and listen for incoming data from an Arduino. For more on the settings, see [definitions](definitions.md).

![Serial Setting](img/007-settings.JPG?raw=true "Serial Settings")

1. **Serial Port**: The easiest way to find this is to use the Arduino IDE.
2. **Baud Rate**: This should match the baud rate of whatever sketch you are running (default 9600).
3. **Separator**: A character to specify the separation of incoming values. In all the examples the separator character is ','
4. **Expected Length**: How many [*Separator*] separated values are you expecting to receive?
5. **Start Serial**: Toggle the Serial port on and off. Will throw an error if the wrong port is specified. Rememeber to **Stop Serial** if you want to upload new code to your board.
6. **Toggle Serial Debugging**: Toggle whether to log incoming data on Blender's System Console.
7. **Data to Write**: This is the data that will send out via Serial. Add a driver here to control what is sent. 

Once you have entered your settings, click Start Serial to open the Serial Port and start listening for data. To check what you are receiving, go to **Window > Toggle System Console**.

![Toggle System Console](img/008-console.JPG?raw=true "Toggle System Console")

You should see the data streaming past akin to the Arduino Serial Monitor. Note: closing the System Console closes Blender, so click away or toggle it off using the Window menu.

![System Console](img/009-serial-console.JPG?raw=true "System Console")

---

## Using Blenduino

### Arduino to Blender

*bpy.context.scene.serial_data[index]*

Blenduino exposes incoming Serial data to Blender's scene context using **serial_data[i]**. If this doesn't make sense to you, watch this video below. The video explains how to access incoming Serial data and use that data to influence your scene.

[How to set up drivers with Blenduino](https://youtu.be/yBkZgEqRoPI).

Within the Ardunio directory of this repo is a demo of how to send data from an Arduino to Blender, called **Simple_Write_Test**

### Blender to Arduino

*bpy.context.scene.serial_write_data*

Similarly to above, the data in the scene context at **serial_write_data** is what is written out to Serial. 

The data can be accessed via the Serial tool panel, under the line item **Data to Write**. Add a driver here to control this data. Note that the data sent is an **integer**. All floats will be floored.

Within the Ardunio directory of this repo is a demo of how to read the data from Blender, called **Simple_Read_Test**

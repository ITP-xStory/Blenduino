# Blenduino User Guide

## Overview

Blenduino is an almost-plug-and-play solution for connection you Arduino (or other microcontroller!) to Blender, via Serial. This guide assumes that you are vaguely familiar with Ardunio serial communication and comfortable with Blender (knowing what "Driver" and "Driven" mean will help).

## Installation

1. Download this repo. 
2. Open Blender. Under **File > User Preferences > Add-ons** click "**Install Add-on from File...**" 
3. Navigate to the repo you downloaded earlier. Select **blender > addon > blenduino.py**
4. Once the addon is installed, you must activate it. In the left of the User Prefs window there is a panel called "**Supported Level**". Select "**Testing**" and click the checkbox next to "**Tool: Serial Communication**"

Once the addon is activated, there should be a new tab in the tool shelf labelled "**Serial**". This tab is where you set up and activate your serial connection. See **Definitions** (below) for info on each item in the tool shelf.

---

## Usage

### Blender to Arduino

*More detailed information (and possibly a video walkthrough!) coming soon*

*bpy.context.scene.serial_write_data*

At the moment the only data you can send to Arduino is within the 'Scene' data block, called **serial_write_data**. It is an int. The data can be accessed via the Blenduino tool panel, under the line item "**Data to Write**"

Within the Ardunio directory of this repo is a demo of how to read the data from Blender, called **Simple_Read_Test**

### Arduino to Blender

*bpy.context.scene.serial_data[index]*

The data from the Serial stream can be accessed through the active 'Scene' data block in Blender, using the variable **serial_data[** *idx* **]**. For example, to connect an object's z rotation to the first data point coming in via Serial, set up a driver/driven relationship like so:

1. With your object selected, open the properties panel ('*N*') 
2. Right click on the **Z Rotation** value
2. Right click on the **Z Rotation** value
3. **Add Drivers > Single From Target**. Then left click on the Z Rotation. It should become highlighted.
4. Pull open a new Editor Window, and navigate to the Graph Editor.
5. In the menu options, change the mode from **F-Curve** to **Drivers**.
6. Select the Z Euler Rotation on the left, open up the driver properties panel ('*N*), and select the "**Drivers**" tab.
7. Make sure "Type" is scripted expression, and the drop down menu next to 'var' says "**Single Property**"
8. Click on the drop down menu next to "**Prop**"" and change the "ID Type" to "**Scene**".
9. In the "**Prop**" text menu type the name of your scene (you should be prompted)
10. *FINALLY* in "**Path**", type serial_data[0]. This will connect the first element of the serial data to the z rotation of your object.

---

## Definitions

### Serial Port
The port your Arduino is connecting to. You can find this in the Arduino IDE under the "**Tools**" drop-down menu

### Baud Rate
Make sure this matches the setting on your Arduino. **Note** the Arduino IDE default is 9600, but Blenduino's default is 115200

### Data Separator
Blenduino expects a string of ints, separated by a character. The default character is a comma.

### Expected Length
The number of data points you are sending from the Arduino. The default is 8, max is 32

### Start Serial
Toggles the Serial connection. 

### Serial Debugging
Toggle printing incoming serial data to the python console


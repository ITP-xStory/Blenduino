# Contributing to Blenduino
Do you have thoughts on how to more usefully implement python threading? Can you think of a feature that you'd want to use? Do you think the serial stream could be more efficiently handled? By all means, feel free to contribute! 

## Submission Steps
To help me keep track of stuff, please submit an issue before submitting a pull request. In your pull request, tag the issue that you are referencing!

## Code Overview
I have tried to structure the code so that it is understandable through comments. Here is an overview of the current functions:

### register() and unregister()
Blender API function to start and stop addon

### initSerialProperties()
Creates variables within the context of Blender. This allows other data blocks in Blender to access the variables within this code

### CreateSerialPanel()
Uses the Blender API to create a UI panel in the tool shelf, and renders the buttons for Blenduino

### ToggleSerial()
Keeps track of threads created to read the Serial stream. Creates requests to kill threads if more than one is detected

### SerialDataThread()
Creates a new thread to read the Serial stream. Current implementation also parses data and writes it to Blender variables in the scene context.

### DebugSerial()
Toggles a serial monitor in the python console

## Helpful Resources
- [Python 3.6.4 documentation](https://www.python.org/downloads/release/python-364/)
- [Blender Python API docs](https://docs.blender.org/api/current/)
- [Arduino Serial docs](https://www.arduino.cc/reference/en/language/functions/communication/serial/)
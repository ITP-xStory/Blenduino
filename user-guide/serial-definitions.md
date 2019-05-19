# Serial Definitions

## Serial Port
The port your Arduino is connecting to. You can find this in the Arduino IDE under the "**Tools**" drop-down menu

## Baud Rate
Make sure this matches the setting on your Arduino. **Note** the Arduino IDE default is 9600, but Blenduino's default is 115200

## Data Separator
Blenduino expects a string of ints, separated by a character. The default character is a comma.

## Expected Length
The number of data points you are sending from the Arduino. The default is 8, max is 32

## Start Serial
Toggles the Serial connection. 

## Serial Debugging
Toggle printing incoming serial data to Blender's python console




/*
 * ORIGINAL: *
  String to Integer conversion

  Reads a serial input string until it sees a newline, then converts the string
  to a number if the characters are digits.

  The circuit:
  - No external components needed.

  created 29 Nov 2010
  by Tom Igoe

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/StringToInt

  * MODIFIED: *
  * 
  * reads an a number (as a string), converts to integer, and 
  * blinks and LED based on the number. 
  * 
  * Very rough code, expects a single int as a string, with a newline character at the end.
  * 
  * Modified Jan 2019
  * for Blenduino
  * by James Hosken
  
*/

String inString = "";    // string to hold input

bool ledState = false;      //Keep track of whether LED is on.
int blinkFrequency = 1000;  // Set default, but will change when serial data recieved
long checkpoint = 0;        

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(115200);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
}

void loop() {
  // Read serial input:

  handleSerial();

  // Use millis and checkpoints, not delay, 
  // to blink. Delay messes up serial.
  if(millis() - checkpoint > blinkFrequency){
    ledState = !ledState;
    digitalWrite(13, ledState);
    checkpoint = millis();
  }
  delay(10);
}

void handleSerial(){
  int val = -1;
  
  while (Serial.available() > 0) {
    int inChar = Serial.read();
    
    
    if (isDigit((char)inChar)) {
      // convert the incoming byte to a char and add it to the string:
      inString += (char)inChar;
    }
    
    // if you get a newline, save the string's value:
    if (inChar == '\n') {
      
      val = inString.toInt();    //parse to int
      inString = "";             //reset string
      Serial.print(val);
      Serial.print("; ");
      
      //Do something with the incoming data
      blinkFrequency = val;
      // clear the string for new input:
      inString = "";
    }
  }
  
  // This flush after is apparently important. Without it 
  // the LED blinker does not update. My best guess is that the arduino is 
  // waiting on some whitespace data or something.
  Serial.flush();
}

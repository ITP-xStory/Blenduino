/*
  A demonstration of Serial printing data 
  for use with Blenduino, an open-source 
  Add-on  for Blender to facilitate 
  communication with Arduino. 

  Blenduino Apr 2019
*/

void setup() {

  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  Serial.begin(9600);
}

void loop() {

  Serial.print(map(analogRead(A0), 0, 1024, 60,300));     //Print data
  Serial.print(",");                                      //Print separator
  Serial.print(map(analogRead(A1), 0, 1024, 60,300));     //Print data
  Serial.print(",");                                      //Print separator
  Serial.println(map(analogRead(A2), 0, 1024, 60,300));   //Print data and end line

  //Delay for a bit so as not to overload Serial
  delay(33);                                              
}

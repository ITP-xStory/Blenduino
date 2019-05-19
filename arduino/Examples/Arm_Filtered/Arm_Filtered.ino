/*
  A demonstration of Serial printing data 
  for use with Blenduino, an open-source 
  Add-on  for Blender to facilitate 
  communication with Arduino.  

  This version includes a small amount 
  of simple filtering to help prevent 
  erratic values.

  Blenduino Apr 2019
*/

void setup() {

  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  Serial.begin(9600);
}

void loop() {

  long cumulative0 = 0;
  long cumulative1 = 0;
  long cumulative2 = 0;

  for(int i = 0; i < 30; i++){
    cumulative0 += map(analogRead(A0), 0, 1024, 60,300);
    cumulative1 += map(analogRead(A1), 0, 1024, 60,300);
    cumulative2 += map(analogRead(A2), 0, 1024, 60,300);
    delay(1);
  }
  cumulative0 /= 30;
  cumulative1 /= 30;
  cumulative2 /= 30;
  
  Serial.print(cumulative0);
  Serial.print(",");
  Serial.print(cumulative1);
  Serial.print(",");
  Serial.println(cumulative2);
}

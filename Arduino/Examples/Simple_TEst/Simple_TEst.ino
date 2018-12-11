// James Hosken 2018
// Blenduino Test Sketch

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:

  for(int i = 0; i < 8; i++){
    Serial.print(random(0,1));
    Serial.print(",");
  }
  Serial.println();
}

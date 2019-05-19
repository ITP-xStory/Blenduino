/*
  A demonstration of Serial printing random 
  data for use with Blenduino, an 
  open-source Add-on  for Blender to 
  facilitate communication with Arduino. 

void setup() {
  Serial.begin(115200);
}

void loop() {

  for(int i = 0; i < 8; i++){
    Serial.print(random(0,1));
    if(i == 7){
    	break;				//Prevent trailing end commas
    }
    Serial.print(",");		//Print separator character
  }
  Serial.println();			//Print end line
}

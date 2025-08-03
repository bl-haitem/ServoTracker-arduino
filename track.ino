#include <Servo.h>

Servo myServo;

void setup() {
  myServo.attach(9); 
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    int angle = Serial.parseInt();      
    angle = constrain(angle, 0, 180);   
    myServo.write(angle);              
  }
}

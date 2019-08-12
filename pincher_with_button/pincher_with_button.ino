// This program is used to control pinching machine with a button, 
// With debouncer
#include <Servo.h>
#include <EasyButton.h>

const unsigned long debounceDelay = 50;
const int closeAngle = 50;
const int openAngle = 15;
const int buttonPin = 2;
const int switchPin = 3;
Servo myServo;

double expTime = 0;
unsigned long expEndTime = 0;
unsigned long expStartTime = 0;
double buttonPressedTime = 0;
double buttonReleasedTime = 0;
EasyButton button(buttonPin,50,true,true);
EasyButton switchExp(switchPin,200,true,true);

void setup() {
  expStartTime = 0;
  buttonPressedTime = 0;
  Serial.begin(9600);
  myServo.attach(9);  // servo connected to D9;
  button.begin();
  switchExp.begin();
}

void loop() {
  button.read();
  switchExp.read();
  
  // Switch
  if(switchExp.isPressed() == 0) {
    // Record the start time of experiment
    if(expStartTime == 0){
      Serial.println(0);
      expStartTime = millis();
    }
  }
  else{
    // record the end time of experiment
    if(expStartTime != 0){
      expEndTime = millis();
      expTime = (double)(expEndTime - expStartTime) / 1000;
      expStartTime = 0;
      Serial.println(1);
      Serial.println(expTime);
    }
  }
  
  // Button
  if(switchExp.isPressed() == 0){
    if(button.isPressed() == 0){
      // Record the time when button is pressed
      if(buttonPressedTime == 0){
        buttonPressedTime = (double)(millis() - expStartTime) / 1000; 
        Serial.println(2);
        Serial.println(buttonPressedTime); 
        
      }
      myServo.write(closeAngle);
    }
    else{
      if(buttonPressedTime != 0){
        buttonReleasedTime = (double)(millis() - expStartTime) / 1000; 
        buttonPressedTime = 0;
        Serial.println(3);
        Serial.println(buttonReleasedTime); 
      }
      myServo.write(openAngle);
    }// End if-else 
  } 
  // switch not pressed
  else  myServo.write(openAngle);

}

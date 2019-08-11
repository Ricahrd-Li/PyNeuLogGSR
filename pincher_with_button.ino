// This program is used to control pinching machine with a button, 
// With debouncer
#include <Servo.h>

unsigned long lastButtonDebounceTime = 0;
unsigned long lastSwitchDebounceTime = 0;
const unsigned long debounceDelay = 50;
const int servoAngle = 45;
const int buttonPin = 2;
const int switchPin = 3;

Servo myServo;
int buttonState = LOW;
int switchState = LOW;
int lastButtonState;
int lastSwitchState;

// For button
bool send1 = 0;
bool send0 = 1;
// For switch
bool send2 = 0;

void setup() {
  Serial.begin(9600);
  myServo.attach(9);  // servo connected to D9;
  pinMode(buttonPin,INPUT);  // Read this level to decide whether button is pressed or not  
  pinMode(switchPin,INPUT);
}

void loop() {
  // debounce
  // button
  int readButtonState = digitalRead(buttonPin);
  // if state change, update lastDebounceTime
  if(readButtonState != lastButtonState)  lastButtonDebounceTime = millis();
  if((millis() - lastButtonDebounceTime) > debounceDelay){
    buttonState = readButtonState;
  }
  // switch
  int readSwitchState = digitalRead(switchPin);
  // if state change, update lastDebounceTime
  if(readSwitchState != lastSwitchState)  lastSwitchDebounceTime = millis();
  if((millis() - lastSwitchDebounceTime) > debounceDelay){
    switchState = readSwitchState;
  }

  // after debounce
  // Button
  if(buttonState == HIGH){
    if(send1 == 0){
      Serial.println(1);
      send1 = 1;
      send0 = 0;
    }
    // close angle : 45
     myServo.write(45);  
  }
  else{
    if(send0 == 0){
      Serial.println(0);
      send0 = 1;
      send1 = 0;
    }
    // open angle: 10
    myServo.write(15);
  }      
  // Switch
  if(switchState == HIGH) {
    if(send2 == 0 ){
      Serial.println(2);
      send2 = 1;
    }
  }
  else send2 = 0;
  // update
  lastButtonState = readButtonState;
  lastSwitchState = readSwitchState;
}

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

// experiment time
double expTime = 0;
unsigned long expEndTime = 0;
unsigned long expStartTime = 0;

// pinch time
unsigned long currentTime = 0; 
unsigned long initialTime = 0;
unsigned long pinchStartTime = 0;

bool buttonPressed = false;
bool pinchStarted = false;
int randomTime = 4; 
unsigned long pinchTime = 2500; // pinch for 2.5 second

EasyButton button(buttonPin,50,true,false);
EasyButton switchExp(switchPin,1000,true,false);

void setup() {
  expStartTime = 0;
  initialTime = 0;

  Serial.begin(9600);
  myServo.attach(9);  // servo connected to D9;
  button.begin();
  switchExp.begin();
  randomTime = (( millis() % 6 )+ 4) *1000;
}

void loop() {
  button.read();
  switchExp.read();

  // Switch
  if(switchExp.isPressed()) {
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
  if(switchExp.isPressed()){
    // When you press the button, the random pinch mode starts!
    if(button.isPressed()){ 
      buttonPressed = true;
      Serial.println("button press");
      // Record button pressed time as initialTime
      initialTime = millis(); 
    }

    // if in the random pinch mode
    if(buttonPressed){
      currentTime = millis();
      if ((currentTime - initialTime)>= randomTime && pinchStarted == false){ // give a pinch
        myServo.write(closeAngle);
        Serial.println("2");
        Serial.println( (double)(currentTime - expStartTime) / 1000.0 );
        pinchStartTime = currentTime; 
        randomTime = (( millis() % 6 )+ 4) *1000;
        pinchStarted = true;
      }

      if(pinchStarted){
        if ((currentTime - pinchStartTime) > pinchTime){
          myServo.write(openAngle);
          Serial.println("3");
          Serial.println( (double)(currentTime - expStartTime) / 1000.0 );
          initialTime = currentTime;
          pinchStarted = false;
        }
      }
    }
  }
  else{ 
    myServo.write(openAngle);
    buttonPressed = false;
  }
}

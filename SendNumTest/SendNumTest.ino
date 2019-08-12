int number;

void setup() {
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  number = (( millis() % 6 )+ 4) *1000;
  Serial.println(number);
  delay(500);
}

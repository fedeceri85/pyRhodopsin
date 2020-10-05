/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the Uno and
  Leonardo, it is attached to digital pin 13. If you're unsure what
  pin the on-board LED is connected to on your Arduino model, check
  the documentation at http://www.arduino.cc

  This example code is in the public domain.

  modified 8 May 2014
  by Scott Fitzgerald
 */
String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 13 as an output.
    Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
  
  pinMode(13, OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(3,OUTPUT);
  digitalWrite(3,HIGH);
  digitalWrite(7,HIGH);
}
int isi = 900; //ISI in ms
int duration = 2;
int turnon = 0;
// the loop function runs over and over again forever
void loop() {
  
  if (turnon ==2){
  digitalWrite(7, LOW);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(3, LOW);
  delay(duration);              // wait for a second
  digitalWrite(7, HIGH);    // turn the LED off by making the voltage LOW
  digitalWrite(3, HIGH);
  delay(isi-duration);              // wait for a second
  }
  if (turnon==1){
     digitalWrite(7, LOW);   // turn the LED on (HIGH is the voltage level)
  }

 if (turnon==0){
     digitalWrite(7, HIGH);   // turn the LED on (HIGH is the voltage level)
  }

  
  // print the string when a newline arrives:
  if (stringComplete) {
    Serial.println(isi);
    Serial.println(duration);
    Serial.println(turnon);
    stringComplete = false;
  }
  
}



void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    int p1= Serial.parseInt();
    int p2= Serial.parseInt();
    int p3= Serial.parseInt();
    
    if (Serial.read() == '\n') {
      isi = p1;
      duration = p2;
      turnon = p3;
      stringComplete = true;
    }
  }
}

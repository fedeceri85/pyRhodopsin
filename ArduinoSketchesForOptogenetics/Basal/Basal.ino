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


// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 13 as an output.
  pinMode(7, OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(2,INPUT);
  pinMode(50,INPUT);

}
int isi = 1000; //ISI in ms
int duration = 2;

// the loop function runs over and over again forever
void loop() {
  if (digitalRead(2)==HIGH){
    if (digitalRead(50)==LOW){
        digitalWrite(7, LOW);   // turn the LED on (HIGH is the voltage level)
        digitalWrite(3, LOW);   // turn the LED on (HIGH is the voltage level)
      
        delay(duration);              // wait for a second
        digitalWrite(7, HIGH);    // turn the LED off by making the voltage LOW
        digitalWrite(3, HIGH);   // turn the LED on (HIGH is the voltage level)
      
        delay(isi-duration);              // wait for a second
    }
    else {
       digitalWrite(7, LOW);
     digitalWrite(3, LOW);
    }
  }
  else{
     digitalWrite(7, HIGH);
     digitalWrite(3, HIGH);

  }

}

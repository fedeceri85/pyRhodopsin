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
 
#include <Wire.h>


String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 13 as an output.
    Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
  
  pinMode(13, OUTPUT);
  pinMode(13,OUTPUT);
  pinMode(3,OUTPUT);
  digitalWrite(3,HIGH);
  digitalWrite(13,HIGH);
  Wire.begin(); // join i2c bus (address optional for master)
}
int isi = 1000; //ISI in ms
int duration = 5;
int turnon = 2;
int interBurstInterval = 900;
int nSpikes = 0;
int potValue = 51;
byte previousPotValue = 63-52;
bool changePot = false;
bool ramp = false;
bool pretrigger = true;
int potValuePretrigger = 63-8;
int pretriggerDuration = 40;
unsigned long t1;
unsigned long t2;
unsigned long t3;
unsigned long t4;
unsigned long t5;
unsigned long t6;
float timeResolution = 1;
float doublenSteps;
long nSteps;
// the loop function runs over and over again forever
void loop() {
  
  if (turnon ==2){

    if (nSpikes == 0){
          t3=micros();
          if (changePot && !ramp && !pretrigger){
                Wire.beginTransmission(44); // transmit to device #44 (0x2c)
                // device address is specified in datasheet
                Wire.write(byte(0x00));            // sends instruction byte
                Wire.write(potValue);             // sends potentiometer value byte
                Wire.endTransmission();     // stop transmitting
          }

          digitalWrite(13, LOW);   // turn the LED on (HIGH is the voltage level)
          digitalWrite(3, LOW);

          if (ramp){

            doublenSteps = duration/timeResolution;
            nSteps= (long)doublenSteps;
            for (long j=1;j<=nSteps;j++){
                t1 = micros();
                float newValue = 63-(63-potValue)*j/nSteps;
                int inewValue;
                inewValue = (int)newValue;
                Wire.beginTransmission(44); // transmit to device #44 (0x2c)
                // device address is specified in datasheet
                Wire.write(byte(0x00));            // sends instruction byte
                Wire.write((char)inewValue);             // sends potentiometer value byte
                Wire.endTransmission();     // stop transmitting     
                t2 = micros();   
                if (t2-t1<timeResolution*1000){ 
                  delayMicroseconds((timeResolution*1000)-(t2-t1));
                }
            }
            
          }

          if (pretrigger){
            doublenSteps = pretriggerDuration/timeResolution;
            nSteps= (long)doublenSteps;
            for (long j=1;j<=nSteps;j++){
                t1 = micros();
                float newValue = 63-(63-potValuePretrigger)*j/nSteps;
                int inewValue;
                inewValue = (int)newValue;
                Wire.beginTransmission(44); // transmit to device #44 (0x2c)
                // device address is specified in datasheet
                Wire.write(byte(0x00));            // sends instruction byte
                Wire.write((char)potValuePretrigger);             // sends potentiometer value byte
                Wire.endTransmission();     // stop transmitting     
                t2 = micros();   
                if (t2-t1<timeResolution*1000){ 
                  delayMicroseconds((timeResolution*1000)-(t2-t1));
                }
            }
            Wire.beginTransmission(44); // transmit to device #44 (0x2c)
            // device address is specified in datasheet
            Wire.write(byte(0x00));            // sends instruction byte
            Wire.write(potValue);             // sends potentiometer value byte
            Wire.endTransmission();     // stop transmitting   
          }
          
          if (!ramp){
          delay(duration);              // wait for a second
          }

          digitalWrite(13, HIGH);    // turn the LED off by making the voltage LOW
          digitalWrite(3, HIGH);
          
          if (ramp || pretrigger){
                   Wire.beginTransmission(44); // transmit to device #44 (0x2c)
                // device address is specified in datasheet
                Wire.write(byte(0x00));            // sends instruction byte
                Wire.write(63);             // sends potentiometer value byte
                Wire.endTransmission();     // stop transmitting  
                
          }
          t4=micros();
          delay( (isi-(t4-t3)/1000));              // wait for a second for a random isi use: random(300)/300.0*
    }
    else{
        t5 = micros();
        for (int j=0;j<nSpikes;j++){
                t3 = micros();
                if (changePot && !ramp){
                    Wire.beginTransmission(44); // transmit to device #44 (0x2c)
                    // device address is specified in datasheet
                    Wire.write(byte(0x00));            // sends instruction byte
                    Wire.write(potValue);             // sends potentiometer value byte
                    Wire.endTransmission();     // stop transmitting
                }
                digitalWrite(13, LOW);   // turn the LED on (HIGH is the voltage level)
                digitalWrite(3, LOW);   // turn the LED on (HIGH is the voltage level)
            
                if (ramp){

                    doublenSteps = duration/timeResolution;
                    nSteps= (long)doublenSteps;
                    for (long j=1;j<=nSteps;j++){
                        t1 = micros();
                        float newValue = 63-(63-potValue)*j/nSteps;
                        int inewValue;
                        inewValue = (int)newValue;
                        Wire.beginTransmission(44); // transmit to device #44 (0x2c)
                        // device address is specified in datasheet
                        Wire.write(byte(0x00));            // sends instruction byte
                        Wire.write((char)inewValue);             // sends potentiometer value byte
                        Wire.endTransmission();     // stop transmitting     
                        t2 = micros();   
                        if (t2-t1<timeResolution*1000){ 
                          delayMicroseconds((timeResolution*1000)-(t2-t1));
                        }     
                  }
            
                }

                if (pretrigger){
                    doublenSteps = pretriggerDuration/timeResolution;
                    nSteps= (long)doublenSteps;
                    for (long j=1;j<=nSteps;j++){
                        t1 = micros();
                        float newValue = 63-(63-potValuePretrigger)*j/nSteps;
                        int inewValue;
                        inewValue = (int)newValue;
                        Wire.beginTransmission(44); // transmit to device #44 (0x2c)
                        // device address is specified in datasheet
                        Wire.write(byte(0x00));            // sends instruction byte
                        Wire.write((char)potValuePretrigger);             // sends potentiometer value byte
                        Wire.endTransmission();     // stop transmitting     
                        t2 = micros();   
                        if (t2-t1<timeResolution*1000){ 
                          delayMicroseconds((timeResolution*1000)-(t2-t1));
                        }
                    }
                    Wire.beginTransmission(44); // transmit to device #44 (0x2c)
                    // device address is specified in datasheet
                    Wire.write(byte(0x00));            // sends instruction byte
                    Wire.write(potValue);             // sends potentiometer value byte
                    Wire.endTransmission();     // stop transmitting   
                }
          
                if (!ramp){
                  delay(duration);              // wait for a second
                }
                digitalWrite(13, HIGH);    // turn the LED off by making the voltage LOW
                digitalWrite(3, HIGH);   // turn the LED on (HIGH is the voltage level)
              if (ramp || pretrigger){
                   Wire.beginTransmission(44); // transmit to device #44 (0x2c)
                // device address is specified in datasheet
                Wire.write(byte(0x00));            // sends instruction byte
                Wire.write(63);             // sends potentiometer value byte
                Wire.endTransmission();     // stop transmitting  
                
              }
                t4 = micros();
                delay(isi-(t4-t3)/1000);              // wait for a second
              }
              t6 = micros();
                 delay(interBurstInterval-(t6-t5)/1000);
      }
  }
  if (turnon==1){
      if (changePot){
            Wire.beginTransmission(44); // transmit to device #44 (0x2c)
            // device address is specified in datasheet
            Wire.write(byte(0x00));            // sends instruction byte
            Wire.write(potValue);             // sends potentiometer value byte
            Wire.endTransmission();     // stop transmitting
      }
     digitalWrite(13, LOW);   // turn the LED on (HIGH is the voltage level)
  }

 if (turnon==0){
      if (changePot){
          Wire.beginTransmission(44); // transmit to device #44 (0x2c)
          // device address is specified in datasheet
          Wire.write(byte(0x00));            // sends instruction byte
          Wire.write(potValue);             // sends potentiometer value byte
          Wire.endTransmission();     // stop transmitting

    }
     digitalWrite(13, HIGH);   // turn the LED on (HIGH is the voltage level)
  }

  

  
}



#include <Servo.h>
int pos;    // variable to store the servo position
int incomingByte;
int ang = 100;
Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards
void setup() {

  
  myservo.attach(5);  // attaches the servo on pin 5 to the servo object
  Serial.begin(9600);
 
}



void loop() {
  if (Serial.available() > 0){
   int in = Serial.read();
    if (in == 'l')
    {
      ang++;
      myservo.write(ang);
      
    }
  else if (in == 'r')
  {
       ang--;
      myservo.write(ang);
  }
  else if (in == 'c')
  {
   myservo.write(ang);
  }

  }


}

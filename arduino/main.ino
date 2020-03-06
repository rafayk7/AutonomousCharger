#include <SoftwareSerial.h>
#include "control.cpp"

RoverControl Controller;
int wheelSpeed = 255;

void setup()
{
    Serial.begin(9600);
    Controller.init(wheelSpeed); // Initialize with motor speeds
}

void loop()
{
    Controller.moveSidewaysRight();
    // if(Serial.available()){
    //     int inCommand = (int) Serial.read(); 
    //     // Logic to interpret serial commands
    //     switch (inCommand)
    //     {
    //     case 0:
    //         Controller.moveForward();
    //         break;
    //     case 1:
    //         Controller.moveBackward();
    //     case 2:
    //         Controller.moveSidewaysLeft();        
    //     case 3:
    //         Controller.moveSidewaysRight();
    //     default:
    //         break;
    //     }
    // }

}
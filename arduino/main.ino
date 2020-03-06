#include <SoftwareSerial.h>
#include "controllers/RoverController.cpp"
#include "controllers/ActuatorController.cpp"

RoverControl RoverController;
ActuatorControl ActuatorController;
int wheelSpeed = 255;
int actuatorSpeed = 700;

void setup()
{
    Serial.begin(9600);
    RoverController.init(wheelSpeed); // Initialize with motor speeds
    ActuatorController.init(actuatorSpeed); // Initialize with optimized actuator speed
}

void loop()
{
    ActuatorController.moveUp();
    if(Serial.available()){
        int inCommand = (int) Serial.read(); 
        // Logic to interpret serial commands
        // switch (inCommand)
        // {
        // case 0:
        //     RoverController.moveForward();
        //     break;
        // case 1:
        //     RoverController.moveBackward();
        //     break;
        // case 2:
        //     RoverController.moveSidewaysLeft();    
        //     break;
        // case 3:
        //     RoverController.moveSidewaysRight();
        //     break;
        // case 4:
        //     RoverController.rotateLeft();
        //     break;
        // case 5:
        //     RoverController.rotateRight();
        //     break;
        // case 6:
        //     ActuatorController.moveUp();
        //     break;
        // case 7:
        //     ActuatorController.moveDown();
        //     break;
        // case 8:
        //     RoverController.stopMotion();
        //     ActuatorController.stopMotion(); // Is there even need for this?
        //     break;
        // default:
        //     break;
        // }
    }

}
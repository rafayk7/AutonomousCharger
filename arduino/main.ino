#include <SoftwareSerial.h>
#include "controllers/RoverController.cpp"
#include "controllers/ActuatorController.cpp"

RoverControl RoverController;
ActuatorControl ActuatorController;
int wheelSpeed = 255;
int actuatorSpeed = 150;
int delay = 100;

void setup()
{
    Serial.begin(9600);
    RoverController.init(wheelSpeed); // Initialize with motor speeds
    ActuatorController.init(actuatorSpeed); // Initialize with optimized actuator speed
}

void loop()
{
    while(Serial.available() > 0){
        char data = (char) Serial.read(); //StringUntil('\n');
        // int inCommand = (int) data - '0';

        // Logic to interpret serial commands
        if(data == 's')
        {
            RoverController.moveForward();
            delay(delay);
            RoverController.stopMotion();
        }
        if(data == 'a')
        {
            RoverController.moveSidewaysLeft();
            delay(delay);
            RoverController.stopMotion();
        }
        if(data == 'd')
        {
            RoverController.moveSidewaysRight();
            delay(delay);
            RoverController.stopMotion();
        }
        if(data == 'w')
        {
            RoverController.moveBackward();
            delay(delay);
            RoverController.stopMotion();
        }
        if(data == 'e')
        {
            RoverController.rotateRight();
            delay(delay);
            RoverController.stopMotion();
        }
        if(data == 'q')
        {
            RoverController.rotateLeft();
            delay(delay);
            RoverController.stopMotion();
        }
        if(data=='p')
        {
            RoverController.stopMotion();
        }
        // if(inCommand == 5)
        // {
        //     RoverController.rotateRight();
        // }
        // if(inCommand == 6)
        // {
        //     RoverController.rotateLeft();
        // }
        // else if (inCommand == 7)
        // {
        //     RoverController.stopMotion();
        // }

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
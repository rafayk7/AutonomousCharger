#include <SoftwareSerial.h>
#include "control.cpp"

SoftwareSerial BTSerial(9, 10); // RX | TX
RoverControl Controller;
int wheelSpeed = 200;

void setup()
{
    Serial.begin(9600);
    BTSerial.begin(38400);
    Controller.init(wheelSpeed); // Initialize with motor speeds
}

void loop()
{
    if(BTSerial.available()){
        // int inCommand = (int)Serial.read(); 
        Serial.write(BTSerial.read());
        // Logic to interpret serial commands
        // switch (inCommand)
        // {
        // case 0:
        //     Controller.moveForward();
        //     break;
        // case 1:
        //     Controller.moveBackward();
        // case 2:
        //     Controller.moveSidewaysLeft();        
        // case 3:
        //     Controller.moveSidewaysRight();
        // default:
        //     break;
        // }
    }

}
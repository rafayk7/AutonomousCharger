#include "RoverControl.h"
#include <SoftwareSerial.h>

String inputString;
RoverControl Controller;

void setup()
{

}

void loop()
{
    if(Serial.available()){
        while(Serial.available()){ // Get the entire input string
            char inChar = (char)Serial.read(); 
            inputString += inChar;
        }

        // Logic to interpret command
        switch (inputStirng)
        {
        case "a":
            Controller.moveForward();
            break;
        default:
            break;
        } 

    }
    
}
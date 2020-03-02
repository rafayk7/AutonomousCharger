#include "RoverControl.h"
#include <SoftwareSerial.h>

String inputString;
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
        

    }
    
}
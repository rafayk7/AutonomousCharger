#include "Arduino.h"

class ActuatorControl
{
    private:
        int stepPin;
        int dirPin;
        int moveSpeed;
    public:
        void init(int speed)
        {
            // TODO : CHANGE THESE PINS
            stepPin = 2;
            dirPin = 3;
            moveSpeed = speed;

            pinMode(stepPin, OUTPUT);
            pinMode(dirPin, OUTPUT);
        }

        void moveUp()
        {
            digitalWrite(dirPin, HIGH);

            for(int x=0; x < 200; x++)
            {
                digitalWrite(stepPin,HIGH); 
                delayMicroseconds(moveSpeed); 
                digitalWrite(stepPin,LOW);
                delayMicroseconds(moveSpeed);
            }
            delay(1000);
        }

        void moveDown()
        {
            digitalWrite(dirPin, LOW);

            for(int x=0; x < 200; x++)
            {
                digitalWrite(stepPin,HIGH); 
                delayMicroseconds(moveSpeed); 
                digitalWrite(stepPin,LOW);
                delayMicroseconds(moveSpeed);
            }
            delay(1000);
        }

        void stopMotion()
        {
            // Do anything?
        }
};
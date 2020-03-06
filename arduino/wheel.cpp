#include <Arduino.h>

class Wheel{
    public: 
        int enablePin;
        int in1Pin;
        int in2Pin;
        int speed;

        void setPins(int en, int in1, int in2, int speed_val)
        {
            pinMode(en, OUTPUT);
            pinMode(in1, OUTPUT);
            pinMode(in2, OUTPUT);

            enablePin = en;
            in1Pin = in1;
            in2Pin = in2;
            speed = speed_val;

            analogWrite(enablePin, speed);
        }

        void forward()
        {
            digitalWrite(in1Pin, HIGH);
            digitalWrite(in2Pin, LOW);
        }

        void backward()
        {
            digitalWrite(in1Pin, LOW);
            digitalWrite(in2Pin, HIGH);
        }

        void stop()
        {
            digitalWrite(in1Pin, LOW);
            digitalWrite(in2Pin, LOW);
        }
};
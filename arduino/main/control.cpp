#include <Arduino.h>
#include "wheel.cpp"

class RoverControl
{
  private:
    int wheelSpeed;
    Wheel LeftBackWheel;
    Wheel LeftFrontWheel;
    Wheel RightBackWheel;
    Wheel RightFrontWheel;

  public:
    void init(int speed)
    {
      wheelSpeed = speed;
      LeftBackWheel.setPins(5, 6, 7, wheelSpeed);
      LeftFrontWheel.setPins(10, 9, 8, wheelSpeed);
      RightBackWheel.setPins(3, 4, 2, wheelSpeed);
      RightFrontWheel.setPins(11, 13, 12, wheelSpeed);
    }

    void moveForward()
    {
        LeftFrontWheel.forward();
        LeftBackWheel.forward();
        RightFrontWheel.forward();
        RightBackWheel.forward();
    }

    void moveBackward() {
        LeftFrontWheel.backward();
        LeftBackWheel.backward();
        RightFrontWheel.backward();
        RightBackWheel.backward();
    }

    void moveSidewaysRight() {
        LeftFrontWheel.forward();
        LeftBackWheel.backward();
        RightFrontWheel.backward();
        RightBackWheel.forward();
    }

    void moveSidewaysLeft() {
      LeftFrontWheel.backward();
      LeftBackWheel.forward();
      RightFrontWheel.forward();
      RightBackWheel.backward();
    }

    void rotateLeft() {
      LeftFrontWheel.backward();
      LeftBackWheel.backward();
      RightFrontWheel.forward();
      RightBackWheel.forward();
    }
    void rotateRight() {
      LeftFrontWheel.forward();
      LeftBackWheel.forward();
      RightFrontWheel.backward();
      RightBackWheel.backward();
    }
};

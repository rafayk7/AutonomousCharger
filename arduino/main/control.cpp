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
      LeftBackWheel.setPins(A0, 2, 6, wheelSpeed);
      LeftFrontWheel.setPins(A1, 3, 7, wheelSpeed);
      RightBackWheel.setPins(A2, 4, 8, wheelSpeed);
      RightFrontWheel.setPins(A3, 5, 9, wheelSpeed);
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

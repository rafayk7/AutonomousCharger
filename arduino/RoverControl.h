#include "wheel.h"

class RoverControl
{
  private:
    int wheelSpeed = 255;

    Wheel LeftBackWheel(A0, 2, 6, wheelSpeed);
    Wheel LeftFrontWheel(A1, 3, 7, wheelSpeed);
    Wheel RightBackWheel(A2, 4, 8, wheelSpeed); 
    Wheel RightFrontWheel(A3, 5, 9, wheelSpeed);
    
  public:
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
}

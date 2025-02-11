#!/bin/bash

echo "Compiling PWM library..."
gcc -shared -o libhardware_pwm.so -fPIC hardware_pwm.c -lwiringPi

echo "Build complete. Use libpwm.so in your Python scripts."


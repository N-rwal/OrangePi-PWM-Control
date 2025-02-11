# OrangePi-PWM-Control

A simple hardware PWM control system for Orange Pi using WiringOP and Python.

## Setup Instructions

1. **Clone the repository**

   git clone https://github.com/N-rwal/OrangePi-PWM-Control.git
   cd OrangePi-PWM-Control

2. **Install WiringOP (if not already installed)**

   sudo apt update
   
   sudo apt install wiringpi

4. **Build the C library**
   
   ./build.sh

6. **Run the Python script**
   
   python3 pwm_control.py

  **Custom Usage**

  Modify pwm_control.py to set different PWM pins, frequencies, or duty cycles.

# OrangePi-PWM-Control

![image](https://github.com/user-attachments/assets/899bb309-ae63-4afa-9cb2-504d2e628868)


A simple hardware PWM control system for Orange Pi zero 2W using WiringOP and Python.

## Setup Instructions

1. **Clone the repository**

   git clone https://github.com/N-rwal/OrangePi-PWM-Control.git
   cd OrangePi-PWM-Control

2. **Install WiringOP (if not already installed)**

   sudo apt update
   
   sudo apt install wiringpi

   **Test with:** gpio readall
   
![image](https://github.com/user-attachments/assets/7a4675dc-0164-4163-bae1-2ed8dad9e615)

4. **Build the C library**
   
   ./build.sh

6. **Run the Python script**
   
   python3 pwm_control.py

**The example script will generate a sweeping PWM signal up to 12% at 50 Hz on the wPi pin 21 which is the PMW1 pin.**
   
   Suitable for a servo.

   ![image](https://github.com/user-attachments/assets/84f6180e-bf62-4e32-9cb4-ba30f6fb8493)

  **Custom Usage**

  Modify pwm_control.py to set different PWM pins, frequencies, or duty cycles.

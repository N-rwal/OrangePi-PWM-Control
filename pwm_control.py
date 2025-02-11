import ctypes
import time

class HardwarePWM:
    def __init__(self, lib_path='./libpwm.so'):
        # Load the shared library
        self.lib = ctypes.CDLL(lib_path)

        # Define argument types
        self.lib.init_pwm.argtypes = [ctypes.c_int, ctypes.c_uint, ctypes.c_uint]
        self.lib.set_pwm_duty_cycle.argtypes = [ctypes.c_int, ctypes.c_uint]

    def init(self, pin, arr, div):
        self.lib.init_pwm(pin, arr, div)

    def set_duty_cycle(self, pin, duty_cycle):
        self.lib.set_pwm_duty_cycle(pin, duty_cycle)


# Example Usage
if __name__ == "__main__":
    PWM_PIN = 21  # Example PWM pin
    ARR_VALUE = 2048  # Example ARR value
    FREQUENCY_DIVISOR = 234  # for 50 Hz
    DUTY_CYCLE = 256  # Max duty cycle (12%)

    pwm = HardwarePWM()
    pwm.init(PWM_PIN, ARR_VALUE, FREQUENCY_DIVISOR)
    print(f"Initialized PWM on pin {PWM_PIN} with ARR={ARR_VALUE}, DIV={FREQUENCY_DIVISOR}")

    try:
        while True:
            # Gradually increase duty cycle
            for duty_cycle in range(0, DUTY_CYCLE, 5):
                pwm.set_duty_cycle(PWM_PIN, duty_cycle)
                time.sleep(0.1)  # Small delay to observe the change

            # Gradually decrease duty cycle
            for duty_cycle in range(DUTY_CYCLE, 0, -5):
                pwm.set_duty_cycle(PWM_PIN, duty_cycle)
                time.sleep(0.1)  # Small delay to observe the change

    except KeyboardInterrupt:
        print("\nExiting PWM control.")

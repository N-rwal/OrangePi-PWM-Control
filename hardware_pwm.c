#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    unsigned int ccr;
    unsigned int arr;
    unsigned int div;
} pwm_info;

static pwm_info pwm_info_t;

// Initialize PWM on a specific pin
void init_pwm(int pin, unsigned int arr, unsigned int div) {
    if (wiringPiSetup() == -1) {
        fprintf(stderr, "WiringPi setup failed!\n");
        return;
    }

    pwm_info_t.ccr = arr / 2;  // Default 50% duty cycle
    pwm_info_t.arr = arr;
    pwm_info_t.div = div;

    pinMode(pin, PWM_OUTPUT);
    pwmSetRange(pin, pwm_info_t.arr);
    pwmSetClock(pin, pwm_info_t.div);
    pwmWrite(pin, pwm_info_t.ccr);
}

// Set the duty cycle for a specific pin
void set_pwm_duty_cycle(int pin, unsigned int ccr) {
    if (ccr >= pwm_info_t.arr) {
        fprintf(stderr, "CCR must be less than ARR\n");
        return;
    }
    pwmWrite(pin, ccr);
}


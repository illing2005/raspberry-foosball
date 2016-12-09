#!/usr/bin/python
"""
Test script to constantly output the two PIN values
"""
import time
import RPi.GPIO as GPIO
from config import GPIO_PLAYER_ONE_PIN, GPIO_PLAYER_TWO_PIN


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

if __name__ == '__main__':
    # setup the two pins
    GPIO.setup(GPIO_PLAYER_ONE_PIN, GPIO.IN)
    GPIO.setup(GPIO_PLAYER_TWO_PIN, GPIO.IN)
    # loop to print the pin values
    while True:
        time.sleep(0.001)
        print GPIO.input(GPIO_PLAYER_ONE_PIN), GPIO.input(GPIO_PLAYER_TWO_PIN)

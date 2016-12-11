#!/usr/bin/python
import RPi.GPIO as GPIO
from pusher_client import PusherThread
from Queue import Queue
import logging
logging.basicConfig(level=logging.DEBUG)

from config import GPIO_PLAYER_TWO_PIN, GPIO_PLAYER_ONE_PIN
from goaldetector import GoalDetector


def main():
    # set GPIO mode
    GPIO.setmode(GPIO.BCM)
    # create message queue
    queue = Queue()
    # create goal detection instances
    GoalDetector(GPIO_PLAYER_ONE_PIN, 0, queue)
    GoalDetector(GPIO_PLAYER_TWO_PIN, 1, queue)
    # Pusher thread listens to events
    PusherThread(queue)

    logging.info('All threads started')
    while True:
        pass


if __name__ == '__main__':
   main()

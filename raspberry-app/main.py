#!/usr/bin/python
import RPi.GPIO as GPIO
import logging
import time
from blinker import signal

logging.basicConfig(level=logging.DEBUG)

from config import GPIO_PLAYER_TWO_PIN, GPIO_PLAYER_ONE_PIN
from goaldetector import GoalDetector
from pusher_client import PusherClient
from replay import Replay


SIGNALS = (
    'goal_scored',
    'replay_ready',
)


def main():
    # set GPIO mode
    GPIO.setmode(GPIO.BCM)

    # create signals
    signals = dict()
    for s in SIGNALS:
        signals[s] = signal(s)
        print signals[s].name

    # create goal detection instances
    GoalDetector(GPIO_PLAYER_ONE_PIN, 0, signals)
    GoalDetector(GPIO_PLAYER_TWO_PIN, 1, signals)

    # Pusher thread listens to events
    pusher_client = PusherClient(signals)

    # Start recording for replays
    replay = Replay(signals)

    logging.info('Main: Setup done')

    while True:
        pass


if __name__ == '__main__':
    main()

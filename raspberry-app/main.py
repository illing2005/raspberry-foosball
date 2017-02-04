#!/usr/bin/python
import RPi.GPIO as GPIO
import logging
import time
from blinker import signal

logging.basicConfig(level=logging.DEBUG)

import config
from goaldetector import GoalDetector
from pusher_client import PusherClient
from replay import Replay
from led_strip import LEDStrip

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
        logging.info('Main: Signal added: %s' % signals[s].name)

    # create goal detection instances
    GoalDetector(config.GPIO_PLAYER_ONE_PIN, 0, signals)
    GoalDetector(config.GPIO_PLAYER_TWO_PIN, 1, signals)

    # Pusher thread listens to events
    pusher_client = PusherClient(signals)

    if config.FEATURE_REPLAY:
        # Start recording for replays
        replay = Replay(signals)

    if config.FEATURE_RGB_LED:
        led = LEDStrip(signals)

    logging.info('Main: Setup done')

    while True:
        pass

if __name__ == '__main__':
    main()

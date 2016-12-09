#!/usr/bin/python
import time
import RPi.GPIO as GPIO
import pusher_client

from config import GPIO_PLAYER_TWO_PIN, GPIO_PLAYER_ONE_PIN

# set GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Player(object):
    def __init__(self, PIN, id):
        self.PIN = PIN
        self.id = id

    def check_for_goal(self):
        if GPIO.input(self.PIN) == GPIO.HIGH:
            print 'GOAL Player %s' % str(self.id+1)
            pusher_client.send_goal(self.id)
            time.sleep(2)  # wait 2s to ensure we don't count goals twice


def main():
    # initialize pins
    GPIO.setup(GPIO_PLAYER_ONE_PIN, GPIO.IN)
    GPIO.setup(GPIO_PLAYER_TWO_PIN, GPIO.IN)

    # initialize players
    player_one = Player(GPIO_PLAYER_ONE_PIN, 0)
    player_two = Player(GPIO_PLAYER_TWO_PIN, 1)

    while True:
        time.sleep(0.001)
        player_one.check_for_goal()
        player_two.check_for_goal()


if __name__ == '__main__':
   main()
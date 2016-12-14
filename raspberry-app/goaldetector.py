import RPi.GPIO as GPIO
import logging


class GoalDetector(object):
    """

    """
    def __init__(self, PIN, id, signals):
        self.PIN = PIN
        self.id = id
        self.signals = signals
        # initialize pin
        GPIO.setup(PIN, GPIO.IN)
        # use threaded event detection
        GPIO.add_event_detect(self.PIN, GPIO.RISING, callback=self.on_goal, bouncetime=5000)
        logging.info('GoalDetector: %s at pin %s initialized' % (id, PIN))

    def on_goal(self, channel):
        """
        Send a event to the queue.
        {type: 'goal_scored', 'player': id}
        """
        logging.info('GoalDetector: GOAL Player %s' % str(self.id))
        self.signals['goal_scored'].send({'type': 'goal_scored', 'player_id': self.id})
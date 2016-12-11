import RPi.GPIO as GPIO
import logging


class GoalDetector(object):
    """
    
    """
    def __init__(self, PIN, id, queue):
        self.PIN = PIN
        self.id = id
        self.queue = queue
        # initialize pin
        GPIO.setup(PIN, GPIO.IN)
        # use threaded event detection
        GPIO.add_event_detect(self.PIN, GPIO.RISING, callback=self.on_goal, bouncetime=1000)
        logging.info('GoalDetector %s at pin %s initialized' % (id, PIN))

    def on_goal(self, channel):
        """
        Send a event to the queue.
        {type: 'goal_scored', 'player': id}
        """
        logging.info('GOAL Player %s' % str(self.id + 1))
        self.queue.put({'type': 'goal_scored', 'player_id': self.id})
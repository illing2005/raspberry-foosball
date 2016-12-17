from config import RED_PIN, GREEN_PIN, BLUE_PIN, PLAYER_ONE_BLINK_COLOR, PLAYER_TWO_BLINK_COLOR
import logging
import pigpio
import time
import threading

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
OFF = (0, 0, 0)


class LEDStrip(object):
    """

    """
    def __init__(self, signals):

        self.signals = signals

        self.pi = pigpio.pi()
        # set white
        self.set_color(*WHITE)

        # connect to all signals we want to subscribe
        for name, signal in self.signals.iteritems():
            method = getattr(self, '%s_subscription' % name, None)
            if method:
                signal.connect(method)
                logging.info('LEDStrip: Connected to signal "%s"' % name)

    def goal_scored_subscription(self, data):
        """
        Start a thread to blink the led strip
        """
        if data['player_id'] == 0:
            color = PLAYER_ONE_BLINK_COLOR
        else:
            color = PLAYER_TWO_BLINK_COLOR
        t = threading.Thread(target=self.blink, args=[color])
        t.start()

    def set_color(self, r, g, b):
        self.pi.set_PWM_dutycycle(RED_PIN, r)
        self.pi.set_PWM_dutycycle(GREEN_PIN, g)
        self.pi.set_PWM_dutycycle(BLUE_PIN, b)
        logging.info('LEDStrip: Set to (%s %s %s)' % (r, g, b))

    def blink(self, color, n=10):
        logging.info('LEDStrip: start blinking in %s' % str(color))
        for i in range(0, n):
            self.set_color(*color)
            time.sleep(0.1)
            self.set_color(*OFF)
            time.sleep(0.1)
        self.set_color(*WHITE)
import pusher
from config import PUSHER_APP_ID, PUSHER_SECRET_KEY, PUSHER_KEY
import logging


class PusherClient(object):
    """

    """

    def __init__(self, signals):
        # connect to pusher
        self.client = pusher.Pusher(
          app_id=PUSHER_APP_ID,
          key=PUSHER_KEY,
          secret=PUSHER_SECRET_KEY,
          cluster='eu',
          ssl=False
        )
        logging.info('Connected to Pusher')
        self.signals = signals

        # connect to all signals we want to subscribe
        for name, signal in self.signals.iteritems():
            method = getattr(self, '%s_subscription' % name, None)
            if method:
                signal.connect(method)
                logging.info('Pusher: Connected to signal "%s"' % name)

    def listen(self):
        """
        Listen for new events in queue
        If event detected and method exists call it.
        """
        while True:
            event = self.queue.get()
            if event:
                logging.info('Pusher: Event detected %s' % event)
                method = getattr(self, event.pop('type'))
                if method:
                    method(**event)

    def replay_ready_subscription(self, data):
        self.client.trigger(
            'kicker_channel',
            'replay_ready',
            {'player': 'test'}
        )
        logging.info('Pusher: Replay ready pushed')

    def goal_scored_subscription(self, data):
        """
        Push a goal to subscribers
        """
        self.client.trigger(
            'kicker_channel',
            'goal_scored',
            {'player': data['player_id']}
        )
        logging.info('Pusher: Goal for player %s pushed' % data['player_id'])

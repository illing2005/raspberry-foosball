import pusher
from config import PUSHER_APP_ID, PUSHER_SECRET_KEY, PUSHER_KEY
from threading import Thread
import logging


class PusherThread(object):
    """

    """
    def __init__(self, queue):
        # connect to pusher
        self.client = pusher.Pusher(
          app_id=PUSHER_APP_ID,
          key=PUSHER_KEY,
          secret=PUSHER_SECRET_KEY,
          cluster='eu',
          ssl=False
        )
        logging.info('Connected to Pusher')
        self.queue = queue
        self.thread = Thread(target=self.listen)
        self.thread.start()

    def listen(self):
        """
        Listen for new events in queue
        If event detected and method exists call it.
        """
        while True:
            event = self.queue.get()
            if event:
                logging.info('Event detected %s' % event)
                method = getattr(self, event.pop('type'))
                if method:
                    method(**event)

    def goal_scored(self, player_id):
        """
        Push a goal to subscribers
        """
        self.client.trigger(
            'kicker_channel',
            'goal_scored',
            {'player': player_id}
        )
        logging.info('Goal for player %s triggered' % player_id)

"""
Singleton module for pusher api functions
"""
import pusher
from config import PUSHER_APP_ID, PUSHER_SECRET_KEY, PUSHER_KEY

# connect to pusher
client = pusher.Pusher(
  app_id=PUSHER_APP_ID,
  key=PUSHER_KEY,
  secret=PUSHER_SECRET_KEY,
  cluster='eu',
  ssl=False
)
print 'Connected to Pusher'


def send_goal(player_id):
    """
    Push a goal to subscribers
    """
    client.trigger(
        'kicker_channel',
        'goal_scored',
        {'player': player_id}
    )

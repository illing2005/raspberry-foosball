"""
Test script to send a message via pusher.com
"""
import pusher_client


# trigger the event
pusher_client.client.trigger(
  'test_channel',
  'my_event',
  {'message': 'hello world'}
)

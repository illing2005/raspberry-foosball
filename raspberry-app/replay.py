import logging
import picamera


class Replay(object):

    def __init__(self, signals):

        self.camera = picamera.PiCamera()
        self.camera.framerate = 90
        self.camera.resolution = '920x750'
        self.stream = picamera.PiCameraCircularIO(self.camera, seconds=5)
        logging.info('Camera initialized: Frames %s, Resolution %s' % (self.camera.framerate, self.camera.resolution))

        self.signals = signals
        # connect to all signals we want to subscribe
        for name, signal in self.signals.iteritems():
            method = getattr(self, '%s_subscription' % name, None)
            if method:
                signal.connect(method)
                logging.info('Connected to signal "%s"' % name)

        self.camera.start_recording(self.stream, format='h264')
        logging.info('Camera: Start recording')


    def __def__(self):
        self.camera.stop_recording()


    def goal_scored_subscription(self, *args, **kwargs):
        print 'goal scored'
        self.stream.copy_to('goal_replay.h264', seconds=5)
        logging.info('Replay stored in goal_replay.h264')

import logging
import picamera
import SimpleHTTPServer
import SocketServer
import threading
import os


class Replay(object):

    file_name = 'goal_replay'

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

        self.start_http_server()
        logging.info('Camera: Http server started')

    def __def__(self):
        self.camera.stop_recording()

    def start_http_server(self):
        PORT = 8000
        Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        httpd = SocketServer.TCPServer(("", PORT), Handler)
        logging.info("serving at port %s" % PORT)
        t = threading.Thread(target=httpd.serve_forever)
        t.start()

    def goal_scored_subscription(self, *args, **kwargs):
        self.stream.copy_to('%s.h264' % self.file_name, seconds=5)
        os.system('avconv -v quiet -i %s.h264 -codec:v copy -f mp4 -y %s.mp4' % (self.file_name, self.file_name))
        logging.info('Replay stored in %s.h264' % self.file_name)
        self.signals['replay_ready'].send({'type': 'replay_ready', 'path': '%s.mp4' % self.file_name})

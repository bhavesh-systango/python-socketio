# set async_mode to 'threading', 'eventlet', 'gevent' or 'gevent_uwsgi' to
# force a mode else, the best mode is selected automatically from what's
# installed
async_mode = "eventlet"

import os

from django.http import HttpResponse
import socketio
import base64
from io import StringIO
import io
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt


basedir = os.path.dirname(os.path.realpath(__file__))
sio = socketio.Server(async_mode=async_mode)
print("----sio----", sio)


def index(request):
    # global thread
    # if thread is None:
        # thread = sio.start_background_task(background_thread)
    return HttpResponse(open(os.path.join(basedir, 'static/index.html')))


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        sio.sleep(10)
        count += 1
        sio.emit('my_response', {'data': 'Server generated event'},
                 namespace='/test')

@sio.event
def my_event(sid, event):
    print("hello", event)
    sio.emit('my_response', {'data': 'How r u'},)
    # data = event
    # sbuf = StringIO()
    # sbuf.write(data)
    # b = io.BytesIO(base64.b64decode(data))
    # try:
    #     pimg = Image.open(b)
    #     plt.imshow(np.array(pimg))
    #     print("hiii")
    #     plt.show()
    # except:
    #     pass




#!/usr/bin/python

import threading
import time
import rovio

class RovioController(threading.Thread):

    """
    Controls the Rovio robot.

    A higher-level wrapper for the API.

    Attributes:
      - rovio: the Rovio being controlled (read-only)
      - wait: the amount of time to sleep before checking the Rovio event queue

    """

    def getRovio(self): return self._rovio
    rovio = property(getRovio, doc="""Rovio being controlled (read-only)""")

    def __init__(self, rovio):
        """
        Initialize a RovioController.

        Parameters:
          - rovio: rovio object to be controlled

        """
        threading.Thread.__init__(self)
        self._rovio = rovio
        self._running = True
        self._queue = []
        self.wait = 0.1

    def enqueue(self, millis, command, params=[]):
        self._queue.append([None, millis, command, params])

    def enqueue_all(self, commands):
        self._queue.extend(commands)

    def interrupt(self, millis, command, params=[]):
        self._queue = [[None, millis, command, params]]

    def clear(self):
        self._queue = []

    def _dispatch(self):
        if len(self._queue) > 0:
            cmd = self._queue[0][2]
            parms = self._queue[0][3]
            if isinstance(parms, list):
                cmd(*parms)
            elif isinstance(parms, dict):
                cmd(**parms)

    def stop(self):
        self._running = False

    def run(self):
        while self._running:
            if len(self._queue) > 0:
                if self._queue[0][0] is None:
                    # start executing
                    self._queue[0][0] = time.time()
                    self._dispatch()
                else:
                    # continue executing, check for time
                    now = time.time()
                    elapsed = (now - self._queue[0][0]) * 1000
                    millis = self._queue[0][1]
                    if elapsed > millis:
                        self._queue = self._queue[1:]
                    else:
                        self._dispatch()
            time.sleep(self.wait)

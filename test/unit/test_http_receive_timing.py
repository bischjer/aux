from unittest2 import TestCase
# from aux.protocol.http.http import HTTP
from aux.api import http
import struct
import os
from ..util.mockhttpserver import MockHTTPServer


class HTTPReceiveTimingTest(TestCase):


    def setUp(self):
        self.test_server = MockHTTPServer(port=8880)
        self.test_server.start_thread()

    def tearDown(self):
        self.test_server.stop()
        
    def test_receive_imediate(self):
        response = http.get("http://localhost:8880/wait/0",
                            headers={})
        print response
        

from unittest2 import TestCase
from aux.api import http
import os
from ..util.mockhttpserver import MockHTTPServer
from time import sleep
from datetime import datetime, timedelta

class HTTPReceiveTimingTest(TestCase):

    def setUp(self):
        def wait_server_app(environ, start_response):
            path = environ.get('request').split()[1]
            sleep_time = float(path.replace('/wait/',''))
            sleep(sleep_time)
            return "HTTP/1.1 200 OK\r\nSlept for %f\r\n\r\n" % (sleep_time)
        
        self.test_server = MockHTTPServer(port=8880)
        self.test_server.applications['/wait'] = wait_server_app
        self.test_server.start_thread()

    def tearDown(self):
        self.test_server.stop()

    def test_receive_missing_route_404(self):
        response = http.get("http://localhost:8880",
                            headers={})
        self.assertEquals(404,
                          response.status)
        
    def test_receive_with_response_time_0_0(self):
        wait_time = 0.0
        then = datetime.now()
        response = http.get("http://localhost:8880/wait/%f" % (wait_time),
                            headers={})
        response_time = datetime.now() - then
        self.assertTrue(response_time > timedelta(seconds=wait_time))
        tolerance = 0.01
        self.assertTrue(response_time < timedelta(seconds=wait_time+tolerance))
        self.assertEquals(200,
                          response.status)

    def test_receive_with_response_time_0_2(self):
        wait_time = 0.2
        then = datetime.now()
        response = http.get("http://localhost:8880/wait/%f" % (wait_time),
                            headers={})
        response_time = datetime.now() - then
        self.assertTrue(response_time > timedelta(seconds=wait_time))
        tolerance = 0.01
        self.assertTrue(response_time < timedelta(seconds=wait_time+tolerance))
        self.assertEquals(200,
                          response.status)        

    def xtest_timeout(self):
        pass

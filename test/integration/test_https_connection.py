from unittest2 import TestCase
from aux.protocol.http import HTTP, HTTPRequest
from ..util.mockhttpserver import MockHTTPSServer

class HTTPSConnectionTest(TestCase):
    
    def setUp(self):
        def https_server_app(environ, start_response):
            return "HTTP/1.1 200 OK\r\nContent-Length: 9\r\n\r\nIt works!\r\n\r\n"
        
        self.test_server = MockHTTPSServer(port=8443)
        self.test_server.applications['/https/connection/ok'] = https_server_app
        self.test_server.start_thread()

    def tearDown(self):
        self.test_server.stop()

    def test_connection_success(self):
        http = HTTP()
        http_request = HTTPRequest(
            url='https://127.0.0.1:8443/https/connection/ok',
            request_data={'method':'GET',
                          'headers': {'Host': 'Aux/0.1 (X11; Ubuntu; Linux x86_64; rv:24.0)',
                                      'User-Agent': 'Aux/0.1 (X11; Ubuntu; Linux x86_64; rv:24.0)',
                                      'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                      'Accept-Language': 'en-US,en;q=0.5',
                                      'Referer': 'http://abc.abc',
                                      'Cache-Control': 'max-stale=0',
                                      'Connection': 'Keep-Alive'
                                      },
                          'data': 'fakedata'})
        response = http.send(http_request)
        self.assertEquals(200,
                          response.status)
        self.assertTrue('It works!' in response.body)




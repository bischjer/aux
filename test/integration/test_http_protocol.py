from unittest2 import TestCase
from aux.api import http
from ..util.mockhttpserver import MockHTTPServer


class HTTPProtocolTest(TestCase):

    def setUp(self):
        def short_response_app(environ, start_response):
            return "HTTP/1.1 200 OK\r\nContent-Length: 22\r\n\r\n<html>It works!</html>\r\n\r\n"
        def long_response_app(environ, start_response):
            ltrs = [a for a in ['A'*20000]]
            return "HTTP/1.1 200 OK\r\nContent-Length: 20000\r\n\r\n%s\r\n\r\n" % (ltrs)
        
        
        self.test_server = MockHTTPServer(port=8989)
        self.test_server.applications['/response/short'] = short_response_app
        self.test_server.applications['/response/long'] = long_response_app
        self.test_server.start_thread()
        
    def tearDown(self):
        self.test_server.stop()
    
    def test_connection(self):
        response = http.get('http://127.0.0.1:8989/response/short',
                            headers={'Host': 'a.a.a',
                                     'User-Agent': 'Aux/0.1',
                                     'Accept':'text/html',
                                     'Connection': 'Keep-Alive'
                                     })
        self.assertEquals(200,
                          response.status)
        self.assertEquals('<html>It works!</html>',
                          response.body)

        
    def xtest_handle_long_response(self):
        #TODO: Overread bug
        response = http.get('http://127.0.0.1:8989/response/long',
                            headers={'Host': 'a.a.a',
                                     'User-Agent': 'Aux/0.1',
                                     'Accept':'text/html',
                                     'Connection': 'Keep-Alive'
                                     })
        self.assertEquals(200,
                          response.status)
        self.assertEquals(20000,
                          len(response.body))


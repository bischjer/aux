from unittest2 import TestCase
from aux.protocol.http.parser import HTTPResponseParser


class HTTPResponseParserTest(TestCase):

    def test_basic_headers(self):
        content = """{\"hello\" : \"world\"}"""
        message = """HTTP/1.0 200 OK\r\nContent-Type: application/xml; charset=utf-8\r\nContent-Length: 19\r\nCache-Control: max-age=10,must-revalidate\r\nExpires: Sun, 29 Nov 2015 10:41:26 GMT\r\nServer: Eve/0.5.3 Werkzeug/0.9.6 Python/2.7.6\r\nDate: Sun, 29 Nov 2015 10:41:06 GMT\r\n\r\n%s\r\n\r\n""" % content
        response = HTTPResponseParser(message)()

        print response

    def test_problematic_colon_response(self):
        message = '''HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 227
Server: Eve/0.5.3 Werkzeug/0.9.6 Python/2.7.6
Date: Mon, 21 Dec 2015 15:18:53 GMT

{"_updated": "Mon, 21 Dec 2015 15:18:53 GMT", "_links": {"self": {"href": "user/2", "title": "user"}}, "_created": "Mon, 21 Dec 2015 15:18:53 GMT", "_status": "OK", "_id": 2, "_etag": "6f8c5078eff68d99a96aec858ed8074dc99a6409"}'''
        response = HTTPResponseParser(message)()

        print response

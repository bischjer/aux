import re
from http import HTTPResponse


class HTTPBodyParser(object):
    
    def __init__(self, message):
        self.message = message

    def __call__(self):
        body = ""

class HTTPHeaderParser(object):
    RE_HEADERS = re.compile(r'^([A-Za-z\-]+\:\s?[A-Za-z0-9\/\;\:\-\=\.\,\s]+)')
    
    def __init__(self, message):
        self.message = message

    def __call__(self):
        print [h for h in self.message.splitlines()]
        # headers = [h for h in self.RE_HEADERS.match(self.message).groups()]
        # headers = [self.RE_HEADERS.match(h).groups() for h in self.message.splitlines() if len(h) > 0]
        # print headers
        # return headers, HTTPBodyParser(self.message)()
        return None


class HTTPStartLine(object):
    RE_STARTLINE = re.compile(r'^(HTTP\/(\d\.\d)\s(\d{3})\s(\w+))')
    
    def __init__(self, message):
        self.message = message
        
    def __call__(self):
        self.line, self.httpversion, self.status, self.code = self.RE_STARTLINE.match(self.message).groups()
        print len(self.line)
        print self.line
        self.message = self.message[len(self.line):]
        return self.status, HTTPHeaderParser(self.message)()

        
class HTTPResponseParser(object):
    
    def __init__(self, message):
        self.message = message

    def __call__(self):
        status, headers = HTTPStartLine(self.message)()
        return HTTPResponse(status, response_data={'headers': headers,
                                                   'body': 'b'})
        
    

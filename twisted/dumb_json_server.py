from twisted.internet import reactor
from twisted.web import static, server
from twisted.web.resource import Resource
import json
from time import sleep

class DumbJSONServer(Resource):
    def getChild(self, name, request):
        return self
    def render_GET(self, request):
	headers = [
	    ("Access-Control-Allow-Origin", ["*"]),
	    ( "Access-Control-Allow-Methods", ["GET, POST, PUT, DELETE, OPTIONS"] ),
	    ( "Access-Control-Allow-Headers", ["X-Requested-With"] ) ]
	for header in headers:
	    request.responseHeaders.setRawHeaders(*header)
	sleep(0.2)
	print "Returning request"
	return json.dumps({'name' : 'jeff', 'age':24})

if __name__ == '__main__':
    site = server.Site(DumbJSONServer())
    reactor.listenTCP(8001, site)
    reactor.run()

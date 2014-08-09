import cgi
from google.appengine.api import users
import webapp2
from google.appengine.ext import ndb
from google.appengine.ext import ndb
from google.appengine.api import urlfetch

import urllib

urlfetch.set_default_fetch_deadline(60)

MAIN_PAGE_HTML = """\
<html>
  <body>
    <form action="/sign" method="post">
        <button>post</button>
    </form>
	
    <form action="/slot" method="post">
        count:<input type="text" name="count"></br>
        deviceId:<input type="text" name="deviceId"></br>
        <input type="submit" value="Submit">
    </form>
	
    <form action=""
  </body>
</html>
"""

count = -1
userId = -1
deviceId = -1

#url = "https://58.247.178.239:8443/parking/countdown/gfgADSFDF?count=10"
class MainPage(webapp2.RequestHandler):
    def get(self):
        f=open('workfile.txt','r')
        self.response.write(MAIN_PAGE_HTML)
        self.response.write(f.read())


class Guestbook(webapp2.RequestHandler):
    def post(self):
        self.response.write(count)
        pass
        #url = "https://58.247.178.239:8443/parking/countdown/gfgADSFDF"
        #self.response.write('111')
        #form_fields = {
            #"count":"10"
        #}
        #form_data = urllib.urlencode(form_fields)
        #result = urlfetch.fetch(url=url,
                                #payload=form_data,
                                #method=urlfetch.POST,
                                #headers={'Content-Type':'application/x-www-form-urlencoded'})

        #if result.status_code == 200:
            #self.response.write("parking slots: "+str(result.content))
        #else:
            #self.response.write("status_code: "+str(result.status_code))

class ParkingSlot(webapp2.RequestHandler):
    def get(self):
        self.response.write(count)
        pass


    def post(self):
        global count
        f = open('UserId.txt','r')
        userId = f.read()
        self.response.write('userId:'+userId)


        count = self.request.get('count')
        if count == '':
            count = -1
        self.response.write(count)

        
        deviceId = self.request.get('deviceId')
        if deviceId == '':
            deviceId =-1
        self.response.write(deviceId)
        
        if count < 0 or deviceId <0:
            self.response.write("error1")
        elif userId != deviceId:
	    self.response.write("error2")
	else:
            #print "count is :%s"%(count)
            self.response.write("success")



routes = [
    ('/', MainPage),
    ('/sign', Guestbook),
    ('/parking/countdown/gfgADSFDF',ParkingSlot),
    ('/slot',ParkingSlot)
]

application = webapp2.WSGIApplication(routes=routes, debug=True)

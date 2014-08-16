import cgi
from google.appengine.api import users
import webapp2
from google.appengine.ext import ndb
from google.appengine.api import urlfetch

import time
import datetime
import urllib

urlfetch.set_default_fetch_deadline(60)

count = -1
userId = -1
deviceId = -1
# global time_key


# CUR_TIME = strftime("%a, %d %b %H:%M:%S", gmtime())


MAIN_PAGE_HTML = """\
<html>
  <body>
    <form action="/parking/countdown" method="post">
        <button>countdown</button>
    </form>

    <form action="/parking/getcount" method="post">
        count:<input type="text" name="count"></br>
        deviceId:<input type="text" name="deviceId"></br>
        <input type="submit" value="getcount"></br>
    </form>

    <form action="/parkingservice/history" method="post">
        <button>gettime</button>
    </form>

    <form action=""
  </body>
</html>
"""


class History(ndb.Model):

    time = ndb.DateTimeProperty(auto_now_add=True)
history = History()
time_key = None


class MainPage(webapp2.RequestHandler):

    def get(self):
        # f=open('workfile.txt','r')
        self.response.write(MAIN_PAGE_HTML)
        # self.response.write(f.read())
        self.response.write('<html><body>')


class Countdown(webapp2.RequestHandler):

    def get(self):
        self.response.write(count)
        pass

    def post(self):
        self.response.write(count)
        # self.response.write(history.time)
        pass


class Gettime(webapp2.RequestHandler):

    def get(self):
        global time_key
        deadline = time_key.get()
        self.response.write(deadline)

    def post(self):
        global time_key
        deadline = time_key.get()
        self.response.write(deadline)


class Getcount(webapp2.RequestHandler):

    def get(self):
        post(self)

    def post(self):
        global count
        print "here ha ha ha "
        f = open('UserId.txt', 'r')
        userId = f.read()
        self.response.write(userId)

        count = self.request.get('count')
        if count == '':
            count = -1

        deviceId = self.request.get('deviceId')
        if deviceId == '':
            deviceId = -1
        self.response.write(deviceId)

        if count < 0 or deviceId < 0:
            self.response.write("error1")
            return
        elif userId != deviceId:
            self.response.write("error2")
            return
        else:
            self.response.write("success")
            # self.response.write(count)
            if count == '0':
                # self.response.write('count:'+count)
                history = History()
                tt = time.time()
                tt += time.altzone
                # self.response.write(tt)
                tt += 9 * 3600
                # self.response.write(tt)
                # history.time = datetime.datetime.utcfromtimestamp(tt)
                self.response.write(history.time)
                self.response.write('%%%%%%%1')
                global time_key
                time_key = history.put()
                self.response.write('%%%%%%%2')


routes = [
    ('/', MainPage),
    ('/parking/countdown', Countdown),
    #('/parking/countdown/gfgADSFDF',ParkingSlot),
    ('/parking/getcount', Getcount),
    ('/parkingservice/history', Gettime),
]

application = webapp2.WSGIApplication(routes=routes, debug=True)

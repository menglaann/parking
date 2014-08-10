import cgi
from google.appengine.api import users
import webapp2
from google.appengine.ext import ndb
from google.appengine.ext import ndb
from google.appengine.api import urlfetch

from time import gmtime, strftime

import urllib

urlfetch.set_default_fetch_deadline(60)

count = -1
userId = -1
deviceId = -1
#CUR_TIME = strftime("%a, %d %b %H:%M:%S", gmtime())

MAIN_PAGE_HTML = """\
<html>
  <body>
    <form action="/sign" method="post">
        <button>post</button>
    </form>
	
    <form action="/slot" method="post">
        count:<input type="text" name="count"></br>
        deviceId:<input type="text" name="deviceId"></br>
        cur_time:
        <input type="text" id="cur_time"></br>

        <script type="text/javascript">
            var elem = document.getElementById("cur_time");
            elem.value = "current time";
        </script></br>

        
        <div ng-controller = "MyCtrl">
            <input type = "date" name = "date" ng-model = "date">
                <p>{{date}}</p>
            <input type = "time" name = "time">
        </div>
        <script>
            var myApp = angular.module('myApp',[]);
            function MyCtrl($scope){
                $scope.date = moment();
            }
        </script>

        <input type="submit" value="Submit"></br>
    </form>

	
    <form action=""
  </body>
</html>
"""



#url = "https://58.247.178.239:8443/parking/countdown/gfgADSFDF?count=10"
class MainPage(webapp2.RequestHandler):
    def get(self):
        f=open('workfile.txt','r')
        self.response.write(MAIN_PAGE_HTML)
        self.response.write(f.read())
        self.response.write('<html><body>')
        #cur_time = self.request.get('cur_time',CUR_TIME)

        #self.response.write(cur_time)


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
        

        
        deviceId = self.request.get('deviceId')
        if deviceId == '':
            deviceId =-1
        self.response.write(deviceId)

        if count < 0 or deviceId <0:
            self.response.write("error1")
            return
        elif userId != deviceId:
	    self.response.write("error2")
	    return
	else:
            #print "count is :%s"%(count)
            self.response.write("success")
            self.response.write(count)


        #self.response.write(cur_time)


        #if count == 0:
        self.response.write('count:'+count)

            #history = History(parent=ndb.Key("history","data"),
                              #time = self.request.get('cur_time'))
        history = History()
        history.date = self.request.get('date')
        history.time = self.request.get('time')
        self.response.write(history.date)
        self.response.write(history.time)
        history.put();



class History(ndb.Model):

    date = ndb.DateTimeProperty(auto_now_add=True)
    time = ndb.DateTimeProperty(auto_now_add=True)




routes = [
    ('/', MainPage),
    ('/sign', Guestbook),
    ('/parking/countdown/gfgADSFDF',ParkingSlot),
    ('/slot',ParkingSlot)
]

application = webapp2.WSGIApplication(routes=routes, debug=True)

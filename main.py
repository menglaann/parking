import cgi
from google.appengine.api import users
import webapp2
from google.appengine.ext import ndb
from google.appengine.api import urlfetch

import time
<<<<<<< HEAD
import datetime
=======

>>>>>>> 067f454a2f529bfd222e9b3764a52a83f5aee911
import urllib

urlfetch.set_default_fetch_deadline(60)

count = -1
userId = -1
deviceId = -1
<<<<<<< HEAD
time_key


#CUR_TIME = strftime("%a, %d %b %H:%M:%S", gmtime())
=======
# CUR_TIME = strftime("%a, %d %b %H:%M:%S", gmtime())
>>>>>>> 067f454a2f529bfd222e9b3764a52a83f5aee911


MAIN_PAGE_HTML = """\
<html>
  <body>
    <form action="/parking/countdown" method="post">
        <button>countdown</button>
    </form>
<<<<<<< HEAD
	
    <form action="/parking/getcount" method="post">
        count:<input type="text" name="count"></br>
        deviceId:<input type="text" name="deviceId"></br>
        <input type="submit" value="getcount"></br>
    </form>

    <form action="/parkingservice/history" method="post">
        <button>gettime</button>
    </form>
	
=======

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


>>>>>>> 067f454a2f529bfd222e9b3764a52a83f5aee911
    <form action=""
  </body>
</html>
"""
class History(ndb.Model):

<<<<<<< HEAD
    time = ndb.DateTimeProperty(auto_now_add=True)
history = History()
    
=======

# url = "https://58.247.178.239:8443/parking/countdown/gfgADSFDF?count=10"
>>>>>>> 067f454a2f529bfd222e9b3764a52a83f5aee911
class MainPage(webapp2.RequestHandler):

    def get(self):
<<<<<<< HEAD
        #f=open('workfile.txt','r')
=======
        f = open('workfile.txt', 'r')
>>>>>>> 067f454a2f529bfd222e9b3764a52a83f5aee911
        self.response.write(MAIN_PAGE_HTML)
        #self.response.write(f.read())
        self.response.write('<html><body>')
<<<<<<< HEAD

class Countdown(webapp2.RequestHandler):
    def get(self):
        self.response.write(count)
        pass
=======
        # cur_time = self.request.get('cur_time',CUR_TIME)

        # self.response.write(cur_time)


class Guestbook(webapp2.RequestHandler):

>>>>>>> 067f454a2f529bfd222e9b3764a52a83f5aee911
    def post(self):
        self.response.write(count)
        #self.response.write(history.time)
        pass
<<<<<<< HEAD

class Gettime(webapp2.RequestHandler):
    def get(self):
        deadline = time_key.get()
        self.response.write(deadline)
    def post(self):
        deadline = time_key.get()
        self.response.write(deadline)
        
        
class Getcount(webapp2.RequestHandler):
    def get(self):
        post(self)
=======
        # url = "https://58.247.178.239:8443/parking/countdown/gfgADSFDF"
        # self.response.write('111')
        # form_fields = {
            #"count":"10"
        #}
        # form_data = urllib.urlencode(form_fields)
        # result = urlfetch.fetch(url=url,
                                # payload=form_data,
                                # method=urlfetch.POST,
                                # headers={'Content-Type':'application/x-www-form-urlencoded'})

        # if result.status_code == 200:
            # self.response.write("parking slots: "+str(result.content))
        # else:
            # self.response.write("status_code: "+str(result.status_code))


class ParkingSlot(webapp2.RequestHandler):

    def get(self):
        self.response.write(count)
        pass
>>>>>>> 067f454a2f529bfd222e9b3764a52a83f5aee911

    def post(self):
        global count
<<<<<<< HEAD
        print "here ha ha ha "
        f = open('UserId.txt','r')
        userId = f.read()
        self.response.write(userId)

=======
        f = open('UserId.txt', 'r')
        userId = f.read()
        self.response.write('userId:' + userId)
>>>>>>> 067f454a2f529bfd222e9b3764a52a83f5aee911

        count = self.request.get('count')
        if count == '':
            count = -1
<<<<<<< HEAD
           
=======

>>>>>>> 067f454a2f529bfd222e9b3764a52a83f5aee911
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
<<<<<<< HEAD
            self.response.write("success")
            #self.response.write(count)
            if count == '0':
                #self.response.write('count:'+count)
                history = History()
                tt = time.time()
                tt += time.altzone
                #self.response.write(tt)
                tt += 9 * 3600
                #self.response.write(tt)
                history.time = datetime.datetime.utcfromtimestamp(tt)
                self.response.write(history.time)
                self.response.write('%%%%%%%1')
                time_key = history.put()
                self.response.write('%%%%%%%2')




=======
            # print "count is :%s"%(count)
            self.response.write("success")
            self.response.write(count)

        # self.response.write(cur_time)

        # if count == 0:
        self.response.write('count:' + count)

        # history = History(parent=ndb.Key("history","data"),
        # time = self.request.get('cur_time'))
        history = History()
        # history.date = self.request.get('date')
        # history.time = self.request.get('time')
        # self.response.write(history.date)
        # history.time = time.time()
        self.response.write(time.ctime(history.time))
        history.put()


class History(ndb.Model):

    # date = ndb.DateTimeProperty(auto_now_add=True)
    time = ndb.DateTimeProperty(auto_now_add=True)

>>>>>>> 067f454a2f529bfd222e9b3764a52a83f5aee911

routes = [
    ('/', MainPage),
<<<<<<< HEAD
    ('/parking/countdown', Countdown),
    #('/parking/countdown/gfgADSFDF',ParkingSlot),
    ('/parking/getcount',Getcount),
    ('/parkingservice/history',Gettime),
=======
    ('/sign', Guestbook),
    ('/parking/countdown/gfgADSFDF', ParkingSlot),
    ('/slot', ParkingSlot)
>>>>>>> 067f454a2f529bfd222e9b3764a52a83f5aee911
]

application = webapp2.WSGIApplication(routes=routes, debug=True)

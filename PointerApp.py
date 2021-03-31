'''
Ti den exei ginei:
    marker
    gps
    search mesw onomatos
    Event Profile
    Friend Requests Handling
    Options
'''

'''
Genika 8elw mia global metavlhth , h opoia 8a einai o user
pou xrhsimopoiei to app thn dedomenh stigmh
'''
global App_Usr

import kivy

kivy.require("2.0.0")

from plyer import gps

from kivy.properties import AliasProperty
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy_garden.mapview import MapView

from kivy.lang import Builder
from kivy.app import App

epiloges_arr = ["Map","Profile","Locations","Friends","Events","Friend\nRequests","Options"]
user_info = ["Id : ","Username : ","Points : ","Location : ","On Event : "]

class BackgroundColor(Widget):
    pass
class BackgroundLabel(Label,BackgroundColor):
    pass
class Epiloges_Button(Button):
    pass
class Profile_Layout(BoxLayout):
    pass
class Location_Layout(BoxLayout):
    pass
class Friend_Request_Layout(BoxLayout):
    pass

#gia recycle view
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleKVIDsDataViewBehavior
#
#Recycle View
#
Builder.load_string('''
<RV_content@Button>:
    font_size : '20dp'
    background_color : .3,.5,.55,.85

<RV>:
    data : []
    viewclass: 'RV_content'
    RecycleBoxLayout:
        default_size: None, dp(65)
        default_size_hint: 1,None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
''')
class RV_content(Button):
    l = None
    b = None
    #prepei me kapoio tropo to button na krata to location
    #otan to button patietai prepei na yparxei metavlhth
    #t.w. na elegxetai to ann to button pati8hke h oxi
    def __init__(self,l = None,b = None,**kwargs):
        super(RV_content,self).__init__(**kwargs)
        self.l = l
        self.b = b
    #
    #getter
    #
    def get_text(self):
        return str(self.text)
    def get_l(self):
        return self.l
    def on_pressed(self):
        self.b(self.get_l())
    def get_b(self):
        return self.b
    #
    #getter
    #
    #
#
#Gia RV_content
#
class RV(RecycleView):
    def __init__(self,arr,**kwargs):
        super(RV, self).__init__(**kwargs)
        #pernaw text kai location
        #to callback exei perasei sto x
        self.data = [{'text': x.get_l().location_string(),'l' : x.get_l(),'b' : x.get_b(),'on_press' : x.on_pressed} for x in arr]
#
#Recycle View
#
#
#Friend Requests Class
#
class FriendRequest:
    _id_1 = 0
    _id_2 = 0
    _name_1 = ""
    _name_2 = ""
    _state_1 = "Pending"
    _state_2 = "Pending"
    #isws valw timestamp

    def __init__(self,id_1 = 0,id_2 = 0,name_1 = "",name_2 = "",state_1 = "Pending",state_2 = "Pending"):
        self._id_1 = id_1
        self._id_2 = id_2
        self._name_1 = name_1
        self._name_2 = name_2
        self._state_1 = state_1
        self._state_2 = state_2
    #
    #setter
    #
    def set_id_1(self,id_1 = 0):
        self._id_1 = id_1
    def set_id_2(self,id_2 = 0):
        self._id_2 = id_2
    def set_name_1(self,name_1 = ""):
        self._name_1 = name_1
    def set_name_2(self,name_2 = ""):
        self._name_2 = name_2
    def set_state_1(self,state = 0):
        if state == 0:
            self._state_1 = "Pending"
        elif state == 1:
            self._state_1 = "Accepted"
        else:
            self._state_1 = "Rejected"
    def set_state_2(self,state = 0):
        if state == 0:
            self._state_2 = "Pending"
        elif state == 1:
            self._state_2 = "Accepted"
        else:
            self._state_2 = "Rejected"
    #
    #setter
    #
    #
    #getter
    #
    def get_id_1(self):
        return self._id_1
    def get_id_2(self):
        return self._id_2
    def get_name_1(self):
        return self._name_1
    def get_name_2(self):
        return self._name_2
    def get_state_1(self):
        return self._state_1
    def get_state_2(self):
        return self._state_2
    #
    #getter
    #
    #
    #friend request string
    #
    def friend_request_string(self):
        return self._name_1 +" "+self._state_1+" "+self._name_2+" "+self._state_2
    #
    #friend request string
    #
    #
    #Friend request Array
    #
    def friend_request_info_array(self):
        arr = []
        arr.append("You : " +self._name_1)
        arr.append("From : " +self._name_2)
        arr.append("State : " +self._state_1)
        return arr
    #
    #Friend request Array
    #
#
#Friend Requests Class
#
#
#Recycle View gia Friend Requests
#
Builder.load_string('''
<friend_requests_content@RecycleKVIDsDataViewBehavior+BoxLayout>:
    b_label : b_label
    profile_button : profile_button
    accept_button : accept_button
    reject_button : reject_button
    orientation : 'horizontal'
    BackgroundLabel :
        id : b_label
    Button :
        id : profile_button
        size_hint_x : .3
        text : 'User Profile'
        font_size : '20dp'
        background_color : .3,.5,.55,.85
    Button :
        id : accept_button
        size_hint_x : .2
        text : 'Accept'
        font_size : '20dp'
        background_color : .3,.5,.55,.85
    Button :
        id : reject_button
        size_hint_x : .2
        text : 'Reject'
        font_size : '20dp'
        background_color : .3,.5,.55,.85
<friend_requests_rv>:
    viewclass: 'friend_requests_content'
    RecycleBoxLayout:
        default_size: None, dp(65)
        default_size_hint: 1,None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
''')
#
#ti periexei to rrv
#
class friend_requests_content(RecycleKVIDsDataViewBehavior,BoxLayout):
    #8a prepei na kouvalaei to friend_request,to b_label,to accept_funct...
    f = None
    b_label = None
    user_funct = None
    reject_funct = None
    usr = None

    def __init__(self,f = None,user_funct = None,usr = None,reject_funct = None,**kwargs):
        super(friend_requests_content,self).__init__(**kwargs)
        self.f = f
        self.usr = usr
        self.user_funct = user_funct
        self.reject_funct = reject_funct

    #
    #setter
    #
    #
    #setter
    #
    #
    #getter
    #
    def get_blabel(self):
        return self.b_label
    def get_f(self):
        return self.f#return friend request
    def get_accept(self):
        return self.accept_funct
    def get_reject(self):
        return self.reject_funct
    def get_user_f(self):
        return self.user_funct
    #
    #getter
    #
    #
    #reject callback
    #
    def reject_callback(self,*pos):
        global App_Usr
        self.f.set_state_1("Rejected")
        self.reject_button.bind(on_press = self.reject_funct)
        return self.reject_button.on_press()
    #
    #reject callback
    #
    #
    #accept callback
    #
    def accept_callback(self,*pos):
        self.f.set_state_1("Accepted")
    #
    #accept callback
    #
#
#ti periexei to rrv
#
#
#to rrv
#
class friend_requests_rv(RecycleView):
    def __init__(self,arr,**kwargs):
        super(friend_requests_rv,self).__init__(**kwargs)
        self.data = [{'b_label.text' : x.get_f().friend_request_string(),'reject_button.on_press' : x.reject_callback ,'accept_button.on_press' : x.accept_callback,'profile_button.on_press' : x.get_user_f() } for x in arr]

#
#to rrv
#
#
#Recycle View gia Friend Requests
#
#
#
#Gia Events Class
#
class Events:
    #event info
    _id = 0
    _name = ""
    _location = None
    _points_g = 0
    _points_r = 0
    _cap = 0
    _counter = 0
    _prv = False
    #usr info
    _creator = None
    _participate = []

    def __init__(self,id = 0,name = "",location = None,points_g = 0,points_r = 0,cap = 0,counter = 0,prv = False,creator = None,participate = []):
        #event info
        self._id = id
        self._name = name
        self._location = location
        self._points_g = points_g
        self._points_r = points_r
        self._cap = cap
        self._counter = counter
        self._prv = prv
        #usr info
        self._creator = creator
        self._participate = participate
    #
    #setter
    #
    #event info
    def set_id(self,id = 0):
        self._id = id
    def set_name(self,name = ""):
        self._name = name
    def points(self,points_g = 0,points_r = 0):
        self.points_g = points_g
        self.points_r = points_r
    def set_cap(self,cap = 0):
        self._cap = cap
    def set_counter(self,counter):
        self._counter = counter
    def set_points_r(self,points_r):
        self._points_r = points_r
    def set_points_g(self,points_g):
        self._points_g = points_g
    def set_prv(self, prv = False):
        self._prv = prv
    #user info
    def set_creator(self,creator = None):
        self._creator = creator
    def set_usrs(self,participate = []):
        self._participate = participate
    #
    #getter
    #
    #event info
    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def get_points(self):
        return (self._points_g,self._points_r)
    def get_cap(self):
        return self._cap
    def get_counter(self):
        return self._counter
    def get_points_r(self):
        return self._points_r
    def get_points_g(self):
        return self._points_g
    def get_prv(self):
        return self._prv
    #user info
    def get_creator(self):
        return self._creator
    def get_users(self):
        return self._participate
    #
    #event string
    #
    def event_string(self):
        return self._name + " " + str(self._points_g)+" "+str(self._points_r)+" "+str(self._cap)+" "+str(self._counter)+" "+str(self._creator)+" "+str(len(self._participate)) +"\n"
#
#events class
#
#
#Recycle View gia Events
#

Builder.load_string('''
<event_content@RecycleKVIDsDataViewBehavior+GridLayout>:
    rows : 3
    b_label : b_label
    participation_button : participation_button
    profile_button : profile_button
    BackgroundLabel :
        id : b_label
    Button :
        id : participation_button
        text : 'Participate'
        font_size : '25dp'
        background_color : .3,.5,.55,.85
    Button :
        id : profile_button
        text : 'Event Profile'
        font_size : '25dp'
        background_color : .3,.5,.55,.85

<Events_RV>:
    data : []
    viewclass: 'event_content'
    RecycleBoxLayout:
        default_size: None, dp(200)
        default_size_hint: 1 ,None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
''')
class event_content(RecycleKVIDsDataViewBehavior,GridLayout):
    ev = None

    def __init__(self,ev ,**kwargs):
        super(event_content,self).__init__(**kwargs)
        self.ev = ev

    def get_ev(self):
        return self.ev

class Events_RV(RecycleView):

    def __init__(self,arr = [],**kwargs):
        super(Events_RV,self).__init__(**kwargs)
        self.data = [{'b_label.text' : x.get_ev().event_string()}for x in arr]
#
#Recycle View gia Events
#
#
#Location Class
#
class Location:
    #location info
    _id = 0
    _name = "" #1
    _lat = 0.0 #2
    _lon = 0.0 #2
    _counter = 0 #3
    _points = 0 #4
    _prv = False#dior8wse kai allou
    #user info
    _creator = None #5
    _usrs = [] #6
    #event info
    _events = [] #7

    def __init__(self,id = 0,name = "",lat = 0.0,lon = 0.0,counter = 0,points = 0,prv = False,creator = None,usrs = [],events = []):
        #location info
        self._id = id
        self._name = name
        self._lat = lat
        self._lon = lon
        self._counter = len(usrs)
        self._points = points
        self._prv = False
        #user info
        self._creator = creator
        self._usrs = usrs
        #event info
        self._events = events

    #
    #setter
    #
    #location info
    def set_id(self,id = 0):
        self._id = id
    def set_name(self,name = ""):
        self._name = name
    def set_coord(self,lon = 0.0,lat = 0.0):
        self._lon = lon
        self._lat = lat
    def set_counter(self,counter):
        self._counter = counter
    def set_points(self,points):
        self._points = points
    def set_prv(self,prv):
        self._prv = prv
    #user info
    def set_creator(self,creator = None):
        self._creator = creator
    def set_usrs(self,usrs = []):
        self._usrs = usrs
    #event info
    def set_events(self, events = []):
        self._events = events
    #
    #getter
    #
    #location info
    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def get_lon(self):
        return self._lon
    def get_lat(self):
        return self._lat
    def get_coord(self):
        return (self._lon,self._lat)
    def get_counter(self):
        return self._counter
    def get_points(self):
        return self._counter
    def get_prv(self):
        return self._prv
    #user info
    def get_creator(self):
        return self._creator
    def get_usrs(self):
        return self._usrs
    #event info
    def get_events(self):
        return self._events

    #Location String
    def location_string(self):
        return str(self._id) + ' ' + str(self._name) + ' ' + str(self._counter) + ' ' + str(len(self._events))
    #location info as an array
    def loc_info_array(self):
        arr = []
        arr.append("Name : " + self._name)
        arr.append("Coordinations : " + str(self.get_coord()))
        arr.append("Points : " +str(self._points))
        arr.append("Counter : " +str(self._counter))
        arr.append("Creator : " + str(self._creator))
        arr.append("Events : "+ str(len(self._events)))
        return arr
#
#Location Class
#
#user class
class User:
    #user info
    _id = 0
    _username = ""
    _pssw = ""
    _points = 0
    #event & location info
    _location = None
    _on_event = False
    _event = None
    _locations = []
    _events = []
    #friends info
    _frnds = []
    _frequests = []

    def __init__(self,id = 0,username = "",pssw = "",points = 0,location = None,event = None,locations = [],events = [],frnds = [],frequests = []):
        #user info
        self._id = id
        self._username = username
        self._pssw = pssw
        self._points = points
        #location info
        self._location = location
        self._locations = locations
        #event info
        if event == None:
            pass
        else:
            self._on_event = True
        self._event = event
        self._events = events
        #friends info
        self._frnds = frnds
        self._frequests = frequests

    #
    #setter
    #
    #user info
    def set_id(self,id = 0):
        self._id = id
    def set_username(self,username):
        self._username = username
    def set_pssw(self,pssw = ""):
        self._pssw = pssw
    def set_points(self,points = 0):
        self._points = points
    #location
    def set_location(self,location = None):
        self._location = location
    def set_locations(self,locations = []):
        self._locations = locations
    #event
    def set_event(self,event = None):
        self._event = event
        if event == None:
            pass
        else:
            self._on_event = True
    def set_events(self,events = []):
        self._events = events
    #frequests
    def set_frequests(self,frequests = []):
        self._frequests = frequests
    #other user info
    def set_frnds(self,frnds = []):
        self._frnds = frnds
    #
    #getter
    #
    #user info
    def get_id(self):
        return self._id
    def get_username(self):
        return self._username
    def get_points(self):
        return self._points
    #location
    def get_location(self):
        return self._location
    def get_locations(self):
        return self._locations
    #gia event
    def get_event(self):
        return self._event
    def get_on_event(self):
        return self._on_event
    def get_events(self):
        return self._events
    #gia friends
    def get_friends(self):
        return self._frnds
    #gia friend requests
    def get_friend_requests(self):
        return self._frequests
    def pop_friend_request(self, i = 0):
        self._frequests.pop(i)
    #User String
    def usr_string(self):
        #einai h oxi se event
        a = ""
        if self._on_event:
            a = "On event"
        else:
            a = "Not on event"
        return self._username +" "+self.loc_string() + " " + str(self._points) + " " + a
    #Location String
    def loc_string(self):
        try :
            a = self.get_location().location_string()
        except :
            return str(None)
#
#Gia User
#
#
#Recycle View gia Friends
#
#name points location name event online show_profile
Builder.load_string('''
<friends_content@RecycleKVIDsDataViewBehavior+BoxLayout>:
    b_label : b_label
    profile_button : profile_button
    BackgroundLabel:
        id : b_label
    Button :
        id : profile_button
        text : 'User Profile'
        font_size : '25dp'
        background_color : .3,.5,.55,.85

<Friends_Rv>:
    data : []
    viewclass: 'friends_content'
    RecycleBoxLayout:
        default_size: dp(65), dp(65)
        default_size_hint: 1,None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
''')
class friends_content(RecycleKVIDsDataViewBehavior,BoxLayout):
    friend = User()#o filos ws ontothta
    def __init__(self,friend = User(),**kwargs):
        super(friends_content,self).__init__(**kwargs)
        self.friend = friend

    #gia na parw to string tou User
    def get_user_string(self):
        return self.friend.usr_string()

class Friends_Rv(RecycleView):

    def __init__(self,arr,**kwargs):
        super(Friends_Rv,self).__init__(**kwargs)
        self.data = [{'b_label.text' : x.get_user_string()}for x in arr]
#
#Recycle View gia Friends
#
class PointerApp(App):

    _main_layout = None#to arxiko layout
    _epiloges = None#to layout me tis epiloges

    def build(self):
        global epiloges_arr
        #
        #gia gps
        #gps.configure(on_location = self.on_gps_location)
        #gps.start()
        #end gia gps
        #
        self._main_layout = GridLayout(cols = 2)
        self._main_layout.add_widget( MapView(zoom=15, lat=38.246700, lon=21.734823,size_hint = (1,.8)))#dhmiourgia xarth, ayto prepei na allaksei ws pros tis suntetagmenes kai to zoom!!
        #gia epiloges
        self._epiloges = BoxLayout(orientation = 'vertical',size_hint_x = .3)
        for i in range(0,7):
            btn = Epiloges_Button(text = epiloges_arr[i])
            if i == 0:
                btn.bind(on_press=self.map_callback)#map callback
            if i == 1:
                btn.bind(on_press = self.profile_callback)#profile button
            if i == 2:
                btn.bind(on_press = self.locations_callback)#gia known locations
            if i == 3 :
                btn.bind(on_press = self.friends_callback)#gia friends
            if i == 4:
                btn.bind(on_press=self.events_callback)#gia known events
            if i == 5:
                btn.bind(on_press=self.friend_request_callback)#gia friend request
            self._epiloges.add_widget(btn)
        self._main_layout.add_widget( self._epiloges)
        return self._main_layout

    #callbacks kai functions gia gps
    def on_gps_location(self,**kwargs):
        kwargs['lat'] = 10.0
        kwargs['lon'] = 10.0
        print(kwargs)
    #gia epistrofh sto map
    def map_callback(self,instance,*pos):
        #allazw to _main_layout
        self._main_layout.clear_widgets()
        self._main_layout.add_widget( MapView(zoom=11, lat=50.6394, lon=3.057,size_hint = (1,.8)))#dhmiourgia xarth, ayto prepei na allaksei ws pros tis suntetagmenes kai to zoom!!
        self._main_layout.add_widget(self._epiloges)
        return self._main_layout

    #gia profile
    def profile_callback(self,instance,*pos,usr = User()):
        #allazw to _main_layout
        self._main_layout.clear_widgets()

        pl = Profile_Layout()
        for i in range(0,5):
            #vriskw ti text 8a valw
            if i==0 :
                pl.add_widget(BackgroundLabel(text = user_info[i] + str(usr.get_id()),size_hint_y = 0.3 ) )#gia id
            elif i==1 :
                pl.add_widget(BackgroundLabel(text = user_info[i] + str(usr.get_username() ) ,size_hint_y = 0.3) )#gia username
            elif i == 2:
                pl.add_widget(BackgroundLabel(text = user_info[i] + str(usr.get_points()) ,size_hint_y = 0.3) )#gia points
            elif i == 3:
                if usr.get_location()==None:
                    pl.add_widget(BackgroundLabel(text = user_info[i] + str(usr.get_location() ) ,size_hint_y = 0.3) )#gia location
                else:
                    pl.add_widget(BackgroundLabel(text = user_info[i] + str(usr.loc_string() ) ,size_hint_y = 0.3) )#gia location
            else:
                pl.add_widget(BackgroundLabel(text = user_info[i] + str(usr.get_on_event()) ,size_hint_y = 0.3) )#an einai se event
        self._main_layout.add_widget(pl)
        self._main_layout.add_widget(self._epiloges)
        return self._main_layout
    #
    #gia profile
    #
    #
    #Gia Friends
    #
    def friends_callback(self,instance,*pos,usr = User()):
        ###
        temp = []
        for x in range(60):
            temp.append(User(id = x,username = str(x)))
        usr.set_frnds(temp)
        ###
        #ann den uparxoun friends
        if len(usr.get_friends()) == 0:
            self._main_layout.clear_widgets()
            a = BoxLayout()
            a.add_widget(BackgroundLabel(text = "You have no friends..!\nBe more social..!"))
            self._main_layout.add_widget(a)
        else:
            lst = []
            for i in usr.get_friends():
                a = friends_content(i)
                lst.append(a)
            self._main_layout.clear_widgets()
            self._main_layout.add_widget(Friends_Rv(arr = lst))
        self._main_layout.add_widget(self._epiloges)
        return self._main_layout
    #
    #gia Friends
    #
    #
    #Gia Locations
    #
    def locations_callback(self,instance,*pos,usr = User()):
        #vlepw an exei locations
        usr.set_locations([Location(0,"kati"),Location(1,"kati allo")])
        if len(usr.get_locations()) == 0:
            #an den exei locations
            self._main_layout.clear_widgets()
            a = BoxLayout()
            a.add_widget(BackgroundLabel(text = "There are no Locations known to you."))
            self._main_layout.add_widget(a)
        else:
            lst = []
            for i in usr.get_locations():
                a = RV_content(i,b = self.location_profile_callback)
                a.bind(on_press = self.location_profile_callback)
                lst.append(a)
            self._main_layout.clear_widgets()
            self._main_layout.add_widget( RV(arr = lst) )

        self._main_layout.add_widget(self._epiloges)
        return self._main_layout
    #
    #Gia Locations
    #
    #
    #Gia Location Profile
    #
    def location_profile_callback(self,l = Location()):
        #uparxei mia metavlhth h opoia apo8hkeuei to location
        #, auth perna ws parametros apo to koumpi
        a = Location_Layout()
        for i in l.loc_info_array():
            a.add_widget(BackgroundLabel(text = i,size_hint_y = 0.3))#allazw kai to mege8os
        #vgazw ola ta widgets
        self._main_layout.clear_widgets()
        self._main_layout.add_widget(a)
        self._main_layout.add_widget(self._epiloges)
        return self._main_layout
    #
    #Gia Location Profile
    #
    #
    #Gia Events
    #
    def events_callback(self,instance,*pos,usr = User() ):
        #
        temp = []
        for x in range(60):
            temp.append(Events(x,str(x)))
        usr.set_events(temp)
        #
        #vlepw ann yparxoun events
        if len(usr.get_events()) == 0:
            #den yparxoun gnwsta events
            self._main_layout.clear_widgets()
            a = BoxLayout()
            a.add_widget(BackgroundLabel(text = "There are no Events known to you."))
            self._main_layout.add_widget(a)
        else:
            lst = []
            for i in usr.get_events():
                a = event_content(ev = i)
                lst.append(a)
            self._main_layout.clear_widgets()
            self._main_layout.add_widget(Events_RV(arr = lst))

        self._main_layout.add_widget(self._epiloges)
        return self._main_layout
    #
    #Gia Events
    #
    #
    #Gia Friend Request
    #
    def friend_request_callback(self,*pos,usr = User(),**kwargs):
        #vlepw ann yparxoun friend requests
        global App_Usr
        App_Usr = User()
        App_Usr.set_frequests([FriendRequest(0,1,'tranpe','d4g10ur0s'),FriendRequest(2,1,'Pr','d4g10ur0s')])

        if len(App_Usr.get_friend_requests()) == 0:
            #ann den yparxoun friend requests
            self._main_layout.clear_widgets()
            a = BoxLayout()
            a.add_widget(BackgroundLabel(text = "You have no friend requests."))
            self._main_layout.add_widget(a)
        else:
            #ann uparxoun friend requests
            lst = []
            counter = 0
            for i in App_Usr.get_friend_requests():
                #diagrafw ola ta requests pou einai rejected.Meta 8a to paiksw me sundeseis
                if i.get_state_1() == 'Rejected' :
                    App_Usr.pop_friend_request(counter)
                    counter-=1
                else:
                    counter+=1
                #diagrafw ola ta requests pou einai rejected.Meta 8a to paiksw me sundeseis
                a = friend_requests_content(f = i,user_funct = self.profile_callback,usr = App_Usr,reject_funct = self.friend_request_callback)#pernw ws parametro to friend request
                lst.append(a)
            self._main_layout.clear_widgets()
            self._main_layout.add_widget(friend_requests_rv(arr = lst))

        self._main_layout.add_widget(self._epiloges)
        return self._main_layout
    #
    #Gia Friend Request
    #
    #
    #Other user profile callback
    #
    def handle_friend_requests(self,f = FriendRequest()):
        #diaxeirish tou state enos friend request
        #mporw na dw profil allou user
        #yparxei layout to opoio exei tis plhrofories tou friend request
        #oti afora emena mporei na allaksei,mporw na dw profil allou user
        a = Friend_Request_Layout()
        for i in f.friend_request_info_array():
            a.add_widget(BackgroundLabel(text = i))
        #vazw 2 koumpia ena gia na dw allon xrhsth kai ena gia apodoxh,aporripsh h tpt
        #gia allagh state
        b = Epiloges_Button(text = "Change State")
        #b.bind(self.state_change_callback)
        #gia na dw profil tou user
        u = Epiloges_Button(text = "User profile")
        #u.bind(kati pou 8a mou dinei to profil tou allou user)

    #
    #Other user profile callback
    #
if __name__ == '__main__':
    PointerApp().run()

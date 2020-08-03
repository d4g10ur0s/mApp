import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput

class BackgroundColor(Widget):
    pass

class BackgroundLabel(Label, BackgroundColor):
    pass

class lButton(Button):
    pass

class sButton(Button):
    pass

class mGrid(GridLayout):
    lg = ''
    sgn = ''

    def __init__(self,**kwargs):
        super(mGrid,self).__init__(**kwargs)
        self.cols = 2
        #sign in button
        self.sgn = sButton()
        #log in button
        self.lg = lButton()
        self.sgn.bind(on_press=self.SGCallback)
        self.lg.bind(on_press=self.LGCallback)

        self.add_widget(self.sgn)
        self.add_widget(self.lg)

        #to LogIn
    def LGCallback(self, instance, *pos):
        self.remove_widget(self.lg)
        self.remove_widget(self.sgn)
        self.cols = None
        self.rows = 5
###############################################################################
        #username label
        usrname = BackgroundLabel(text='Username', font_size='25dp')
        usrname.background_color=[1,.1,0,.5]
        self.add_widget(usrname)
        #text input for username
        self.lg = None
        self.lg = TextInput(multiline=False)
        self.add_widget(self.lg)
        #Password label
        pssw=BackgroundLabel(text='Password',font_size='25dp')
        pssw.background_color=[1,.1,0,.5]
        self.add_widget(pssw)
        #text input for Password
        self.sgn = TextInput(multiline=False)
        self.add_widget(self.sgn)
        #Confirm Button
        cnfr=Button(text='Confirm',font_size='25dp',background_color=[1,.1,0,.5])
        self.add_widget(cnfr)

        #To SignIn
    def SGCallback(self, instance, *pos):
        self.remove_widget(self.lg)
        self.remove_widget(self.sgn)
        self.cols = None
        self.rows = 7
###############################################################################
        #username label
        usrname = BackgroundLabel(text = 'Username', font_size = '25dp')
        usrname.background_color = [0,.2,1,.7]
        self.add_widget(usrname)
        #text input for username
        self.lg = None
        self.lg = TextInput(multiline = False,cursor_width = '25dp')
        self.add_widget(self.lg)
        #Password Label
        pssw = BackgroundLabel(text = 'Password' , font_size = '25dp')
        pssw.background_color = [0,.2,1,.7]
        self.add_widget(pssw)
        #text input for Password
        self.sgn = None
        self.sgn = TextInput(multiline = False)
        self.add_widget(self.sgn)
        #Password Confirmation
        pssw1 = BackgroundLabel(text = 'Password Confirmation' , font_size = '25dp')
        pssw1.background_color = [0,.2,1,.7]
        self.add_widget(pssw1)
        #text input for confirmation
        psswc = None
        psswc = TextInput(multiline = False)
        self.add_widget(psswc)
        #Confirmation button
        conf = Button(text='Confirm', font_size='25dp', background_color=[0,.1,1,.5])
        self.add_widget(conf)


class katiApp(App):
    def build(self):
        root = mGrid()
        return root



if __name__=="__main__":
    katiApp.run()

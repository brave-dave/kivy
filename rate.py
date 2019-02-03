from kivy.app import App
import requests, re, json

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

from kivy.config import Config
Config.set("graphics", "resizeble", 0)
Config.set("graphics", "width", 400)
Config.set("graphics", "height", 500)

dropdown = DropDown()
dropdown2 = DropDown()

class MainApp(App):
    

    def get_rate(self, instance):
        url = "http://free.currencyconverterapi.com/api/v5/convert?q={}&compact=y".format(self.mainbutton.text + "_" + self.mainbutton2.text)
        get = requests.get(url)
        res = get.json()
        try:
            self.lbl.text = "{} TO {} exchange rate: ".format(self.mainbutton.text, self.mainbutton2.text) + str(round(res[self.mainbutton.text + "_" + self.mainbutton2.text]['val'], 1)) + " " +self.mainbutton2.text
        except KeyError:
            self.lbl.text = "Please Choose Rate Of Which Currencies Do You Want To Get"
        

    def build(self):
        self.title = 'Exchange Rates To AMD'
        bl = BoxLayout(orientation = "vertical")
        bl2 = BoxLayout(orientation = "horizontal")
        gl = GridLayout(cols = 1, spacing = 3)
        gl2 = GridLayout(cols = 2, spacing = 1)
        self.lbl = Label(text="- - - - - - - - -", font_size = 20)
        
        btn_usd = Button(text='USD', size_hint_y=None, height=44)
        btn_usd.bind(on_release=lambda btn: dropdown.select(btn_usd.text))
        btn_eur = Button(text='EUR', size_hint_y=None, height=44)
        btn_eur.bind(on_release=lambda btn: dropdown.select(btn_eur.text))
        btn_rub = Button(text='RUB', size_hint_y=None, height=44)
        btn_rub.bind(on_release=lambda btn: dropdown.select(btn_rub.text))
        btn_uah = Button(text='UAH', size_hint_y=None, height=44)
        btn_uah.bind(on_release=lambda btn: dropdown.select(btn_uah.text))
        btn_amd = Button(text='AMD', size_hint_y=None, height=44)
        btn_amd.bind(on_release=lambda btn: dropdown.select(btn_amd.text))

        dropdown.add_widget(btn_usd)
        dropdown.add_widget(btn_eur)
        dropdown.add_widget(btn_rub)
        dropdown.add_widget(btn_uah)
        dropdown.add_widget(btn_amd)

        btn_usd2 = Button(text='USD', size_hint_y=None, height=44)
        btn_usd2.bind(on_release=lambda btn: dropdown2.select(btn_usd2.text))
        btn_eur2 = Button(text='EUR', size_hint_y=None, height=44)
        btn_eur2.bind(on_release=lambda btn: dropdown2.select(btn_eur2.text))
        btn_rub2 = Button(text='RUB', size_hint_y=None, height=44)
        btn_rub2.bind(on_release=lambda btn: dropdown2.select(btn_rub2.text))
        btn_uah2 = Button(text='UAH', size_hint_y=None, height=44)
        btn_uah2.bind(on_release=lambda btn: dropdown2.select(btn_uah2.text))
        btn_amd2 = Button(text='AMD', size_hint_y=None, height=44)
        btn_amd2.bind(on_release=lambda btn: dropdown2.select(btn_amd2.text))

        dropdown2.add_widget(btn_usd2)
        dropdown2.add_widget(btn_eur2)
        dropdown2.add_widget(btn_rub2)
        dropdown2.add_widget(btn_uah2)
        dropdown2.add_widget(btn_amd2)
        
        self.mainbutton  = Button(text="From", size_hint=(1, .5))
        self.mainbutton2 = Button(text="To", size_hint=(1, .5))

        self.mainbutton.bind(on_release=dropdown.open)
        self.mainbutton2.bind(on_release=dropdown2.open)

        dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))
        dropdown2.bind(on_select=lambda instance, x: setattr(self.mainbutton2, 'text', x))

        """
        bl.add_widget(self.lbl)
        bl.add_widget( Button(text="Get Rate", on_press=self.get_rate) )
        bl2.add_widget(self.mainbutton)
        bl2.add_widget(self.mainbutton2)
        bl.add_widget(bl2)
        return bl
        """
        gl.add_widget(self.lbl)
        gl2.add_widget(self.mainbutton)
        gl2.add_widget(self.mainbutton2)
        gl.add_widget(gl2)
        gl.add_widget( Button(text="Get Rate", on_press=self.get_rate, size_hint=(.4, .5)) )
        return gl


if __name__ == "__main__":
    MainApp().run()
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


from kivy.core.window import Window

dollar = "https://www.google.com/search?client=opera&hs=cx&sxsrf=ALeKk00xmBUn-WeeMLREkRgQ8Ux0QV5FNA%3A1609854665821&ei=yW70X6vYMcfJrgSM6Ro&q=доллар+в+гривнах&oq=доллар&gs_lcp=CgZwc3ktYWIQAxgAMgkIIxAnEEYQggIyBAgjECcyBAgjECcyBwgAELEDEEMyBwgAELEDEEMyBwgAELEDEEMyBQgAELEDMgUILhCxAzIFCAAQsQMyAggAOggILhCxAxCDAToICAAQsQMQgwE6BwguEEMQkwI6CggAEMcBEK8BEEM6BAgAEEM6CwgAELEDEMcBEKMCOgIILjoICAAQxwEQrwFQ9pdeWPWdXmClpF5oAHABeACAAcQBiAGHBpIBAzEuNZgBAKABAaoBB2d3cy13aXrAAQE&sclient=psy-ab"
euro = "https://www.google.com/search?client=opera&sxsrf=ALeKk000P25KZ_zracRq33Gfcbt1XjYTlw%3A1609856211288&ei=03T0X_KHEbKrrgTCg5m4Cg&q=евро+в+гривнах&oq=tdhj&gs_lcp=CgZwc3ktYWIQAxgAMgcIIxCxAhAnMgcIIxCxAhAnMgcIIxCxAhAnMgoIABCxAxCDARBDMgcIABCxAxBDMgQIABBDMgQIABBDMgQIABBDMgcIABCxAxBDMgQIABBDOgQIIxAnOggIABCxAxCDAToFCAAQsQM6AggAOggIABAKEAEQKjoMCAAQxwEQrwEQChABOgYIABAKEAFQ5dIFWIbWBWDW3QVoAHABeACAAY4BiAHxA5IBAzAuNJgBAKABAaoBB2d3cy13aXrAAQE&sclient=psy-ab"

headers = { "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.400" }


Window.size = ( 550, 500 )
Window.clearcolor = (155/255, 186/255, 3/255, 1)
Window.title = "Конвертер"


class MyApp(App):

	def __init__(self):
		super().__init__()
		self.label = Label(text="Конвертер")
		self.dollars = Label(text="Доллар")
		self.euros = Label(text="Евро")
		self.bitcoins = Label(text="Биткоин")
		self.input_data = TextInput(hint_text="Введите значение (грн)", multiline=False)
		self.input_data.bind(text=self.on_text)

	def on_text(self, *args):
		data = self.input_data.text
		if data.isnumeric():
			self.dollars.text = "Доллары " + str(float(data) / 1)
			self.euros.text = "Евро " + str(float(data) / 1)
			self.bitcoins.text = "Биткоины " + str(float(data) / 1)
		else:
			self.input_data.text = ""

	def build(self):
		box = BoxLayout(orientation="vertical")
		box.add_widget(self.label)
		box.add_widget(self.input_data)
		box.add_widget(self.dollars)
		box.add_widget(self.euros)
		box.add_widget(self.bitcoins)

		return box



if __name__ == "__main__":
	MyApp().run()
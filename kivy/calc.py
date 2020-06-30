from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config
Config.set('graphics','resizable',0)				
Config.set('graphics','width',400)
Config.set('graphics','height',500)	

class CalcApp(App):
	def update_label(self):
		self.lbl.text = self.lbl_text

	def add_numb(self, instance):
		if self.lbl_text != '0':
			self.lbl_text == ''
			self.lbl_text += str(instance.text)
		elif self.lbl_text == '0':
			self.lbl_text == '0'
			self.lbl_text += str(instance.text)
		# print(self.lbl_text)
		self.update_label()

	def operation(self,instance):
		if str(instance.text).lower() == 'x':
			self.lbl_text+='*'
		else:
			self.lbl_text+=str(instance.text)
		self.update_label()

	def result(self, instance):
		self.lbl.text = str(eval(self.lbl.text))
		self.lbl_text = '0'
	def build(self):
		
		self.lbl = Label(text='0',font_size=40,size_hint=(1,.4),halign ='right',valign = "center",text_size =(400 - 30, 500 * .4 - 30))
		self.lbl_text = '0'

		bl = BoxLayout(orientation='vertical',padding=15)
		gl = GridLayout(cols =4, spacing=2,size_hint=(1,.6))

		bl.add_widget(self.lbl)

		gl.add_widget(Button(text='7',on_press = self.add_numb))
		gl.add_widget(Button(text='8',on_press = self.add_numb))
		gl.add_widget(Button(text='9',on_press = self.add_numb))
		gl.add_widget(Button(text='x', on_press = self.operation))

		gl.add_widget(Button(text='4',on_press = self.add_numb))
		gl.add_widget(Button(text='5',on_press = self.add_numb))
		gl.add_widget(Button(text='6',on_press = self.add_numb))
		gl.add_widget(Button(text='-', on_press = self.operation))

		gl.add_widget(Button(text='1',on_press = self.add_numb))
		gl.add_widget(Button(text='2',on_press = self.add_numb))
		gl.add_widget(Button(text='3',on_press = self.add_numb))
		gl.add_widget(Button(text='+', on_press = self.operation))

		gl.add_widget(Widget())
		gl.add_widget(Button(text='0',on_press = self.add_numb))
		gl.add_widget(Button(text='.',on_press = self.add_numb))
		gl.add_widget(Button(text='=',on_press = self.result))
		
		bl.add_widget(gl)

		return bl


if __name__== '__main__':
	CalcApp().run()
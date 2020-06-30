from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.scatter import Scatter

from kivy.config import Config
Config.set('graphics','resizable',0)				
Config.set('graphics','width',540)
Config.set('graphics','height',480)				

class MyApp(App):		
	def build(self):
# Scatter - чтобы изменять размер и плоложение двумя палцьами!
		# s = Scatter()
	#FloatLayout  - виджет который заполняет все окно, в него поместили кнопку
		fl = FloatLayout(size = (300, 300))
		# s.add_widget(fl)
		fl.add_widget(Button(text='Моя первая кнопка!', 	
        	on_press = self.btn_press,
        	background_normal = '',
        	background_color = [.64,.6,.78,1],
        	size_hint = (.3,.15),
        	pos = (540/2 - (540 *.3 / 2), 480/2 - (480 *.15 / 2))))
# Вторая кнопка, как вывести обе?
		# fl1 = FloatLayout(size = (150,150))
		fl.add_widget(Button(text = 'Вторая кнопка',
			on_press = self.btn_press,
			background_color = [1,0,0,1],
			size_hint = (.5,.25),
			pos = (540/3 - (540*.5 / 2),480/3 - (480*.25 / 2))))
		return fl

	def btn_press(self,instance):
		print(f'Вы нажали кнопку')
		instance.text = 'я уже нажата' 				

if __name__ == "__main__":
	MyApp().run()


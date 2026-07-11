from kivy.app import App
from kivy.uix.label import Label

class AutoBrainApp(App):
    def build(self):
        return Label(text='Automated Build Successful!', font_size='24sp')

if __name__ == '__main__':
    AutoBrainApp().run()

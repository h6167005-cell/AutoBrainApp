from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.camera import Camera

class ScannerUI(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        self.camera = Camera(play=True, resolution=(640, 480))
        self.layout.add_widget(self.camera)
        
        self.status_label = Label(text="Auto Brain: Camera Ready.", size_hint_y=0.1)
        self.layout.add_widget(self.status_label)
        
        self.scan_btn = Button(text="[ SCAN DOCUMENT ]", size_hint_y=0.2, background_color=(0, 1, 0, 1))
        self.scan_btn.bind(on_press=self.capture_and_scan)
        self.layout.add_widget(self.scan_btn)
        
        return self.layout

    def capture_and_scan(self, instance):
        self.status_label.text = "Processing image with OpenCV..."
        print("Camera button pressed! Ready for math engine.")

if __name__ == '__main__':
    ScannerUI().run()

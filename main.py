from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.camera import Camera

class ScannerUI(App):
    def build(self):
        # Create a vertical layout
        self.layout = BoxLayout(orientation='vertical')
        
        # Add the live camera feed
        self.camera = Camera(play=True, resolution=(640, 480))
        self.layout.add_widget(self.camera)
        
        # Add the status label
        self.status_label = Label(text="Auto Brain: Camera Ready.", size_hint_y=0.1)
        self.layout.add_widget(self.status_label)
        
        # Add the Scan Button
        self.scan_btn = Button(text="[ SCAN DOCUMENT ]", size_hint_y=0.2, background_color=(0, 1, 0, 1))
        self.scan_btn.bind(on_press=self.capture_and_scan)
        self.layout.add_widget(self.scan_btn)
        
        return self.layout

    def capture_and_scan(self, instance):
        # This is where the OpenCV logic will execute
        self.status_label.text = "Processing image with OpenCV..."
        print("Camera button pressed! Ready for math engine.")

if __name__ == '__main__':
    ScannerUI().run()

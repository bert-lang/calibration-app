from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.label = Label(
            text="Calibration App\nAPK Build Successful!",
            font_size=24
        )

        self.button = Button(
            text="Click Me",
            size_hint=(1, 0.3)
        )
        self.button.bind(on_press=self.on_button_press)

        self.add_widget(self.label)
        self.add_widget(self.button)

    def on_button_press(self, instance):
        self.label.text = "Button Clicked!"


class CalibrationApp(App):
    def build(self):
        return MainLayout()


if __name__ == "__main__":
    CalibrationApp().run()
    

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp

from calibration import calculate_calibration


class CalibrationApp(App):
    def build(self):
        root = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10
        )

        # Inputs
        self.diameter = TextInput(
            hint_text="Tank Diameter",
            multiline=False,
            size_hint_y=None,
            height=dp(40)
        )
        self.length = TextInput(
            hint_text="Tank Length",
            multiline=False,
            size_hint_y=None,
            height=dp(40)
        )
        self.step = TextInput(
            hint_text="Liter Step",
            multiline=False,
            size_hint_y=None,
            height=dp(40)
        )
        self.unit = TextInput(
            hint_text="Unit (mm / cm / m)",
            multiline=False,
            size_hint_y=None,
            height=dp(40)
        )

        for widget in [self.diameter, self.length, self.step, self.unit]:
            root.add_widget(widget)

        # Button
        btn = Button(
            text="CALCULATE",
            size_hint_y=None,
            height=dp(45)
        )
        btn.bind(on_press=self.calculate)
        root.add_widget(btn)

        # Output
        self.output = Label(
            text="Result will appear here",
            halign="left",
            valign="top",
            size_hint_y=None,
            font_size=16
        )
        self.output.bind(texture_size=self.output.setter("size"))

        scroll = ScrollView()
        scroll.add_widget(self.output)
        root.add_widget(scroll)

        return root

    def calculate(self, instance):
        try:
            d = float(self.diameter.text)
            l = float(self.length.text)
            step = float(self.step.text)
            unit = self.unit.text.lower()

            table, max_vol = calculate_calibration(d, l, step, unit)

            text = f"VOLUME (L)    LEVEL ({unit.upper()})\n"
            text += "-" * 32 + "\n"

            for vol, height in table:
                text += f"{vol:>10.2f}   {height:>10.2f}\n"

            text += f"\nFULL VOLUME ≈ {max_vol} L"
            self.output.text = text

        except Exception as e:
            self.output.text = str(e)


if __name__ == "__main__":
    CalibrationApp().run()
  

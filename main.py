import math
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp

class CalibrationApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=12, spacing=12)

        # ===== TITLE =====
        title = Label(
            text="CALIBRATION CALCULATOR",
            size_hint_y=None,
            height=dp(40),
            font_size=22,
            bold=True
        )
        root.add_widget(title)

        # ===== INPUT SECTION =====
        input_box = BoxLayout(
            orientation='vertical',
            spacing=8,
            size_hint_y=None
        )
        input_box.bind(minimum_height=input_box.setter('height'))

        def small_input(hint):
            return TextInput(
                hint_text=hint,
                multiline=False,
                size_hint_y=None,
                height=dp(42),
                font_size=16
            )

        self.d_input = small_input("Tank Diameter")
        self.l_input = small_input("Tank Length")
        self.step_input = small_input("Liter Step")
        self.unit_input = small_input("Unit (mm / cm / m)")

        input_box.add_widget(self.d_input)
        input_box.add_widget(self.l_input)
        input_box.add_widget(self.step_input)
        input_box.add_widget(self.unit_input)

        root.add_widget(input_box)

        # ===== BUTTON =====
        btn = Button(
            text="CALCULATE",
            size_hint_y=None,
            height=dp(48),
            font_size=18
        )
        btn.bind(on_press=self.calculate)
        root.add_widget(btn)

        # ===== RESULT TITLE =====
        result_title = Label(
            text="Calibration Result",
            size_hint_y=None,
            height=dp(30),
            font_size=18,
            bold=True
        )
        root.add_widget(result_title)

        # ===== OUTPUT (BIG & READABLE) =====
        self.output = Label(
            text="Result will appear here",
            font_size=26,        # BIG TEXT
            size_hint_y=None,
            halign="left",
            valign="top"
        )
        self.output.bind(
            texture_size=lambda inst, val: setattr(inst, 'size', val)
        )

        scroll = ScrollView()
        scroll.add_widget(self.output)
        root.add_widget(scroll)

        return root

    def calculate(self, instance):
        try:
            D = float(self.d_input.text)
            L = float(self.l_input.text)
            liter_step = float(self.step_input.text)
            unit = self.unit_input.text.lower()

            if unit == "mm":
                liter_factor = 1_000_000
            elif unit == "cm":
                liter_factor = 1_000
            else:
                liter_factor = 0.001

            h_step = 0.0001
            R = D / 2
            max_volume_liters = math.pi * R * R * L / liter_factor

            def volume_from_height(h):
                if h <= 0:
                    return 0.0
                if h >= D:
                    return math.pi * R * R * L
                area = (R**2 * math.acos((R - h) / R)
                        - (R - h) * math.sqrt(2 * R * h - h**2))
                return area * L

            result = "VOLUME (L)     LEVEL ({})\n".format(unit.upper())
            result += "---------------------------\n"

            target_liters = liter_step
            h = 0.0

            while target_liters <= max_volume_liters:
                while h <= D:
                    vol_liters = volume_from_height(h) / liter_factor
                    if vol_liters >= target_liters:
                        result += "{:>10.2f}   {:>10.2f}\n".format(
                            target_liters, h
                        )
                        break
                    h += h_step
                target_liters += liter_step

            result += "\nFULL VOLUME ≈ {:.2f} L".format(max_volume_liters)

            self.output.text = result

        except Exception as e:
            self.output.text = str(e)

CalibrationApp().run()

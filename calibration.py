import math

def calculate_calibration(diameter, length, liter_step, unit):
    # Unit conversion to liters
    if unit == "mm":
        factor = 1_000_000
    elif unit == "cm":
        factor = 1_000
    else:
        factor = 0.001  # meters

    radius = diameter / 2
    max_volume = math.pi * radius * radius * length / factor
    h_step = diameter / 10000  # adaptive step (fast & accurate)

    def volume_from_height(h):
        if h <= 0:
            return 0.0
        if h >= diameter:
            return math.pi * radius * radius * length / factor

        area = (
            radius**2 * math.acos((radius - h) / radius)
            - (radius - h) * math.sqrt(2 * radius * h - h**2)
        )
        return (area * length) / factor

    table = []
    target_volume = liter_step
    h = 0.0

    while target_volume <= max_volume:
        while h <= diameter:
            if volume_from_height(h) >= target_volume:
                table.append((round(target_volume, 2), round(h, 2)))
                break
            h += h_step
        target_volume += liter_step

    return table, round(max_volume, 2)
  

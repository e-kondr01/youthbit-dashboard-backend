import math


def rgb_to_hex(rgb):
    return "#" + "%02x%02x%02x" % rgb


def number_to_hex(mag, cmin, cmax):
    """Return a tuple of floats between 0 and 1 for R, G, and B."""
    # Normalize to 0-1
    try:
        x = float(mag - cmin) / (cmax - cmin)
    except ZeroDivisionError:
        x = 0.5  # cmax == cmin
    blue = min((max((4 * (0.75 - x), 0.0)), 1.0))
    red = min((max((4 * (x - 0.25), 0.0)), 1.0))
    green = min((max((4 * math.fabs(x - 0.5) - 1.0, 0.0)), 1.0))
    return rgb_to_hex((int(red * 255), int(green * 255), int(blue * 255)))

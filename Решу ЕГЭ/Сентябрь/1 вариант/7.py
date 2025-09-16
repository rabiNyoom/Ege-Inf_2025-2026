FILE_SIZE = 12 # MB

OLD_DPI = 600
NEW_DPI = 300

OLD_COLOR_POWER = 24
NEW_COLOR_POWER = 16

color_diff = NEW_COLOR_POWER / OLD_COLOR_POWER
dpi_diff = (NEW_DPI ** 2) / (OLD_DPI ** 2)

print(FILE_SIZE * dpi_diff * color_diff)

# 2
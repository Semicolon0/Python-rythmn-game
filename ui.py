import pygame as pyg

#colors
color1 = (128, 60, 0)
color2 = (38, 128, 0)
color3 = (0, 0, 128)
color4 = (128, 0, 127)
color5 = (128, 0, 0)
color6 = (0, 128, 123)

def draw_triggerboxes():
    import main
    colors = [color1, color2, color3, color4, color5, color6]
    for color in colors:
        index = colors.index(color)
        divisor = index + 1 if index != 0 else 1
        pyg.draw.rect(main.screen, color, pyg.Rect(main.x / 6 * divisor - main.x / 6, main.y / 6 * 5, main.x / 6, main.y / 6))
        pyg.draw.line(main.screen, (28, 28, 28), ( main.x / 6 * divisor, 0), ( main.x / 6 * divisor, main.y), width=1)

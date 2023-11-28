import pygame as pyg

x_pos = 0
moving_right = True

def test_block(screen, x, y):
    global x_pos
    global moving_right
    if x_pos == x-50:
        moving_right = False
    elif x_pos == 0:
        moving_right = True
        
    if moving_right:
        x_pos += 1
    else:
        x_pos -= 1
        
    pyg.draw.rect(screen, (255, 255, 255), pyg.Rect(x_pos, y // 2, 50, 50))

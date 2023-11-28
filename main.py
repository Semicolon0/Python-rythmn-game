import pygame as pyg
import random as rnd
import ui
import input
import running_visual as rv
import notes
import test_map as tm

background_color = (0, 0, 0)  # Fix background color

screen = pyg.display.set_mode((500, 500), vsync=1)
surface = pyg.Surface((500, 500), pyg.SRCALPHA)
pyg.display.set_caption('Buh guh')

x, y = size = surface.get_width(), surface.get_height()
clock = pyg.time.Clock()
game_time = pyg.time.get_ticks()

note = notes.Note(2, rnd.randint(1,6), 0, True, (255, 255, 255))

running = True

while running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False
            
    input.handle_input_actions()
    
    #input timers
    input.q_timer()
    input.w_timer()
    input.e_timer()          
    input.r_timer()
    input.t_timer()
    input.y_timer()
    
    #other
    note.note_color()
    input.note_info(note.y_pos)
    # Update and draw section start
    
    ui.draw_triggerboxes()
    rv.test_block(screen, x, y)
    game_time = pyg.time.get_ticks()
    tm.test_map(game_time)
    # Update and draw section end
    
    pyg.display.flip()
    screen.fill(background_color)
    
    clock.tick(60)
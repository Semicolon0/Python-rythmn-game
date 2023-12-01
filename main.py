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

tm.play_song()

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
    # Update and draw section start
    
    ui.draw_triggerboxes()
    rv.test_block(screen, x, y)
    game_time = pyg.time.get_ticks()
    tm.test_map(game_time)
    for note in tm.notes_list:
        note.note_color()
        note.draw_note(screen,x,y)
        if note.y_pos > 500:
            tm.notes_list.remove(note)
    # Update and draw section end
    
    pyg.display.flip()
    screen.fill(background_color)
    
    clock.tick(60)
import pygame as pyg
import ui
import notes
import test_map as tm

# Initialize key state dictionary
key_state = {pyg.K_q: False, pyg.K_w: False, pyg.K_e: False, pyg.K_r: False, pyg.K_t: False, pyg.K_y: False}


q_active = False
q_time = 0

w_active = False
w_time = 0

e_active = False
e_time = 0

r_active = False
r_time = 0

t_active = False
t_time = 0

y_active = False
y_active = 0


light_up_time = 150

def note_info(y_pos):
    global note
    import main
    note = main.note

def get_input():
    keys = pyg.key.get_pressed()
    return keys

#multiple timers cause' I can't think of anything better atm, it works though and I don't really experiece slowdown

def q_timer():
    global q_active, q_time, light_up_time  # Move the global declaration to the beginning
    if q_active:
        import main
        if main.game_time >= q_time + light_up_time:
            ui.color1 = (128, 60, 0)
            q_active = False
            
def w_timer():
    global w_active, w_time, light_up_time
    if w_active:
        import main
        if main.game_time >= w_time + light_up_time:
            ui.color2 = (38, 128, 0)
            w_active = False

def e_timer():
    global e_active, e_time, light_up_time
    if e_active:
        import main
        if main.game_time >= e_time + light_up_time:
            ui.color3 = (0, 0, 128)
            e_active = False

def r_timer():
    global r_active, r_time, light_up_time
    if r_active:
        import main
        if main.game_time >= r_time + light_up_time:
            ui.color4 = (128, 0, 127)
            r_active = False
            
            
def t_timer():
    global t_active, t_time, light_up_time
    if t_active:
        import main
        if main.game_time >= t_time + light_up_time:
            ui.color5 = (128, 0, 0)
            t_active = False

def y_timer():
    global y_active, y_time, light_up_time
    if y_active:
        import main
        if main.game_time >= y_time + light_up_time:
            ui.color6 = (0, 128, 123)
            y_active = False


def handle_input_actions():
    global key_state, q_active, q_time, w_active, w_time, e_active, e_time, r_active, r_time, t_active, t_time, y_active, y_time # Add q_active and q_time to the global statement

    keys = get_input()
    #------- K -------#
    if keys[pyg.K_q] and not key_state[pyg.K_q]:
        key_state[pyg.K_q] = True
        ui.color1 = (255, 119, 0)
        for note in tm.notes_list:
            note.note_hit(1, note.y_pos, note)
        import main
        q_active = True
        q_time = main.game_time

    elif not keys[pyg.K_q]:
        key_state[pyg.K_q] = False


    #------- W -------#
    if keys[pyg.K_w] and not key_state[pyg.K_w]:
        key_state[pyg.K_w] = True
        ui.color2 = (77, 255, 0)
        for note in tm.notes_list:
            note.note_hit(2, note.y_pos, note)
        import main
        w_active = True
        w_time = main.game_time
        # Your additional actions for 'w' key press go here

    elif not keys[pyg.K_w]:
        key_state[pyg.K_w] = False


    #------- E -------#
    if keys[pyg.K_e] and not key_state[pyg.K_e]:
        key_state[pyg.K_e] = True
        ui.color3 = (0, 0, 255)
        for note in tm.notes_list:
            note.note_hit(3, note.y_pos, note)
        import main
        e_active = True
        e_time = main.game_time
        
        # Your additional actions for 'e' key press go here

    elif not keys[pyg.K_e]:
        key_state[pyg.K_e] = False


    #------- R -------#
    if keys[pyg.K_r] and not key_state[pyg.K_r]:
        key_state[pyg.K_r] = True
        ui.color4 = (255, 0, 255)
        for note in tm.notes_list:
            note.note_hit(4, note.y_pos, note)
        import main
        r_active = True
        r_time = main.game_time
        
        # Your additional actions for 'r' key press go here

    elif not keys[pyg.K_r]:
        key_state[pyg.K_r] = False


    #------- T -------#
    if keys[pyg.K_t] and not key_state[pyg.K_t]:
        key_state[pyg.K_t] = True
        ui.color5 = (255, 0, 0)
        for note in tm.notes_list:
            note.note_hit(5, note.y_pos, note)
        import main
        t_active = True
        t_time = main.game_time
        
        # Your additional actions for 't' key press go here

    elif not keys[pyg.K_t]:
        key_state[pyg.K_t] = False


    #------- Y -------#
    if keys[pyg.K_y] and not key_state[pyg.K_y]:
        key_state[pyg.K_y] = True
        ui.color6 = (0, 255, 246)
        for note in tm.notes_list:
            note.note_hit(6, note.y_pos, note)
        import main
        y_active = True
        y_time = main.game_time
        
        # Your additional actions for 'y' key press go here

    elif not keys[pyg.K_y]:
        key_state[pyg.K_y] = False

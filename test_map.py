from pygame import mixer
import notes

notes_list = list()
speed = 20

def play_song():
    mixer.init()
    mixer.music.load("Playing God.mp3")
    mixer.music.set_volume(1)
    mixer.music.play()
    
    
def note1():
    global notes_list,speed
    notes_list.append(notes.Note(speed, 1, 0, True, (255, 255, 255)))

def note2():
    # Define the action for this case
    global notes_list, speed
    notes_list.append(notes.Note(speed,2,0,True, (255, 255, 255)))
    
def note3():
    global notes_list,speed
    notes_list.append(notes.Note(speed,3,0,True, (255)))
    
def note4():
    global notes_list, speed
    notes_list.append(notes.Note(speed,4,0,True,(255)))
    
def note5():
    global notes_list, speed
    notes_list.append(notes.Note(speed,5,0,True,(255)))
    
def note6():
    global notes_list, speed
    notes_list.append(notes.Note(speed,6,0,True,(255)))
# Create a dictionary mapping cases to functions

case_functions = {
    range(1490, 1510): [note1, note2],
    range(1690, 1710): note4,
    range(1890, 1910): note3,
    range(2090, 2110): note6,
    range(2290, 2310): note5,
    range(2490, 2510): note4,
    range(2690, 2710): note5,
    range(2890, 2910): [note5, note1],
    range(3090, 3110): note1,
    
    # Add more cases as needed
}

def test_map(time):
    for case_range, case_function in case_functions.items():
        if time in case_range:
            if isinstance(case_function, list):
                for func in case_function:
                    func()
            else:
                case_function()
            break
    else:
        # Default case, do nothing
        pass

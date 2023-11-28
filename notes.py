import pygame as pyg


class Note:
    
    def __init__(self, speed, lane, y_pos, draw, color):
        self.speed = speed
        self.lane = lane
        self.y_pos = y_pos
        self.draw = True
        self.color = color

    def note_color(self):
        match self.lane:
            case 1:
                self.color = (255, 119, 0)
        
            case 2:
                self.color = (77, 255, 0)
            
            case 3:
                self.color = (0, 0, 255)
            
            case 4:
                self.color = (255, 0, 255)
            
            case 5:
                self.color = (255, 0, 0)
            
            case 6:
                self.color = (0, 255, 246)
            

    def draw_note(self,screen, x, y):
        if self.draw:
            self.x_pos = x / 6 * self.lane - x / 6
            self.y_pos += self.speed
            
            if self.y_pos > 500:
                self.draw = False

            pyg.draw.rect(screen, self.color, pyg.Rect(self.x_pos + 15, self.y_pos, x / 6 - 30, y / 6 / 2))

      
    def note_hit(self,input_lane, y_pos):
        import main
        if self.lane == input_lane and self.y_pos + main.y / 6 / 2 > main.y / 6 * 5:
            self.draw = False
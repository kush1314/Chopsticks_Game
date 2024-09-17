import pygame
import os
import sys
import players1
#orginally set to 950, 500
WIDTH, HEIGHT = 1100, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chopsticks Game")
WHITE = (255,255,255)
BLACK = (0, 0, 0)
BLUE = WHITE
FPS = 30
pygame.init()
font = pygame.font.SysFont(None, 35)
font1 = pygame.font.SysFont(None, 25)

def draw_text(text, x, y, text_col):
    img = font.render(text, True, text_col)
    WIN.blit(img, (x, y))
def draw_text1(text, x, y, text_col):
    img = font1.render(text, True, text_col)
    WIN.blit(img, (x, y))


def draw_window():
    WIN.fill(BLUE)

    pygame.display.update()

def draw_something():
    #hand on the left
    color_rect = (0,0,0)
    
    x = 155
    y = 404
    for i in range(0, 21): #bottom of the hand
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x -= 5
    x = 155
    y = 404
    for i in range(0, 29): # right side of hand(bottom)
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x += 1.1
        y-= 2
    pygame.draw.rect(WIN, color_rect, (185, 340, 9, 9)) # right side combining piece

    x = 184.5
    y = 335
    for i in range(0, 20):#right side of hand(top of it)
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x -= 1
        y-= 2

    x = 160
    y = 295.5

    for i in range(0, 5): #top right diagnol
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x -= 2
    x = 143
    y = 280
    for i in range(0, 20): #straight down thumb line
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        y += 2
    pygame.draw.rect(WIN, color_rect, (142, 273, 8, 9)) #idk

    x = 50
    y = 400
    for i in range(0, 20): #bottom left part
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x -= 0.7
        y-= 2

    x = 35
    y = 354
    for i in range(0, 26): #top left part
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x -= 0.1
        y-= 2

    x = 32
    y= 296
    for i in range(0, 6):
        pygame.draw.rect(WIN, color_rect, (x, y, 10, 9))
        x +=1
        y -=1
    


    pygame.draw.rect(WIN, color_rect, (47, 292, 10, 9))
    pygame.draw.rect(WIN, color_rect, (49, 293, 10, 9))
    pygame.draw.rect(WIN, color_rect, (51, 293, 10, 9))
    pygame.draw.rect(WIN, color_rect, (53, 294, 10, 9))
    pygame.draw.rect(WIN, color_rect, (53, 294, 10, 9))
    pygame.draw.rect(WIN, color_rect, (55, 294, 10, 9))
    pygame.draw.rect(WIN, color_rect, (57, 294, 10, 9))

    x = 58.6
    y = 294
    for i in range(0, 2):
        pygame.draw.rect(WIN, color_rect, (x, y, 10, 9))
        y +=2

    pygame.draw.rect(WIN, color_rect, (58.6, 302, 10, 9))
    pygame.draw.rect(WIN, color_rect, (58.6, 290, 10, 9))
    pygame.draw.rect(WIN, color_rect, (58.6, 288, 10, 9))

    x = 59
    y = 286
    for i in range(0, 3):
        pygame.draw.rect(WIN, color_rect, (x, y, 10, 9))
        x +=2
        y -=2

   
    pygame.draw.rect(WIN, color_rect, (67, 278.8, 10, 9))
    pygame.draw.rect(WIN, color_rect, (69, 278, 10, 9))
    pygame.draw.rect(WIN, color_rect, (71, 280, 10, 9))
    pygame.draw.rect(WIN, color_rect, (73, 278, 10, 9))
    pygame.draw.rect(WIN, color_rect, (75, 280, 10, 9))

    x = 77
    y = 280
    for i in range(0, 2):
        pygame.draw.rect(WIN, color_rect, (x, y, 10, 9))
        x +=2
        y +=1

  
    pygame.draw.rect(WIN, color_rect, (84, 284, 10, 9))
    pygame.draw.rect(WIN, color_rect, (86, 290, 10, 9))
    pygame.draw.rect(WIN, color_rect, (87, 290, 10, 9))
    pygame.draw.rect(WIN, color_rect, (87, 295, 10, 9))

    x = 87
    y = 287
    for i in range(0, 3):
        pygame.draw.rect(WIN, color_rect, (x, y, 10, 9))
        y -=2
    

    pygame.draw.rect(WIN, color_rect, (900, 270, 9, 7))
    pygame.draw.rect(WIN, color_rect, (87, 279, 9, 9))
    pygame.draw.rect(WIN, color_rect, (88, 279, 9, 9))
    pygame.draw.rect(WIN, color_rect, (88, 277, 9, 9))
    pygame.draw.rect(WIN, color_rect, (88, 275, 9, 9))
    pygame.draw.rect(WIN, color_rect, (89, 273, 9, 9))
    pygame.draw.rect(WIN, color_rect, (91, 271, 9, 9))
    pygame.draw.rect(WIN, color_rect, (92, 270, 9, 9))
    pygame.draw.rect(WIN, color_rect, (94, 269, 9, 9))
    pygame.draw.rect(WIN, color_rect, (95, 268, 9, 9))
    pygame.draw.rect(WIN, color_rect, (96, 268, 9, 9))
    pygame.draw.rect(WIN, color_rect, (98, 268, 9, 9))
    pygame.draw.rect(WIN, color_rect, (100, 268, 9, 9))
    pygame.draw.rect(WIN, color_rect, (103, 268, 9, 9))
    pygame.draw.rect(WIN, color_rect, (110, 269, 5, 9))
    pygame.draw.rect(WIN, color_rect, (112, 271, 5, 9))
    pygame.draw.rect(WIN, color_rect, (114, 273, 5, 9))
    pygame.draw.rect(WIN, color_rect, (116, 275, 5, 9))
    pygame.draw.rect(WIN, color_rect, (118, 277, 5, 9))
    pygame.draw.rect(WIN, color_rect, (114, 279, 9, 9))
    pygame.draw.rect(WIN, color_rect, (115, 282, 9, 9))
    pygame.draw.rect(WIN, color_rect, (115, 285, 9, 9))
    pygame.draw.rect(WIN, color_rect, (115, 288, 9, 9))
    pygame.draw.rect(WIN, color_rect, (116, 274, 9, 9))
    pygame.draw.rect(WIN, color_rect, (121, 272, 5, 9))

    pygame.draw.rect(WIN, color_rect, (125, 270, 9, 9))
    pygame.draw.rect(WIN, color_rect, (130, 270, 9, 9))
    pygame.draw.rect(WIN, color_rect, (137, 272, 9, 9))
    pygame.draw.rect(WIN, color_rect, (139, 272, 9, 9))

    #the other hand again thumb towards inside on the right side of the screen
    x = 155 + 600
    y = 404
    for i in range(0, 21):  # bottom of the hand
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x -= 5
    x = 155 + 600
    y = 404
    for i in range(0, 29):  # right side of hand (bottom)
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x += 1.1
        y -= 2
    pygame.draw.rect(WIN, color_rect, (185 + 600, 340, 9, 9))  # right side combining piece

    x = 184.5 + 600
    y = 335
    for i in range(0, 20):  # right side of hand (top of it)
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x -= 1
        y -= 2

    x = 160 + 600
    y = 295.5
    for i in range(0, 5):  # top right diagonal
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x -= 2
    x = 143 + 600
    y = 280
    for i in range(0, 20):  # straight down thumb line
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        y += 2
    pygame.draw.rect(WIN, color_rect, (142 + 600, 273, 8, 9))  # idk

    x = 50 + 600
    y = 400
    for i in range(0, 20):  # bottom left part
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x -= 0.7
        y -= 2

    x = 35 + 600
    y = 354
    for i in range(0, 26):  # top left part
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x -= 0.1
        y -= 2

    x = 32 + 600
    y = 296
    for i in range(0, 6):
        pygame.draw.rect(WIN, color_rect, (x, y, 10, 9))
        x += 1
        y -= 1

    pygame.draw.rect(WIN, color_rect, (47 + 600, 292, 10, 9))
    pygame.draw.rect(WIN, color_rect, (49 + 600, 293, 10, 9))
    pygame.draw.rect(WIN, color_rect, (51 + 600, 293, 10, 9))
    pygame.draw.rect(WIN, color_rect, (53 + 600, 294, 10, 9))
    pygame.draw.rect(WIN, color_rect, (53 + 600, 294, 10, 9))
    pygame.draw.rect(WIN, color_rect, (55 + 600, 294, 10, 9))
    pygame.draw.rect(WIN, color_rect, (57 + 600, 294, 10, 9))

    x = 58.6 + 600
    y = 294
    for i in range(0, 2):
        pygame.draw.rect(WIN, color_rect, (x, y, 10, 9))
        y += 2

    pygame.draw.rect(WIN, color_rect, (58.6 + 600, 302, 10, 9))
    pygame.draw.rect(WIN, color_rect, (58.6 + 600, 290, 10, 9))
    pygame.draw.rect(WIN, color_rect, (58.6 + 600, 288, 10, 9))

    x = 59 + 600
    y = 286
    for i in range(0, 3):
        pygame.draw.rect(WIN, color_rect, (x, y, 10, 9))
        x += 2
        y -= 2

    pygame.draw.rect(WIN, color_rect, (67 + 600, 278.8, 10, 9))
    pygame.draw.rect(WIN, color_rect, (69 + 600, 278, 10, 9))
    pygame.draw.rect(WIN, color_rect, (71 + 600, 280, 10, 9))
    pygame.draw.rect(WIN, color_rect, (73 + 600, 278, 10, 9))
    pygame.draw.rect(WIN, color_rect, (75 + 600, 280, 10, 9))

    x = 77 + 600
    y = 280
    for i in range(0, 2):
        pygame.draw.rect(WIN, color_rect, (x, y, 10, 9))
        x += 2
        y += 1

    pygame.draw.rect(WIN, color_rect, (84 + 600, 284, 10, 9))
    pygame.draw.rect(WIN, color_rect, (86 + 600, 290, 10, 9))
    pygame.draw.rect(WIN, color_rect, (87 + 600, 290, 10, 9))
    pygame.draw.rect(WIN, color_rect, (87 + 600, 295, 10, 9))

    x = 87 + 600
    y = 287
    for i in range(0, 3):
        pygame.draw.rect(WIN, color_rect, (x, y, 10, 9))
        y -= 2

    pygame.draw.rect(WIN, color_rect, (87 + 600, 279, 9, 9))
    pygame.draw.rect(WIN, color_rect, (88 + 600, 279, 9, 9))
    pygame.draw.rect(WIN, color_rect, (88 + 600, 277, 9, 9))
    pygame.draw.rect(WIN, color_rect, (88 + 600, 275, 9, 9))
    pygame.draw.rect(WIN, color_rect, (89 + 600, 273, 9, 9))
    pygame.draw.rect(WIN, color_rect, (91 + 600, 271, 9, 9))
    pygame.draw.rect(WIN, color_rect, (92 + 600, 270, 9, 9))
    pygame.draw.rect(WIN, color_rect, (94 + 600, 269, 9, 9))
    pygame.draw.rect(WIN, color_rect, (95 + 600, 268, 9, 9))
    pygame.draw.rect(WIN, color_rect, (96 + 600, 268, 9, 9))
    pygame.draw.rect(WIN, color_rect, (98 + 600, 268, 9, 9))
    pygame.draw.rect(WIN, color_rect, (100 + 600, 268, 9, 9))
    pygame.draw.rect(WIN, color_rect, (103 + 600, 268, 9, 9))
    pygame.draw.rect(WIN, color_rect, (110 + 600, 269, 5, 9))
    pygame.draw.rect(WIN, color_rect, (112 + 600, 271, 5, 9))
    pygame.draw.rect(WIN, color_rect, (114 + 600, 273, 5, 9))
    pygame.draw.rect(WIN, color_rect, (116 + 600, 275, 5, 9))
    pygame.draw.rect(WIN, color_rect, (118 + 600, 277, 5, 9))
    pygame.draw.rect(WIN, color_rect, (114 + 600, 279, 9, 9))
    pygame.draw.rect(WIN, color_rect, (115 + 600, 282, 9, 9))
    pygame.draw.rect(WIN, color_rect, (115 + 600, 285, 9, 9))
    pygame.draw.rect(WIN, color_rect, (115 + 600, 288, 9, 9))
    pygame.draw.rect(WIN, color_rect, (116 + 600, 274, 9, 9))
    pygame.draw.rect(WIN, color_rect, (121 + 600, 272, 5, 9))

    pygame.draw.rect(WIN, color_rect, (125 + 600, 270, 9, 9))
    pygame.draw.rect(WIN, color_rect, (130 + 600, 270, 9, 9))
    pygame.draw.rect(WIN, color_rect, (137 + 600, 272, 9, 9))
    pygame.draw.rect(WIN, color_rect, (139 + 600, 272, 9, 9))



    # flipped 1 on the right side

    shift_x = 100  # 100 units to the right
    x = 155 + shift_x
    y = 404
    for i in range(0, 21):  # bottom of the hand
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x += 5
    x = 155 + shift_x
    y = 404
    for i in range(0, 29):  # left side of hand (bottom)
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x -= 1.1
        y -= 2

    pygame.draw.rect(WIN, color_rect, (125 + shift_x, 340, 9, 9))  # left side combining piece

    x = 125.5 + shift_x
    y = 335
    for i in range(0, 20):  # left side of hand (top of it)
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x += 1
        y -= 2

    x = 150 + shift_x
    y = 295.5
    for i in range(0, 5):  # top left diagonal
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x += 2
    x = 167 + shift_x
    y = 280
    for i in range(0, 20):  # straight down thumb line (flipped)
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        y += 2
    pygame.draw.rect(WIN, color_rect, (168 + shift_x, 273, 8, 9))  # idk

    x = 260 + shift_x
    y = 400
    for i in range(0, 20):  # bottom right part
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x += 0.7
        y -= 2

    x = 275 + shift_x
    y = 354
    for i in range(0, 26):  # top right part
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x += 0.1
        y -= 2

    x = 278 + shift_x
    y = 296
    for i in range(0, 6):
        pygame.draw.rect(WIN, color_rect, (x, y, 10, 9))
        x -= 1
        y -= 1

    pygame.draw.rect(WIN, color_rect, (263 + shift_x, 292, 10, 9))
    pygame.draw.rect(WIN, color_rect, (261 + shift_x, 293, 10, 9))
    pygame.draw.rect(WIN, color_rect, (259 + shift_x, 293, 10, 9))
    pygame.draw.rect(WIN, color_rect, (257 + shift_x, 294, 10, 9))
    pygame.draw.rect(WIN, color_rect, (257 + shift_x, 294, 10, 9))
    pygame.draw.rect(WIN, color_rect, (255 + shift_x, 294, 10, 9))
    pygame.draw.rect(WIN, color_rect, (253 + shift_x, 294, 10, 9))

    x = 251.4 + shift_x
    y = 294
    for i in range(0, 2):
        pygame.draw.rect(WIN, color_rect, (x, y, 10, 9))
        y += 2

    pygame.draw.rect(WIN, color_rect, (251.4 + shift_x, 302, 10, 9))
    pygame.draw.rect(WIN, color_rect, (251.4 + shift_x, 290, 10, 9))
    pygame.draw.rect(WIN, color_rect, (251.4 + shift_x, 288, 10, 9))

    x = 251 + shift_x
    y = 286
    for i in range(0, 3):
        pygame.draw.rect(WIN, color_rect, (x, y, 10, 9))
        x -= 2
        y -= 2

    pygame.draw.rect(WIN, color_rect, (243 + shift_x, 278.8, 10, 9))
    pygame.draw.rect(WIN, color_rect, (241 + shift_x, 278, 10, 9))
    pygame.draw.rect(WIN, color_rect, (239 + shift_x, 280, 10, 9))
    pygame.draw.rect(WIN, color_rect, (237 + shift_x, 278, 10, 9))
    pygame.draw.rect(WIN, color_rect, (235 + shift_x, 280, 10, 9))

    x = 233 + shift_x
    y = 280
    for i in range(0, 2):
        pygame.draw.rect(WIN, color_rect, (x, y, 10, 9))
        x -= 2
        y += 1

    pygame.draw.rect(WIN, color_rect, (226 + shift_x, 284, 10, 9))
    pygame.draw.rect(WIN, color_rect, (224 + shift_x, 290, 10, 9))
    pygame.draw.rect(WIN, color_rect, (223 + shift_x, 290, 10, 9))
    pygame.draw.rect(WIN, color_rect, (223 + shift_x, 295, 10, 9))

    x = 223 + shift_x
    y = 287
    for i in range(0, 3):
        pygame.draw.rect(WIN, color_rect, (x, y, 10, 9))
        y -= 2

    pygame.draw.rect(WIN, color_rect, (223 + shift_x, 279, 9, 9))
    pygame.draw.rect(WIN, color_rect, (222 + shift_x, 279, 9, 9))
    pygame.draw.rect(WIN, color_rect, (222 + shift_x, 277, 9, 9))
    pygame.draw.rect(WIN, color_rect, (222 + shift_x, 275, 9, 9))
    pygame.draw.rect(WIN, color_rect, (221 + shift_x, 273, 9, 9))
    pygame.draw.rect(WIN, color_rect, (219 + shift_x, 271, 9, 9))
    pygame.draw.rect(WIN, color_rect, (218 + shift_x, 270, 9, 9))
    pygame.draw.rect(WIN, color_rect, (216 + shift_x, 269, 9, 9))
    pygame.draw.rect(WIN, color_rect, (215 + shift_x, 268, 9, 9))
    pygame.draw.rect(WIN, color_rect, (214 + shift_x, 268, 9, 9))
    pygame.draw.rect(WIN, color_rect, (212 + shift_x, 268, 9, 9))
    pygame.draw.rect(WIN, color_rect, (210 + shift_x, 268, 9, 9))
    pygame.draw.rect(WIN, color_rect, (207 + shift_x, 268, 9, 9))
    pygame.draw.rect(WIN, color_rect, (200 + shift_x, 269, 5, 9))
    pygame.draw.rect(WIN, color_rect, (198 + shift_x, 271, 5, 9))
    pygame.draw.rect(WIN, color_rect, (196 + shift_x, 273, 5, 9))
    pygame.draw.rect(WIN, color_rect, (194 + shift_x, 275, 5, 9))
    pygame.draw.rect(WIN, color_rect, (192 + shift_x, 277, 5, 9))
    pygame.draw.rect(WIN, color_rect, (196 + shift_x, 279, 9, 9))
    pygame.draw.rect(WIN, color_rect, (195 + shift_x, 282, 9, 9))
    pygame.draw.rect(WIN, color_rect, (195 + shift_x, 285, 9, 9))
    pygame.draw.rect(WIN, color_rect, (195 + shift_x, 288, 9, 9))
    pygame.draw.rect(WIN, color_rect, (194 + shift_x, 274, 9, 9))
    pygame.draw.rect(WIN, color_rect, (189 + shift_x, 272, 5, 9))

    pygame.draw.rect(WIN, color_rect, (185 + shift_x, 270, 9, 9))
    pygame.draw.rect(WIN, color_rect, (180 + shift_x, 270, 9, 9))
    pygame.draw.rect(WIN, color_rect, (173 + shift_x, 272, 9, 9))
    pygame.draw.rect(WIN, color_rect, (171 + shift_x, 272, 9, 9))
   


    #clean-up white or black spaces
    color_rect = (255,255,255)
    pygame.draw.rect(WIN, color_rect, (386, 293, 9, 20))
    pygame.draw.rect(WIN, color_rect, (384, 290, 15, 9))
    color_rect = (0,0,0)
    pygame.draw.rect(WIN, color_rect, (300, 270, 9, 9))
    pygame.draw.rect(WIN, color_rect, (300, 270, 9, 9))

    #flipped number 2:
    shift_x = 695  # 100 units to the right
    x = 155 + shift_x
    y = 404
    for i in range(0, 21):  # bottom of the hand
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x += 5
    x = 155 + shift_x
    y = 404
    for i in range(0, 29):  # left side of hand (bottom)
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x -= 1.1
        y -= 2

    pygame.draw.rect(WIN, color_rect, (125 + shift_x, 340, 9, 9))  # left side combining piece

    x = 125.5 + shift_x
    y = 335
    for i in range(0, 20):  # left side of hand (top of it)
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x += 1
        y -= 2

    x = 150 + shift_x
    y = 295.5
    for i in range(0, 5):  # top left diagonal
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x += 2
    x = 167 + shift_x
    y = 280
    for i in range(0, 20):  # straight down thumb line (flipped)
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        y += 2
    pygame.draw.rect(WIN, color_rect, (168 + shift_x, 273, 8, 9))  # idk

    x = 260 + shift_x
    y = 400
    for i in range(0, 20):  # bottom right part
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x += 0.7
        y -= 2

    x = 275 + shift_x
    y = 354
    for i in range(0, 26):  # top right part
        pygame.draw.rect(WIN, color_rect, (x, y, 9, 9))
        x += 0.1
        y -= 2

    x = 278 + shift_x
    y = 296
    for i in range(0, 6):
        pygame.draw.rect(WIN, color_rect, (x, y, 10, 9))
        x -= 1
        y -= 1

    pygame.draw.rect(WIN, color_rect, (263 + shift_x, 292, 10, 9))
    pygame.draw.rect(WIN, color_rect, (261 + shift_x, 293, 10, 9))
    pygame.draw.rect(WIN, color_rect, (259 + shift_x, 293, 10, 9))
    pygame.draw.rect(WIN, color_rect, (257 + shift_x, 294, 10, 9))
    pygame.draw.rect(WIN, color_rect, (257 + shift_x, 294, 10, 9))
    pygame.draw.rect(WIN, color_rect, (255 + shift_x, 294, 10, 9))
    pygame.draw.rect(WIN, color_rect, (253 + shift_x, 294, 10, 9))

    x = 251.4 + shift_x
    y = 294
    for i in range(0, 2):
        pygame.draw.rect(WIN, color_rect, (x, y, 10, 9))
        y += 2

    pygame.draw.rect(WIN, color_rect, (251.4 + shift_x, 302, 10, 9))
    pygame.draw.rect(WIN, color_rect, (251.4 + shift_x, 290, 10, 9))
    pygame.draw.rect(WIN, color_rect, (251.4 + shift_x, 288, 10, 9))

    x = 251 + shift_x
    y = 286
    for i in range(0, 3):
        pygame.draw.rect(WIN, color_rect, (x, y, 10, 9))
        x -= 2
        y -= 2

    pygame.draw.rect(WIN, color_rect, (243 + shift_x, 278.8, 10, 9))
    pygame.draw.rect(WIN, color_rect, (241 + shift_x, 278, 10, 9))
    pygame.draw.rect(WIN, color_rect, (239 + shift_x, 280, 10, 9))
    pygame.draw.rect(WIN, color_rect, (237 + shift_x, 278, 10, 9))
    pygame.draw.rect(WIN, color_rect, (235 + shift_x, 280, 10, 9))

    x = 233 + shift_x
    y = 280
    for i in range(0, 2):
        pygame.draw.rect(WIN, color_rect, (x, y, 10, 9))
        x -= 2
        y += 1

    pygame.draw.rect(WIN, color_rect, (226 + shift_x, 284, 10, 9))
    pygame.draw.rect(WIN, color_rect, (224 + shift_x, 290, 10, 9))
    pygame.draw.rect(WIN, color_rect, (223 + shift_x, 290, 10, 9))
    pygame.draw.rect(WIN, color_rect, (223 + shift_x, 295, 10, 9))

    x = 223 + shift_x
    y = 287
    for i in range(0, 3):
        pygame.draw.rect(WIN, color_rect, (x, y, 10, 9))
        y -= 2

    pygame.draw.rect(WIN, color_rect, (223 + shift_x, 279, 9, 9))
    pygame.draw.rect(WIN, color_rect, (222 + shift_x, 279, 9, 9))
    pygame.draw.rect(WIN, color_rect, (222 + shift_x, 277, 9, 9))
    pygame.draw.rect(WIN, color_rect, (222 + shift_x, 275, 9, 9))
    pygame.draw.rect(WIN, color_rect, (221 + shift_x, 273, 9, 9))
    pygame.draw.rect(WIN, color_rect, (219 + shift_x, 271, 9, 9))
    pygame.draw.rect(WIN, color_rect, (218 + shift_x, 270, 9, 9))
    pygame.draw.rect(WIN, color_rect, (216 + shift_x, 269, 9, 9))
    pygame.draw.rect(WIN, color_rect, (215 + shift_x, 268, 9, 9))
    pygame.draw.rect(WIN, color_rect, (214 + shift_x, 268, 9, 9))
    pygame.draw.rect(WIN, color_rect, (212 + shift_x, 268, 9, 9))
    pygame.draw.rect(WIN, color_rect, (210 + shift_x, 268, 9, 9))
    pygame.draw.rect(WIN, color_rect, (207 + shift_x, 268, 9, 9))
    pygame.draw.rect(WIN, color_rect, (200 + shift_x, 269, 5, 9))
    pygame.draw.rect(WIN, color_rect, (198 + shift_x, 271, 5, 9))
    pygame.draw.rect(WIN, color_rect, (196 + shift_x, 273, 5, 9))
    pygame.draw.rect(WIN, color_rect, (194 + shift_x, 275, 5, 9))
    pygame.draw.rect(WIN, color_rect, (192 + shift_x, 277, 5, 9))
    pygame.draw.rect(WIN, color_rect, (196 + shift_x, 279, 9, 9))
    pygame.draw.rect(WIN, color_rect, (195 + shift_x, 282, 9, 9))
    pygame.draw.rect(WIN, color_rect, (195 + shift_x, 285, 9, 9))
    pygame.draw.rect(WIN, color_rect, (195 + shift_x, 288, 9, 9))
    pygame.draw.rect(WIN, color_rect, (194 + shift_x, 274, 9, 9))
    pygame.draw.rect(WIN, color_rect, (189 + shift_x, 272, 5, 9))

    pygame.draw.rect(WIN, color_rect, (185 + shift_x, 270, 9, 9))
    pygame.draw.rect(WIN, color_rect, (180 + shift_x, 270, 9, 9))
    pygame.draw.rect(WIN, color_rect, (173 + shift_x, 272, 9, 9))
    pygame.draw.rect(WIN, color_rect, (171 + shift_x, 272, 9, 9))

def extend_index_finger1():
    # Erase the fingertip of the index finger
    pygame.draw.rect(WIN, WHITE, (126, 270, 18, 30))

    # Draw the extended index finger lines
    pygame.draw.line(WIN, BLACK, (120, 195), (120, 300), 10)  # Left line of index finger
    pygame.draw.line(WIN, BLACK, (147, 195), (147, 300), 10)  # Right line of index finger

    # Draw the fingertip at the new position
    pygame.draw.arc(WIN, BLACK, (116, 182, 37, 35), 0, 3.14, 10)  # Fingertip



def extend_middle_finger1():
    # Erase the fingertip of the index finger
    pygame.draw.rect(WIN, WHITE, (95, 260, 21, 40))

    # Draw the extended index finger lines
    pygame.draw.line(WIN, BLACK, (92, 187), (92, 300), 10)  # Left line of index finger
    pygame.draw.line(WIN, BLACK, (121, 187), (121, 300), 10)  # Left line of index finger

    # Draw the fingertip at the new position
    pygame.draw.arc(WIN, BLACK, (88, 177, 40, 33), 0, 3.14, 10)  # Fingertip


def extend_ring_finger1():
    # Erase the fingertip of the index finger
    pygame.draw.rect(WIN, WHITE, (58, 270, 30, 42))

    # Draw the extended index finger lines
    pygame.draw.line(WIN, BLACK, (65, 195), (65, 310), 10)  # Left line of index finger
    pygame.draw.line(WIN, BLACK, (90, 195), (90, 310), 10)  # Left line of index finger
   

    # Draw the fingertip at the new position
    pygame.draw.arc(WIN, BLACK, (62, 185, 35, 33), 0, 3.14, 10)  # Fingertip

    # Fill in
    pygame.draw.rect(WIN, BLACK, (54, 294, 15, 10))

def extend_pinky_finger1():
    # Erase the fingertip of the index finger
    pygame.draw.rect(WIN, WHITE, (43.5, 270, 18, 35))

    # Draw the extended index finger lines
    pygame.draw.line(WIN, BLACK, (36.5, 230), (36.5, 300), 10)  # Left line of index finger

    # Draw the fingertip at the new position
    pygame.draw.arc(WIN, BLACK, (32, 220, 39, 35), 0, 3.14, 10)  # Fingertip


    #second-hand

def extend_index_finger2():
    # Erase the fingertip of the index finger
    pygame.draw.rect(WIN, WHITE, (276, 270, 18, 30))

    # Draw the extended index finger lines
    pygame.draw.line(WIN, BLACK, (270, 195), (270, 300), 10)  # Left line of index finger
    pygame.draw.line(WIN, BLACK, (297, 195), (297, 300), 10)  # Right line of index finger

    # Draw the fingertip at the new position
    pygame.draw.arc(WIN, BLACK, (266, 182, 37, 35), 0, 3.14, 10)  # Fingertip


def extend_middle_finger2():
    # Erase the fingertip of the index finger
    pygame.draw.rect(WIN, WHITE, (303, 260, 21, 40))

    # Draw the extended index finger lines
    pygame.draw.line(WIN, BLACK, (325, 187), (325, 300), 10)  # Left line of index finger
    pygame.draw.line(WIN, BLACK, (298, 187), (298, 300), 10)  # Left line of index finger

    # Draw the fingertip at the new position
    pygame.draw.arc(WIN, BLACK, (294, 175, 37.5, 33), 0, 3.14, 10)  # Fingertip

def extend_ring_finger2():
    # Erase the fingertip of the index finger
    pygame.draw.rect(WIN, WHITE, (331, 270, 30, 42))

    # Draw the extended index finger lines
    pygame.draw.line(WIN, BLACK, (350, 195), (350, 310), 10)  # Left line of index finger
    pygame.draw.line(WIN, BLACK, (325, 195), (325, 310), 10)  # Left line of index finger
   

    # Draw the fingertip at the new position
    pygame.draw.arc(WIN, BLACK, (322, 185, 35, 33), 0, 3.14, 10)  # Fingertip

    # Fill in
    pygame.draw.rect(WIN, BLACK, (350, 294, 15, 10))

def extend_pinky_finger2():
    # Erase the fingertip of the index finger
    pygame.draw.rect(WIN, WHITE, (356, 270, 18, 35))

    # Draw the extended index finger lines
    pygame.draw.line(WIN, BLACK, (377, 230), (377, 300), 10)  # Left line of index finger

    # Draw the fingertip at the new position
    pygame.draw.arc(WIN, BLACK, (348, 218, 35, 35), 0, 3.14, 10)  # Fingertip

def extend_index_finger3():
    # Erase the fingertip of the index finger
    pygame.draw.rect(WIN, WHITE, (721.5, 270, 22, 30))

    # Draw the extended index finger lines
    pygame.draw.line(WIN, BLACK, (719, 195), (719, 300), 10)  # Left line of index finger
    pygame.draw.line(WIN, BLACK, (747, 195), (747, 300), 10)  # Right line of index finger

    # Draw the fingertip at the new position
    pygame.draw.arc(WIN, BLACK, (715, 182, 38, 35), 0, 3.14, 10)  # Fingertip

def extend_middle_finger3():
    # Erase the fingertip of the index finger
    pygame.draw.rect(WIN, WHITE, (692, 260, 23, 45))

    # Draw the extended index finger lines
    pygame.draw.line(WIN, BLACK, (690, 187), (690, 305), 10)  # Left line of index finger
    pygame.draw.line(WIN, BLACK, (719, 187), (719, 305), 10)  # Left line of index finger

    # Draw the fingertip at the new position
    pygame.draw.arc(WIN, BLACK, (686, 177, 40, 33), 0, 3.14, 10)  # Fingertip

def extend_ring_finger3():
    # Erase the fingertip of the index finger
    pygame.draw.rect(WIN, WHITE, (664, 270, 22, 40))

    # Draw the extended index finger lines
    pygame.draw.line(WIN, BLACK, (662, 195), (662, 310), 10)  # Left line of index finger
    pygame.draw.line(WIN, BLACK, (686, 195), (686, 310), 10)  # Left line of index finger
   

    # Draw the fingertip at the new position
    pygame.draw.arc(WIN, BLACK, (658, 185, 35, 33), 0, 3.14, 10)  # Fingertip

    # Fill in
    #pygame.draw.rect(WIN, BLACK, (54, 294, 15, 10))

def extend_pinky_finger3():
    # Erase the fingertip of the index finger
    pygame.draw.rect(WIN, WHITE, (640.5, 270, 17, 35))

    # Draw the extended index finger lines
    pygame.draw.line(WIN, BLACK, (636, 230), (636, 304), 10)  # Left line of index finger

    # Draw the fingertip at the new position
    pygame.draw.arc(WIN, BLACK, (632, 220, 36, 36), 0, 3.14, 10)  # Fingertip

def extend_index_finger4():
    # Erase the fingertip of the index finger
    pygame.draw.rect(WIN, WHITE, (871, 270, 19, 30))

    # Draw the extended index finger lines
    pygame.draw.line(WIN, BLACK, (865, 195), (865, 300), 10)  # Left line of index finger
    pygame.draw.line(WIN, BLACK, (891, 195), (891, 300), 10)  # Right line of index finger

    # Draw the fingertip at the new position
    pygame.draw.arc(WIN, BLACK, (860, 182, 37, 35), 0, 3.14, 10)  # Fingertip

def extend_middle_finger4():
    # Erase the fingertip of the index finger
    pygame.draw.rect(WIN, WHITE, (897, 260, 21, 40))

    # Draw the extended index finger lines
    pygame.draw.line(WIN, BLACK, (920, 187), (920, 302), 10)  # Left line of index finger
    pygame.draw.line(WIN, BLACK, (893, 187), (893, 302), 10)  # Left line of index finger

    # Draw the fingertip at the new position
    pygame.draw.arc(WIN, BLACK, (888, 177, 38, 36), 0, 3.14, 10)  # Fingertip

def extend_ring_finger4():
    # Erase the fingertip of the index finger
    pygame.draw.rect(WIN, WHITE, (926, 270, 20, 40))

    # Draw the extended index finger lines
    pygame.draw.line(WIN, BLACK, (948, 195), (948, 310), 10)  # Left line of index finger
    pygame.draw.line(WIN, BLACK, (923, 195), (923, 310), 10)  # Left line of index finger
   

    # Draw the fingertip at the new position
    pygame.draw.arc(WIN, BLACK, (918, 185, 36, 34), 0, 3.14, 10)  # Fingertip
    

def extend_pinky_finger4():
    # Erase the fingertip of the index finger
    pygame.draw.rect(WIN, WHITE, (954, 270, 18, 45))

    # Draw the extended index finger lines
    pygame.draw.line(WIN, BLACK, (976, 230), (976, 300), 10)  # Left line of index finger


    # Draw the fingertip at the new position
    pygame.draw.arc(WIN, BLACK, (945, 218, 35, 35), 0, 3.14, 10)  # Fingertip
    

import pygame

import pygame

import pygame

def main():
    clock = pygame.time.Clock()

    run = True
    # Track finger extensions for all hands
    index_finger_extended_right = False
    index_finger_extended_left = False
    middle_finger_extended_up = False
    ring_finger_extended_down = False
    middle_finger_extended_1 = False
    ring_finger_extended_2 = False
    pinky_finger_extended_3 = False
    middle_finger_extended_4 = False
    ring_finger_extended_5 = False
    pinky_finger_extended_6 = False
    middle_finger_extended_7 = False
    ring_finger_extended_8 = False
    pinky_finger_extended_9 = False
    middle_finger_extended_10 = False
    ring_finger_extended_11 = False
    pinky_finger_extended_12 = False

    # New flags for 'a' and 'b' keys
    extend_middle_ring_fingers = False
    extend_middle_ring_pinky_fingers = False

    while run:
        clock.tick(FPS)  # Run the while loop at 30 times per second

        for event in pygame.event.get():  # List of all events that are happening
            if event.type == pygame.QUIT:
                run = False  # Quit the game

            # Check if a key was pressed down
            if event.type == pygame.KEYDOWN:
                # Right arrow key
                if event.key == pygame.K_RIGHT:
                    index_finger_extended_right = True
                    extend_index_finger1()

                # Left arrow key
                if event.key == pygame.K_LEFT:
                    index_finger_extended_left = True
                    extend_index_finger3()

                # Key 1
                if event.key == pygame.K_1:
                    middle_finger_extended_1 = True
                    extend_middle_finger1()

                # Key 2
                if event.key == pygame.K_2:
                    ring_finger_extended_2 = True
                    extend_ring_finger1()

                # Key 3
                if event.key == pygame.K_3:
                    pinky_finger_extended_3 = True
                    extend_pinky_finger1()

                # Key 4
                if event.key == pygame.K_4:
                    middle_finger_extended_4 = True
                    extend_middle_finger2()

                # Key 5
                if event.key == pygame.K_5:
                    ring_finger_extended_5 = True
                    extend_ring_finger2()

                # Key 6
                if event.key == pygame.K_6:
                    pinky_finger_extended_6 = True
                    extend_pinky_finger2()

                # Key 7
                if event.key == pygame.K_7:
                    middle_finger_extended_7 = True
                    extend_middle_finger3()

                # Key 8
                if event.key == pygame.K_8:
                    ring_finger_extended_8 = True
                    extend_ring_finger3()

                # Key 9
                if event.key == pygame.K_9:
                    pinky_finger_extended_9 = True
                    extend_pinky_finger3()

                # Key 10
                if event.key == pygame.K_0:
                    middle_finger_extended_10 = True
                    extend_middle_finger4()

                # Key 11
                if event.key == pygame.K_MINUS:
                    ring_finger_extended_11 = True
                    extend_ring_finger4()

                # Key 12
                if event.key == pygame.K_EQUALS:
                    pinky_finger_extended_12 = True
                    extend_pinky_finger4()

                # Character 'a'
                if event.key == pygame.K_a:
                    middle_finger_extended_1 = True
                    ring_finger_extended_2 = True
                    extend_middle_finger1()
                    extend_ring_finger1()

                # Character 'b'
                if event.key == pygame.K_b:
                    middle_finger_extended_1 = True
                    ring_finger_extended_2 = True
                    pinky_finger_extended_3 = True
                    extend_middle_finger1()
                    extend_ring_finger1()
                    extend_pinky_finger1()
                
                # Character 'c'
                if event.key == pygame.K_c:
                    middle_finger_extended_4 = True
                    ring_finger_extended_5 = True
                    extend_middle_finger2()
                    extend_ring_finger2()
                    extend_pinky_finger2()
                
                # Character 'd'
                if event.key == pygame.K_d:
                    middle_finger_extended_4 = True
                    ring_finger_extended_5 = True
                    pinky_finger_extended_6 = True
                    extend_middle_finger2()
                    extend_ring_finger2()
                    extend_pinky_finger2()
                
                # Character 'e'
                if event.key == pygame.K_e:
                    middle_finger_extended_7 = True
                    ring_finger_extended_8 = True
                    extend_middle_finger3()
                    extend_ring_finger3()

                 # Character 'f'
                if event.key == pygame.K_f:
                    middle_finger_extended_10 = True
                    ring_finger_extended_11 = True
                    extend_middle_finger3()
                    extend_ring_finger3()
                
                # Character 'g'
                if event.key == pygame.K_g:
                    middle_finger_extended_10 = True
                    ring_finger_extended_11 = True
                    extend_middle_finger4()
                    extend_ring_finger4()

                # Character 'h'
                if event.key == pygame.K_h:
                    middle_finger_extended_10 = True
                    ring_finger_extended_11 = True
                    pinky_finger_extended_12 = True
                    extend_middle_finger4()
                    extend_ring_finger4()
                    extend_pinky_finger4()
           

        draw_window()
        draw_something()
        extend_index_finger1()
        extend_index_finger2()
        extend_index_finger3()
        extend_index_finger4()
        draw_text("KEY: Hand1 : 1, Hand2: 2, Hand3: 3, Hand4: 4 ", 0, 1, (0, 0, 0))  # Text, x, y, and color
        draw_text1("1: Extend Middle for 1",0,35, (0,0,0))
        draw_text1("2: Extend Ring for 1",0,57, (0,0,0))
        draw_text1("3: Extend Pinky for 1",0,79, (0,0,0))
        draw_text1("4: Extend Middle for 2",0,101, (0,0,0))
        draw_text1("5: Extend Ring for 2",0,123, (0,0,0))
        draw_text1("6: Extend Pinky for 2",0,145, (0,0,0))
        draw_text1("7: Extend Middle for 3",235,35, (0,0,0))
        draw_text1("8: Extend Ring for 3",235,57, (0,0,0))
        draw_text1("9: Extend Pinky for 3",235,79, (0,0,0))
        draw_text1("0: Extend Middle for 4",235,101, (0,0,0))
        draw_text1("-: Extend Ring for 4",235,123, (0,0,0))
        draw_text1("=: Extend Pinky for 4",235,145, (0,0,0))
        draw_text1("a: Extend Middle and Ring for 1",455,35, (0,0,0))
        draw_text1("b: Extend Middle, Ring, and Pinky for 1",455,57, (0,0,0))
        draw_text1("c: Extend Middle and Ring for 2",455,79, (0,0,0))
        draw_text1("d: Extend Middle, Ring, and Piny for 2",455,101, (0,0,0))
        draw_text1("e:Extend Middle and Ring for 3",455,123, (0,0,0))
        draw_text1("f:Extend Middle,Ring, and Piny for 3" ,455,145, (0,0,0))

        # Permanently redraw fingers based on key presses
        if index_finger_extended_right:
            extend_index_finger1()
        if index_finger_extended_left:
            extend_index_finger3()
        if middle_finger_extended_1:
            extend_middle_finger1()
        if ring_finger_extended_2:
            extend_ring_finger1()
        if pinky_finger_extended_3:
            extend_pinky_finger1()
        if middle_finger_extended_4:
            extend_middle_finger2()
        if ring_finger_extended_5:
            extend_ring_finger2()
        if pinky_finger_extended_6:
            extend_pinky_finger2()
        if middle_finger_extended_7:
            extend_middle_finger3()
        if ring_finger_extended_8:
            extend_ring_finger3()
        if pinky_finger_extended_9:
            extend_pinky_finger3()
        if middle_finger_extended_10:
            extend_middle_finger4()
        if ring_finger_extended_11:
            extend_ring_finger4()
        if pinky_finger_extended_12:
            extend_pinky_finger4()

        # Handle new key functionalities
        if extend_middle_ring_fingers:
            extend_middle_finger1()
            extend_ring_finger1()
            extend_middle_ring_fingers = False  # Reset flag

        if extend_middle_ring_pinky_fingers:
            extend_middle_finger1()
            extend_ring_finger1()
            extend_pinky_finger1()
            extend_middle_ring_pinky_fingers = False  # Reset flag

        pygame.display.update()  # Update the entire display in each frame

    pygame.quit()  # Quit Pygame when exiting the game




if __name__ == "__main__":
    main()

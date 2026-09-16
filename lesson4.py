# NEON CITY

import ctypes

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    ctypes.windll.user32.SetProcessDPIAware()

import pgzrun

WIDTH = 800
HEIGHT = 550

SCALE_X = WIDTH / 1000

def X(value):
    return int(value * SCALE_X)

MAGENTA = (255,0,255)
CYAN = (0,255,255)
WHITE = (255,255,255)
black = (0,0,0)

def draw_rectangle(x,y,width,height,color):
    screen.draw.line((X(x),y), (X(x + width), y), color)
    screen.draw.line((X(x),y), (X(x),y  + width), color)
    screen.draw.line((X(x + width),y), (X(x + width), y + height), color)
    screen.draw.line((X(x),y + height), (X(x + width),y  + height), color)

def draw():
    screen.fill(BLACK)

    screen.draw.text(
        "NEON WIREFRAME CITY",
        fontsize = 45,
        color = MAGENTA
    )

    #SUN

    sun_x = 500
    sun_y = 180
    radius = 90

    screen.draw.circle(
        (X(sun_x), sun_y),
        int(radius * SCALE_X)
        MAGENTA
    )

    #SUN STRIPES

    for y in range(130,240,15):
        screen.draw.line((X(420),y), (X(580), y),MAGENTA)

    #Horizon
    horizon_y = 420
    screen.draw.line((X(0), horizon_y), (X(1000), horizon_y), CYAN)

    vanish_x = 500
    vanish_y = horizon_y

    for x in range(0,1001,40):
        screen.draw.line(
            (X(x), HEIGHT)
            (X(vanish_x), vanish_y),
            CYAN
        )

    y = horizon_y + 20
    gap = 20

    while y < HEIGHT:
      screen.draw.line((X(0),y), (X(1000), y), CYAN)
      Y = Y + gap
      gap = gap + 6

    left_buildings = [
      (50,220,70,200)
      (150,170,90,250)
      (280,270,60,150)
    ]

    for x,y,w,h in left_buildings:
        offset = 30
        draw_rectangle(x,y,w,h, MAGENTA)
        draw_rectangle( x + offset,y - offset,w,h, MAGENTA)
        screen.draw.line(
            (X(x), y),
            (X(x + offset), y - offset),
            MAGENTA
        )

        screen.draw.line(
                    (X(x + w), y),
                    (X(x + w + offset), y - offset),
                    MAGENTA
                )

        screen.draw.line(
                            (X(x), y + h),
                            (X(x + offset), y + h - offset),
                            MAGENTA
                        )
                


        screen.draw.line(
                            (X(x + w), y),
                            (X(x + w + offset), y + h - offset),
                            MAGENTA
                        )

    right_buildings = [
        (650,270,70,150),
        (760,170,90,250),
        (880,220,70,200)
    ]

    for x,y,w,h in right_buildings:
        offset = 30
        draw_rectangle(x,y,w,h, CYAN)
        draw_rectangle( x- offset, y - offset,w,h,CYAN)
        screen.draw.line(
            (X(x),y)
            (X(x - offset),y - offset),
            CYAN
        )       

        screen.draw.line(
                    (X(x + w),y)
                    (X(x + w - offset),y - offset),
                    CYAN
                )    

        screen.draw.line(
                      (X(x),y + h)
                      (X(x - offset),y + h - offset),
                      CYAN
                ) 


          screen.draw.line(
                      (X(x + w),y + h)
                      (X(x + w - offset),y + h - offset),
                      CYAN
                ) 

    stars = [
        (80,60),
        (150,90),
        (250,70),
        (350,100),
        (650,80),
        (760,60),
        (900,90),
    ] 

    for x, y in stars:
        screen.draw.filled_circle((X(x), y), 2, WHITE)


pgzrun.go()              
        
        
                
        
        






import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 300

def draw():
   screen.fill((0,0,0)) #background

   r = 255
   g = 0
   b = randint(120,255)

   cx, cy = 150,150

   size = 20

   for i in range(15):
      point1 = (cx, cy - size)
      point2 = (cx - size, cy + size)
      point3 = (cx + size,cy + size)

      screen.draw.line(point1,point2, (r,g,b))
      screen.draw.line(point2,point3, (r,g,b))
      screen.draw.line(point3,point1, (r,g,b))

      size += 10

      r -= 10
      g += 10

pgzrun.go()

# Monte Carlo Rando Walk Part 2
# by Heider Jeffer
# Free University of Bozen-Bolzano
# Faculty of Computer Science
# 2020
import random
def random_walk_2(n):
   x, y = 0, 0
   for i in range(n):
       (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
       x += dx # x = x + dx
       y += dy # y = y + dy

   return (x, y)


for i in  range(25):
    walk = random_walk_2(10)
    print(walk, "Distance from home =",
          abs(walk[0]) + abs(walk[1]))

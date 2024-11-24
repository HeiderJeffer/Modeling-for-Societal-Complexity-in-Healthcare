# Monte Carlo Rando Walk Part 3 Long Walk
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

number_of_walks  = 10000

for walk_length in range(1, 31):
   no_transport = 0 # Number of walks 4 or fewer blocks from home
   for i in range(number_of_walks):
      (x,y) = random_walk_2(walk_length)
      distance = abs(x) + abs(y)
      if distance < 4:
        no_transport += 1
   no_transport_percentage = float(no_transport) / number_of_walks
   print("Walk size = ", walk_length,
              "/ % of no transport = ", 100*no_transport_percentage)

# for i in  range(25):
#     walk = random_walk_2(10)
#     print(walk, "Distance from home =",
#           abs(walk[0]) + abs(walk[1]))
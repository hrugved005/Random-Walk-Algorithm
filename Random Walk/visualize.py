from random_walk import RandomWalk
import matplotlib.pyplot as plt
while True:
 rw= RandomWalk()
 rw.fill_walk()
 plt.scatter(rw.x_values, rw.y_values, s=1)
 xmin=0
 plt.show()

 keep_running = input("Make another walk? (y/n): ")
 if keep_running == 'n':
  break
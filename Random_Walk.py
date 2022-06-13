# -*- coding: utf-8 -*-
# @Time : 2022/6/13 2:25
# @Author : DanYang
# @File : test.py
# @Software : PyCharm
"""
Random walks:
Random walks refer to the inability to predict future development
steps and directions based on past performance.
The core concept is that the conserved quantities carried
by any random walker correspond to a law of diffusion and transportation,
which is close to Brownian motion and is the ideal mathematical state of
Brownian motion. At this stage, it is mainly used in Internet link analysis
and financial stock market.
"""


from random import choice
import matplotlib.pyplot as plt

"""
Set up random walk class
"""


class RandomWalk:
    def __init__(self, num_points=50_000):
        self.num_points = num_points
        # Initialize the data collection array
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            # Determine the direction and distance
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            # refuse to stand still
            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


"""
Draw a random walk image
"""

rw = RandomWalk()
rw.fill_walk()
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
point_numbers = range(rw.num_points)

# Label the starting point and increase the view hierarchy
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
           edgecolors='none', s=1)
ax.scatter(0, 0, c='green', edgecolor='none', s=10)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=10)
plt.text(0, 0, "Start", fontsize=10, c='green')
plt.text(rw.x_values[-1], rw.y_values[-1], "End", fontsize=10, c='red')

# Set title and hide axes
ax.set_title("Random Walk", c='blue')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

# draw the image
plt.show()

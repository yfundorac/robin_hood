import math

# Variables
points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5),
          (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2),
          (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]

# 2. Calculate how many arrows have fallen in each quadrant.
q1 = 0
q2 = 0
q3 = 0
q4 = 0

for i in range(len(points)):
    if(points[i][0] >= 0) & (points[i][1] >= 0):
        q1 += 1
    elif (points[i][0] >= 0) & (points[i][1] <= 0):
        q2 += 1
    elif (points[i][0] <= 0) & (points[i][1] <= 0):
        q3 += 1
    elif (points[i][0] <= 0) & (points[i][1] >= 0):
        q4 += 1

print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)
print("Q4:", q4)

# 3. Find the point closest to the center. Calculate its distance to the center
# Defining a function that calculates the distance to the center can help.


def euclidean_distance(plot):
    distance = math.sqrt((plot[0])**2 + (plot[1]**2))
    return distance


min_distance = euclidean_distance(points[0])
closest_point = points[0]

for i in range(1, len(points)):
    if euclidean_distance(points[i]) < min_distance:
        min_distance = euclidean_distance(points[i])
        closest_point = points[i]

print("The closest point is", closest_point)

# 4. If the target has a radius of 9, calculate the number of arrows that
# must be picked up in the forest.

out = 0
for i in range(0, len(points)):
    if euclidean_distance(points[i]) > 9:
        out += 1

print("The number of arrows that must be picked up in the forest is", out)









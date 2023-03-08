import os

import pygame
import time
import random
import os
from points import Point

os.environ["SDL_VIDEO_CENTERED"] = "1"

# make widht and height
width,height = 500,500

# Make a colors
black = (0,0,0)
white = (255,255,255)
green = (0,255,24)

# pygame settings
pygame.init()
pygame.display.set_caption("Travelling Salesman Algorithm")
screen = pygame.display.set_mode((width,height))

# variables
points = []
offset_screen = 50
smallest_path = []
record_distance = 0
number_of_point = 5

# Generate Random Points on Screen
for n in range(number_of_point):
    x = random.randint(offset_screen,width-offset_screen)
    y = random.randint(offset_screen, height - offset_screen)

    point = Point(x,y)
    points.append(point)

# shuffle points position in the list

def shuffle(a,b,c):
    temp = a[b]
    a[b] = a[c]
    a[c] = temp

# distance between point using pythagorean theory

def calculate_distance(point_list):
    total = 0
    for n in range(len(points)-1):
        distance = ((points[n].x - points[n+1].x)**2 + (points[n].y - points[n+1].y)**2)**0.5
        total += distance
    return total
dist = calculate_distance(points)
record_distance = dist

smallest_path = points.copy()

run = True
while run:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # draw lines and points

    for n in range(len(points)):
        pygame.draw.circle(screen,white,(points[n].x,points[n].y),10)
    a = random.randint(0,len(points)-1)
    b = random.randint(0,len(points)-1)
    shuffle(points,a,b)
    dist = calculate_distance(points)
    if dist < record_distance:
        record_distance = dist
        smallest_path = points.copy()

    for m in range(len(points)-1):
        pygame.draw.line(screen,white,(points[m].x,points[m].y),(points[m+1].x,points[m+1].y),2)

    for m in range(len(smallest_path)-1):
        pygame.draw.line(screen,green,(smallest_path[m].x,smallest_path[m].y),(smallest_path[m+1].x,smallest_path[m+1].y),4)

    pygame.display.update()

print("The Smallest dictance is : ",record_distance)

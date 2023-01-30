#!/usr/bin/python3
"""
    Project - Replicating a Sol LeWitt piece
    Author:  Jailynne Estevez (jesteveznolasco@bennington.edu)
    Date: 11/15/2019
"""
from graphics import *
import random

win = GraphWin("Sol LeWitt Art", 500, 500)
hori_line = Line(Point(250, 0), Point(250, 500))
vert_line = Line(Point(0, 250), Point(500, 250))
hori_line.draw(win)
vert_line.draw(win)

class DraftsPerson:
    """
    A class to represent some person who drafts.
    """
    def __init__(self, color, seconds):
        """
        CONSTRUCTOR
        :param pencil_color: the color of the pencil used to draw lines
        """
        self.pencil_color = color
        self.current_quadrant = 0
        self.current_day = 1
        self.seconds = seconds

    def draw(self, window_to_draw_in, day):
        """
        Draw some lines
        :param window_to_draw_in: A GraphWin window to draw in.
        :param day: The current day (checked against self.current_day)
        :return: None.
        """

        counter = self.seconds
        self.current_day = day

        if self.current_day == 1:
            for i in range(counter):
                a = Line(Point(random.randint(0, 250), random.randint(0, 250)), Point(random.randint(0, 250), random.randint(0, 250)))
                a.draw(window_to_draw_in)
                a.setOutline(self.pencil_color)

        if self.current_day == 2:
            for i in range(counter):
                a = Line(Point(random.randint(250, 500), random.randint(0, 250)), Point(random.randint(250, 500), random.randint(0, 250)))
                a.draw(window_to_draw_in)
                a.setOutline(self.pencil_color)

        if self.current_day == 3:
            for i in range(counter):
                a = Line(Point(random.randint(0, 250), random.randint(250, 500)), Point(random.randint(0, 250), random.randint(250, 500)))
                a.draw(window_to_draw_in)
                a.setOutline(self.pencil_color)

        if self.current_day == 4:
            for i in range(counter):
                a = Line(Point(random.randint(250, 500), random.randint(250, 500)), Point(random.randint(250, 500), random.randint(250, 500)))
                a.draw(window_to_draw_in)
                a.setOutline(self.pencil_color)

def wallDrawing():
    secondsinfourhours = (4*60*60)
    for day in range(0, 4):
        for sec in range(0, secondsinfourhours):
            for draftsperson in range(0, 4):
                p1.draw(win, 0)
                p2.draw(win, 0)
                p3.draw(win, 0)
                p4.draw(win, 0)

quadrant1 = Point(250, 0)
quadrant2 = Point(250, 500)
quadrant3 = Point(0, 250)
quadrant4 = Point(500, 250)

p1 = DraftsPerson("yellow", 5)
p2 = DraftsPerson("red", 10)
p3 = DraftsPerson("black", 15)
p4 = DraftsPerson("blue", 20)

p1.current_quadrant = 1
p2.current_quadrant = 2
p3.current_quadrant = 3
p4.current_quadrant = 4

p1.draw(win, 1)
p2.draw(win, 2)
p3.draw(win, 3)
p4.draw(win, 4)

p1.seconds = 1
p2.seconds = 2
p3.seconds = 3
p4.seconds = 4

p4.draw(win, 1)
p1.draw(win, 2)
p2.draw(win, 3)
p3.draw(win, 4)

p3.draw(win, 1)
p4.draw(win, 2)
p1.draw(win, 3)
p2.draw(win, 4)

p1.seconds = 1
p2.seconds = 2
p3.seconds = 3
p4.seconds = 4

p2.draw(win, 1)
p3.draw(win, 2)
p4.draw(win, 3)
p1.draw(win, 4)


win.getMouse()

#Discussed logic with Katrina, Inigo, Alex, and Rabel in order to fully play out and plan out the lines and coordinates

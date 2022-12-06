from turtle import Turtle

INIT_POS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.dead = False
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for positions in INIT_POS:
            self.create_segment(positions)

    def create_segment(self, positions):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        self.segments.append(new_seg)
        new_seg.goto(positions)

    def move(self):
        a = self.segments
        for seg_num in range(len(a) - 1, 0, -1):
            new_x = a[seg_num - 1].xcor()
            new_y = a[seg_num - 1].ycor()
            a[seg_num].goto(new_x, new_y)
            if seg_num > 3 and a[seg_num].distance(a[0]) < 10:
                self.dead = True
            if a[0].xcor() > 520 or a[0].xcor() < -520 or a[0].ycor() > 360 or a[0].ycor() < -360:
                self.dead = True
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

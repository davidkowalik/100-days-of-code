from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
INITIAL_TRAFFIC = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.add_new_car = 1
        self.init_traffic()
        
    def move_traffic(self):
        for i in range(0, len(self.cars)):
            self.cars[i].forward(STARTING_MOVE_DISTANCE)
        if self.add_new_car % 10 == 0:
            self.add_car()
            self.add_new_car = 1
        else:
            self.add_new_car += 1
        

    def init_car(self):
        new_car = Turtle(shape="square")
        new_car.penup()
        new_car.setheading(180)
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.color(random.choice(COLORS))
        rand_x_cord = random.randint(-300, 300)
        rand_y_cord = random.randint(-260, 300)
        new_car.goto(rand_x_cord, rand_y_cord)
        self.cars.append(new_car) 
    
    def add_car(self):
        new_car = Turtle(shape="square")
        new_car.penup()
        new_car.setheading(180)
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.color(random.choice(COLORS))
        rand_y_cord = random.randint(-300, 300)
        new_car.goto(310, rand_y_cord)
        self.cars.append(new_car)
    
    def init_traffic(self):
        for _ in range(1, INITIAL_TRAFFIC):
            self.init_car()
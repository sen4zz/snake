import turtle
import random
import pygame


"""Настройка игрового поля, а также размера яблока и скорость передвижения змейки:"""

w = 1520
h = 770
apple_size = 10
delay = 100

"""Настройка изменений движении при нажатии кнопок:"""

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

"""Настройки начала игры и при перезагрузке. Ее начальные координаты, вектор движения.
 Также случайно задается расположение яблока и в этом месте создатся круг."""


def reset():
    global snake, snake_dir, apple_position, pen
    snake = [[0, 0], [20, 0], [40, 0], [60, 0], [80, 0]]
    snake_dir = "right"
    apple_position = get_random_apple_position()
    apple.goto(apple_position)
    move_snake()


"""Функция отвечает за анимацию движения змейки. Она передвигается методом одновременного добавления "головы" 
и стирания "хвоста".

Также здесь прописан результат при столкновении змейки с самой собой.
Помимо этого написан результат (для змейки) при поедании змейкой яблока, а также "телепортирования" змейки с 
одного края на другой. При пересечении змейкой верхней границы ее голова должна появиться ровно в той же точке 
по оси Х на противоположной стороне. Идентично с перемещением по боковым границам. """


def move_snake():
    global snake_dir
    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_dir][0]
    new_head[1] = snake[-1][1] + offsets[snake_dir][1]

    if new_head in snake[:-1]:
        reset()
    else:
        snake.append(new_head)

        if not apple_collision():
            snake.pop(0)

        if snake[-1][0] > w / 2:
            snake[-1][0] -= w
        elif snake[-1][0] < - w / 2:
            snake[-1][0] += w
        elif snake[-1][1] > h / 2:
            snake[-1][1] -= h
        elif snake[-1][1] < -h / 2:
            snake[-1][1] += h

        pen.clearstamps()

        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()

        screen.update()

        turtle.ontimer(move_snake, delay)


"""В данной функции написано съедение змейкой яблока и его повторное появление. 
Сначала определяется случайная точка в двумерном пространстве, затем моделька яблока направляется в эту точку."""


def apple_collision():
    global apple_position
    if get_distance(snake[-1], apple_position) < 20:
        apple_position = get_random_apple_position()
        apple.goto(apple_position)
        return True
    return False


"""Задание расположения яблока. Определяется та самая случайная точка."""


def get_random_apple_position():
    x = random.randint(- w / 2 + apple_size, w / 2 - apple_size)
    y = random.randint(- h / 2 + apple_size, h / 2 - apple_size)
    return x, y


"""Настройка "хитбокса" яблока. Нужно для того, чтобы фиксировалось "поедание" змейкой яблока.
"""


def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance


"""В следующих четырех функциях заданны настройки движения змейки """


def go_up():
    global snake_dir
    if snake_dir != "down":
        snake_dir = "up"


def go_right():
    global snake_dir
    if snake_dir != "left":
        snake_dir = "right"


def go_down():
    global snake_dir
    if snake_dir != "up":
        snake_dir = "down"


def go_left():
    global snake_dir
    if snake_dir != "right":
        snake_dir = "left"


"""Прменение настроек и создание не заданных параметров*."""

screen = turtle.Screen()
screen.setup(w, h)
screen.title("Snake")
screen.bgcolor("green")
screen.setup(1550, 770)
screen.tracer(0)


"""*касательно змейки. Задание формы змейки и ее цвета."""

pen = turtle.Turtle("circle")
pen.color("yellow")
pen.penup()


"""*касательно яблока. Задание формы яблока и его цвета."""

apple = turtle.Turtle()
apple.shape("circle")
apple.color("red")
apple.shapesize(apple_size / 15)
apple.penup()


"""*касательно механики изменения движения"""

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

reset()
turtle.done()
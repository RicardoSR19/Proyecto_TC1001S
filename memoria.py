from random import shuffle
from turtle import (
    up, goto, down, color, begin_fill, forward, left,
    end_fill, write, clear, shape, stamp, update, ontimer,
    setup, addshape, hideturtle, tracer, onscreenclick, done
)
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
# Global variable to keep track of the number of "taps".
tap_count = 0


def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    "Update mark and hidden tiles based on tap."
    global tap_count  # Access the global tap_count variable
    tap_count += 1    # Increases the taps counter
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw_tap_count():
    "Draw the tap count on the screen."
    up()
    goto(-180, 180)  # Position to display the number
    color('black')
    write(f'Taps: {tap_count}', font=('Arial', 16, 'normal'))


def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    draw_tap_count()  # Call the function to display the number of taps.
    update()

    if all_tiles_uncovered():
        up()
        goto(-100, -20)  # Position to display the message
        color('black')
        write('¡Has ganado!', font=('Arial', 24, 'bold'))

    ontimer(draw, 100)


def all_tiles_uncovered():
    "Check if all tiles have been uncovered."
    return all(not hidden for hidden in hide)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()

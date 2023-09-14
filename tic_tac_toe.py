from turtle import (
    color, width, up, goto, down, circle, setup,
    hideturtle, tracer, update, onscreenclick, done
)
from freegames import line

# Create a matrix to represent the state of
# the game (0 for empty square, 1 for X, 2 for O).
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    # Change color to red
    color('red')
    # Change thickness of lines
    width(4)
    line(x+33, y+33, x + 100, y + 100)  # Change size of symbol
    line(x+33, y + 100, x + 100, y+33)  # Change size of symbol


def drawo(x, y):
    """Draw O player."""
    # Change color to blue
    color('blue')
    # Change thickness of circle
    width(5)
    up()
    goto(x + 67, y + 26)
    down()
    # Change size of the circle
    circle(40)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']

    # Check if the box is empty
    row = int((y + 200) / 133)
    col = int((x + 200) / 133)

    if board[row][col] == 0:  # Condition for drawing
        draw = players[player]
        draw(x, y)
        update()
        board[row][col] = player + 1  # Update game status
        state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()

from random import *
from turtle import *
from freegames import path


tapCounter = 0
car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64

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
    global tapCounter
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    tapCounter += 1
    print(tapCounter)



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

    counterForTilesThatAreHidden=0

    for count in range(64):
        if (hide[count]==0):
            counterForTilesThatAreHidden+=1

    if (counterForTilesThatAreHidden==64):
        print("No more Tiles")
        done()

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        if tiles[mark]<10:
            goto(x+18, y+8)
        if tiles[mark]>=10:
            goto(x+10, y+8)
        if tiles[mark]%2==0:
            color('green')
        else:
            color('red')
        write(tiles[mark], font=('Arial', 30, 'normal'))
    update()
    ontimer(draw, 100)

    


    

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()

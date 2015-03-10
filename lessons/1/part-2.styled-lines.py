from draw import *

w = Window(title=__file__)

w.line(50, 50, 50, 300, thickness=1, color='red')
w.line(60, 50, 60, 300, thickness=2, color='orange')
w.line(70, 50, 70, 300, thickness=3, color='yellow')
w.line(80, 50, 80, 300, thickness=4, color='green')
w.line(90, 50, 90, 300, thickness=5, color='blue')
w.line(100, 50, 100, 300, thickness=6, color='indigo')

w.wait()

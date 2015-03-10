from draw import *

w = Window(title=__file__)

w.rect(50, 50, 100, 200)
w.rect(150, 150, 300, 250, color='orange', thickness=5)
w.rect(300, 300, 400, 550, color='blue', fill='cyan', thickness=3)

w.wait()

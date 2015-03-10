from draw import *

w = Window(title=__file__)

w.circle(400, 300, 280, color='lightgrey', fill='lightgrey')
w.circle(50, 50, 20)
w.circle(150, 150, 60, color='green', thickness=10)
w.circle(300, 300, 100, color='violet', fill='pink', thickness=3)

w.wait()

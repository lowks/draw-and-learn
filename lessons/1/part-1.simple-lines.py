from draw import *

w = Window(title=__file__)

w.line(0, 0, w.width, w.height)
w.line(w.width, 0, 0, w.height)

w.wait()

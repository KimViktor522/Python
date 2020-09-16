import graphics 
win = gr.GraphWin("Окно", 300, 300)
Rect = gr.Rectangle(Point(50, 50), Point(200, 250))
Rect.setFill('red')
Rect.draw(win)

win.getMouse()
win.close()

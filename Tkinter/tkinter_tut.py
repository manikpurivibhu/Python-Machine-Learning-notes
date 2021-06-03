import tkinter as tk



#every app made with Tlinter needs a root window to place eveerything into it 
#root acts as nested container
root = tk.Tk()

#var = tk.widget1(para-widget(canvas/frame)) puts widget1 onto passed para-widget

#widget.pack(options) organizes widgets in blocks before placing them in parent widget
#pack options are : 1. expand-expands widget to any space not used by parent widget
#  /n 2. fill-fills widget to none/x/y/both axes  /n 3. side(left, right, bottom, top(default))

#Canvas is literally the canvas. Everything(widgets, etc) are on the canvas
canvas = tk.Canvas(root, height = 700, width = 800)
canvas.pack()

#Frame is a frame that goes on top of master. like literally a frame or poster on the wall
frame = tk.Frame(root, bg = '#80c1ff')                  # bg = color string or color hexadecimal code
frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)


'''
#PACK
#Building a button:
button = tk.Button(frame, text = 'Test Button', bg = 'gray', fg = 'red' )
button.pack(side = 'left') 

#Label :
label = tk.Label(frame, text = 'This is a label', bg = 'yellow')
#label.pack(side = 'right')
label.pack(side = 'right', fill = 'both')

entry = tk.Entry(frame, bg = 'green')
#entry.pack(side = 'bottom')
entry.pack(side = 'bottom', expand = True)
'''
'''
#widget.grid to stack widgets in an organized fashion by specifying row and col no in every widget def
#it does have a problem for resizing the widgets

#button:
button = tk.Button(frame, text = 'Test Button', bg = 'gray', fg = 'red' )
button.grid(row = 0, column = 0) 

#Label :
label = tk.Label(frame, text = 'This is a label', bg = 'yellow')
label.grid(row = 0, column = 1)

entry = tk.Entry(frame, bg = 'green')
entry.grid(row = 1, column = 0)
'''


#PLACE : this geometry managaer organizes widgets by putting them in a specific position in the parent widget
#widget.place(options)      options:    1.anchor-exact spot N?S?E?W?NS?etc
#2.bordermode-INSIDE/OUTSIDE    3.height,width
#4.relheight,relwidth- float bw 0 and 1 as a fraction of height and width of parent widget
#relx,rely- horizontal and vertical offset bw 0 & 1 as a fraction of height & width of parent widget
#x, y - horizontal & vertical offset

button = tk.Button(frame, text = 'Test Button', bg = 'gray', fg = 'red' )
button.place(relx = 0.1, rely = 0.1, relwidth = 0.05, relheight = 0.05) 

#Label :
label = tk.Label(frame, text = 'This is a label', bg = 'yellow')
label.place(relx = 0, rely = 0, x=100, y=50)

entry = tk.Entry(frame, bg = 'green')
entry.place(relx = 0, rely = 0, bordermode = 'inside')



#to run your appliication:
root.mainloop()
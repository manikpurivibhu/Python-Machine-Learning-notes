import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=600)
canvas.pack()

def get_string(hmm):
    var = hmm
    global ok 
    ok = label['text'] = str.upper(var)

#background_image = tk.PhotoImage(file = 'i.png')
#background_label = tk.Label(root, image = background_image)
#background_label.place(relwidth = 1, relheight = 1)


frame = tk.Frame(root, bg = '#80c1ff',bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')


entry = tk.Entry(frame, font = 40)
entry.place(relheight = 1, relwidth = 0.65)

button = tk.Button(frame, text = 'Get String', font = 40, command = lambda: get_string(entry.get()))
button.place(relx = 0.7, relheight = 1, relwidth = 0.3)

lower_frame = tk.Frame(root, bg = '#80c1ff', bd = 10)
lower_frame.place(relx = 0.5, rely = 0.25, relheight = 0.6, relwidth = 0.75, anchor = 'n' )

label = tk.Label(lower_frame, font = 50, justify = 'left', bd = 4)
label.place(relwidth = 1, relheight = 1)

root.mainloop()

print(ok)

#Converting this to an actual app

#pip install pyinstaller
#cd <directory location>
#pyinstaller.exe --onefile --icon-<app icon name> main.py
#the app will be in "dist" folder in that directory.
#all the images and files that are used in the program should be in "dist" directory
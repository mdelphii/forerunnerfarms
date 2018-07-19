from Tkinter import *
from PIL import Image,ImageTk


root = Tkinter.Tk()  
root.title("display image")  
im=Image.open("home/pi/Pictures/image1.png") 
photo=ImageTk.PhotoImage(im)  
cv = tk.Canvas()  
cv.pack(side='top', fill='both', expand='yes')  
cv.create_image(10, 10, image=photo, anchor='nw')  

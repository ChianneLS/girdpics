#  imports
import tkinter as tk
from PIL import Image, ImageTk  # Pillow modules

# create the main window
root = tk.Tk()
root.title("Grid and Image Display")
root.geometry("800x480") # might have to adjust

# frame for the grid/ group the grid together
grid_frame = tk.Frame(root)
grid_frame.grid (row =0, column =0, padx=10, pady=10)

# Add a grid of labels and arrage them in order
rows, cols =5,5 # this is the number of colums and rows
for i in range(rows):
    for j in range (cols):
        label = tk.Label(grid_frame, text=f"{i}{j}", font =("Arial",18), width=5, height=2, borderwidth=1, relief="solid")
        label.grid(row=i, column=j, padx=2, pady=2)
                             
#Frame for the image
image_frame = tk.Frame(root)
image_frame.grid(row=0, column=1, padx=10, pady=10)
                             
#Load and display the image
try:
    # load and resize the image
    img = Image.open("cat.jpg")
    img = img.resize((300,300))
    photo =ImageTk.PhotoImage(img)
        
    # Display the image
    img_label = tk.Label(image_frame, image=photo)
    # keep a refenace to advoid garbage collection
    img_label.image = photo
    img_label.pack()
except Exception as e:
    print(" Error loading image: ",e)
    
#run the gui
root.mainloop()

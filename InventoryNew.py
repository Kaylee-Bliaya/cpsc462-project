import os
import tkinter as tk
from PIL import Image, ImageTk
from settings2 import *

def display_next_image():
    global current_image_index, image_label
    current_image_index = (current_image_index + 1) % len(image_files)
    img = Image.open(image_files[current_image_index])
    img = img.resize((500, 650), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    image_label.config(image=photo)
    image_label.image = photo

play_image = pygame.image.load("images/play.png").convert_alpha()


image_folder = "/Users/shaf/Desktop/cpsc462-project-main/graphics"

image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.lower().endswith('.png')]
current_image_index = 0

root = tk.Tk()
root.title("Inventory")

image_label = tk.Label(root)
image_label.pack()

root.bind('<space>', lambda event: display_next_image())

display_next_image()
root.mainloop()



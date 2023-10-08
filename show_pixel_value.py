import tkinter as tk
from PIL import Image, ImageTk

def get_darkness(event):
    x, y = event.x, event.y
    pixel = img.getpixel((x, y))
    darkness = sum(pixel) / 3  # Calculate average pixel value (grayscale)
    label.config(text=f"Darkness Value: {darkness:.2f}")

root = tk.Tk()
root.title("Image Darkness Viewer")

# Load the image
image = Image.open("your_image.jpg")
img = ImageTk.PhotoImage(image)

# Create a label to display the image
label = tk.Label(root, image=img)
label.pack()

# Bind mouse motion event to the get_darkness function
label.bind("<Motion>", get_darkness)

root.mainloop()

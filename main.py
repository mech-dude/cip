import customtkinter
from customtkinter import filedialog
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter
from tkinter import ttk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1000x600")

pen_color = "black"
pen_size = 1
file_path = ""

def add_image():
    global file_path
    file_path = filedialog.askopenfilename(
        initialdir="C:/Users/usuario/Pictures")
    if file_path:
        image = Image.open(file_path)
        width, height = int(image.width / 2), int(image.height / 2)
        image = ImageOps.fit(image, (width,height), Image.LANCZOS)
        canvas.config(width=image.width, height=image.height)
        image = ImageTk.PhotoImage(image)
        canvas.image = image
        canvas.create_image(0, 0, image=image, anchor="nw")

def change_color():
    global pen_color
    pen_color = colorchooser.askcolor(title="Select Pen Color")[1]

def draw(event):
    x1, y1 = (event.x - pen_size), (event.y - pen_size)
    x2, y2 = (event.x + pen_size), (event.y + pen_size)
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline="")

def clear_canvas():
    canvas.delete("all")

def apply_filter(selected_filter):
    image = Image.open(file_path)
    width, height = int(image.width / 2), int(image.height / 2)
    image = ImageOps.fit(image, (width,height), Image.LANCZOS)
    if selected_filter == "Black and White":
        image = ImageOps.grayscale(image)
    elif selected_filter == "Blur":
        image = image.filter(ImageFilter.BLUR)
    elif selected_filter == "Sharpen":
        image = image.filter(ImageFilter.SHARPEN)
    elif selected_filter == "Smooth":
        image = image.filter(ImageFilter.SMOOTH)
    elif selected_filter == "Emboss":
        image = image.filter(ImageFilter.EMBOSS)
    elif selected_filter == "Detail":
        image = image.filter(ImageFilter.DETAIL)

    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0,0, image=image, anchor="nw")

left_frame = customtkinter.CTkFrame(root, width=200, height=600)
left_frame.pack(side="left", fill="y")

canvas = customtkinter.CTkCanvas(root, width=750, height=600)
canvas.pack(side="right", fill="both", expand=True)

canvas.bind("<B1-Motion>", draw)

image_button = customtkinter.CTkButton(left_frame, text="Add Image", command=add_image)
image_button.pack(pady=15)

color_button = customtkinter.CTkButton(left_frame, text="Change Pen Color", command=change_color)
color_button.pack(pady=5)

pen_size_frame = customtkinter.CTkFrame(left_frame, fg_color="gray")
pen_size_frame.pack(pady=5)

clear_button = customtkinter.CTkButton(pen_size_frame, text="Clear", command=clear_canvas, fg_color="red")
clear_button.pack(pady=10)

filter_label = customtkinter.CTkLabel(pen_size_frame, text="Select Filter")
filter_label.pack(pady=10)


filter_combobox = ttk.Combobox(pen_size_frame, values=["Black and White", "Blur", "Emboss", "Sharpen", "Smooth", "Detail"])
filter_combobox.pack(pady=10)

filter_combobox.bind("<<ComboboxSelected>>", lambda event: apply_filter(filter_combobox.get()))



root.mainloop()
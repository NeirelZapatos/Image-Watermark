import tkinter
from tkinter import filedialog
from PIL import Image, ImageFont, ImageDraw

def open_image():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.gif")])
    if file_path:
        image = tkinter.PhotoImage(file=file_path)
        image_label.config(image=image)
        image_label.image = image

        watermark_image = Image.open(file_path)
        draw = ImageDraw.Draw(watermark_image)
        font = ImageFont.truetype("arial.ttf", 24)
        text = "Hello"

        draw.text((0, 150), text, (0, 0, 0), font=font)
        watermark_image.save("new_image.png")


window = tkinter.Tk()
window.title("Image Watermark GUI")
window.minsize(width=500, height=300)

# frame = tkinter.Frame(window)
# frame.pack()

label = tkinter.Label(text="Image Watermark GUI", font=("Arial", 24, "bold"))
label.pack()

image_label = tkinter.Label()
image_label.pack()

button = tkinter.Button(text="Select Image", command=open_image)
button.pack()

window.mainloop()

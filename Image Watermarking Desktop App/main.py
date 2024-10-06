from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter import Tk

root = Tk()
root.withdraw()
filename = filedialog.askopenfilename(initialdir='C:/Users/drago/Desktop/instagram', title='Select an Image')


def add_watermark(image, text):
    open_image = Image.open(image)

    image_width, image_height = open_image.size
    draw = ImageDraw.Draw(open_image)

    font_size = int(image_width / 4)

    font = ImageFont.truetype('arial.ttf', font_size)

    x, y = int(image_width / 2), int(image_height / 2)

    draw.text((x, y), text, font=font, fill='#FFF', stroke_width=5, stroke_fill='#222', anchor='ms')

    open_image.show()


add_watermark(filename, 'Rudix')

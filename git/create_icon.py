from PIL import Image, ImageDraw, ImageFont
import os

# Create a new image with a transparent background
size = (256, 256)
image = Image.new('RGBA', size, (0, 0, 0, 0))
draw = ImageDraw.Draw(image)

# Draw the main circle
circle_color = (13, 71, 161, 255)  # Dark blue
draw.ellipse([(20, 20), (236, 236)], fill=circle_color)

# Draw the git symbol
text_color = (255, 255, 255, 255)  # White
font_size = 150
try:
    font = ImageFont.truetype("arial.ttf", font_size)
except:
    font = ImageFont.load_default()

# Draw the text
text = ".git"
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# Center the text
x = (size[0] - text_width) // 2
y = (size[1] - text_height) // 2 - 10

draw.text((x, y), text, font=font, fill=text_color)

# Save as ICO
image.save('icon.ico', format='ICO') 
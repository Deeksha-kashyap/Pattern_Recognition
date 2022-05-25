from PIL import Image
img = Image.open('images.jpg')
img.show()
print(img.format)
print(img.mode)
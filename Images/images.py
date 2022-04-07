from PIL import Image
a=Image.open('pencils.jpg')
print(type(a))
print(a.size,a.filename,a.format_description)
a.show()
b=a.rotate(180)
b.show()
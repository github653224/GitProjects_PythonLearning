from PIL import Image
im=Image.open(r"D:\Users\Administrator\images\test.jpeg")
print(im.format,im.size,im.mode)
im.thumbnail((200,400))
im.save("4.jpg","JPEG")
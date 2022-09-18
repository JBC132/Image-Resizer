from PIL import Image

def resize_image(size1, size2):

    image = Image.open("image_before.png")
    print(f"Current size : {image.size}")

    resized_image = image.resize((size1, size2))
    resized_image.save("image_after"+ str(size1) + 'x' + str(size2) + ".png")


size1 = int(input("Width: "))
size2 = int(input("Length: "))
resize_image(size1, size2)
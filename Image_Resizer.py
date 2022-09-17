from PIL import Image

image = Image.open("image_before.png")
print(f"Current size : {image.size}")

resized_image = image.resize((500,500))
resized_image.save("image_after.png")
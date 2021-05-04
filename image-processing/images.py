from PIL import Image, ImageFilter

img = Image.open("./Pokedex/pikachu.jpg")
filtered_image = img.filter(ImageFilter.BLUR)
filtered_image.save("pikachu-1.png", "png")

greyscale_image = img.convert("L")
greyscale_image.save("pikachu-grey.png", "png")

# img.resize("","") to resize the image
# img.thumbnail() will preserve the aspect ratio

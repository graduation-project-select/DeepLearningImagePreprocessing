import os
from PIL import Image

input_dir = "input_images"
output_dir = "output_images"


def composite(cate, files):
    for el in files:
        splt = el.split(".")
        ext = splt.pop()
        if ext in "jpg jpeg png bmp JPG JPEG PNG BMP":
            image = Image.open(input_dir + '/' + cate + '/' + el)
            x, y = image.size
            if x > y:
                new_size = x
                x_offset = 0
                y_offset = int((x - y) / 2)
            elif y > x:
                new_size = y
                x_offset = int((y - x) / 2)
                y_offset = 0

            # background_color = "white"  #white, black, blue, red, ...
            new_image = Image.new("RGBA", (new_size, new_size), (255, 0, 0, 0))
            new_image.paste(image, (x_offset, y_offset))

            outfile_name = ".".join(splt) + ".png"
            new_image.save(output_dir + '/' + cate + '/' + outfile_name)


category = os.listdir(input_dir)

for cate in category:
    print(cate)
    if output_dir + '/' + cate not in os.listdir():
        os.mkdir(output_dir + '/' + cate)

    img_files = os.listdir(input_dir + '/' + cate)
    composite(cate, img_files)

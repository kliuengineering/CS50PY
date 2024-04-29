# count(argc) == 2
# output -> overlay
# resize, crop -> ImageOps.fit
# overlay -> image.paste
# save -> Image.save

# sys.exit() when:
#   1. not exactly 2 argv
#   2. input/ouput must end in .jpg .jpeg .png
#   3. input/ouput must have the same extension
#   4. input images DNE


from PIL import Image, ImageOps
import sys


def Validate(argv):
    jpg = ".jpg"
    jpeg = ".jpeg"
    png = ".png"

    if len(argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not( argv[1][-4:] == jpg or argv[1][-4:] == png or argv[1][-5:] == jpeg ):
        sys.exit("Invalid input")
    elif not( argv[2][-4:] == jpg or argv[2][-4:] == png or argv[2][-5:] != jpeg ):
        sys.exit("Invalid output")
    elif not( argv[1][-4:] == argv[2][-4:] or argv[1][-5:] == argv[2][-5:] ):
        sys.exit("Input and output have different extensions")
    else:
        pass

    INPUT_PATH = argv[1]
    OUTPUT_PATH = argv[2]

    try:
        with Image.open(INPUT_PATH) as file:
            pass
    except FileNotFoundError:
        sys.exit("Input does not exist")

    return INPUT_PATH, OUTPUT_PATH


def ImageTransform(SHIRT, INPUT_PATH, OUTPUT_PATH):
    try:
        fd_shirt = Image.open(SHIRT, mode="r", formats=None)
        fd_photo = Image.open(INPUT_PATH, mode="r", formats=None)

        #print(fd_photo.size) # 1200, 1600
        #print(fd_shirt.size) # 600, 600
        fit = fd_shirt.size

        # shirt_processed = ImageOps.fit(fd_shirt, fd_photo.size, method=0, bleed=0.0, centering=(0.5, 0.5))
        photo_processed = ImageOps.fit(fd_photo, fit) # (fd_photo, fit, method=0, bleed=0.0, centering=(0.5, 0.5))
        photo_processed.paste(fd_shirt, mask=fd_shirt) # (fd_shirt, box=None, mask=fd_shirt)

        photo_processed.save(OUTPUT_PATH)

        fd_shirt.close()
        fd_photo.close()

    except FileNotFoundError:
        sys.exit("Input does not exist")


def main():
    SHIRT = "shirt.png"
    INPUT_PATH, OUTPUT_PATH = Validate(sys.argv)
    ImageTransform(SHIRT, INPUT_PATH, OUTPUT_PATH)


if __name__ == "__main__":
    main()

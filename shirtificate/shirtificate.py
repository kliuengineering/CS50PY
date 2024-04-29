# requirements
    # 1) PDF -> portrait
    # 2) format -> A4 210x297 (mm)
    # 3) "CS50 Shirtificate" -> centered horizontally
    # 4) shirt image -> centered horizontally
    # 5) user name -> top of shirt (overlay), white


from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont


class PDF(FPDF):
    def header(self):
        # Setting font
        self.set_font("Courier", "B", 32)

        # Calculating width of title and setting cursor position:
        width = self.get_string_width(self.title) + 6
        self.set_x((210 - width) / 2)
        self.cell(
            width,
            9,
            self.title,
            border=0,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
            fill=False,
        )

    def chapter_body(self, image):
        # adds image file:
        mm_per_inch = 25.4
        dpi = 76.2
        image_width, image_height = image.size
        image_width_pt = (image_width / dpi) * mm_per_inch
        image_height_pt = (image_height / dpi) * mm_per_inch
        center_x = (self.w - image_width_pt) / 2
        center_y = (self.h - image_height_pt) / 2
        self.image(image, x=center_x, y=center_y, w=image_width_pt)

    def print_chapter(self, filepath):
        self.add_page()
        self.chapter_body(filepath)


def ImageManip(IMAGE_PATH, text):
    image = None
    font = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
    font_size = 16
    font_colour = "white"

    with Image.open(IMAGE_PATH) as img:
        new_size = ( round(img.width // 1.5), round(img.height // 1.5) )
        image = img.resize( new_size )

        # adds text to the shirt
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(font, font_size)
        text_width = draw.textlength(text, font=font)
        text_height = 0
        x = (image.width - text_width) / 2
        y = (image.height - text_height) / 3
        draw.text( (x, y), text, font=font, fill=font_colour )

    return image


def main():
    text = input("Name: ") + " took CS50"
    IMAGE_PATH = "shirtificate.png"
    pdf = PDF()
    pdf.set_title("CS50 Shirtificate")
    IMAGE_PATH_2 = ImageManip(IMAGE_PATH, text)
    pdf.print_chapter(IMAGE_PATH_2)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()


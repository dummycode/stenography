from PIL import Image
import numpy as np

class Decoder:
    def __init__(self, image):
        self.image = image.convert('RGB')

    def decode(self):
        pixels = np.array(self.image)

        changed_pixels = 0
        for i, row in enumerate(pixels):
            for j, pixel in enumerate(row):
                new_pixel = self.extract_bits(pixel)
                pixels[i][j] = new_pixel

        new_image = Image.fromarray(pixels)

        return new_image


    def extract_bits(self, pixel):
        r = int(bin(pixel[0]).replace("0b", "")[-1:] + "0000000", 2)
        g = int(bin(pixel[1]).replace("0b", "")[-1:] + "0000000", 2)
        b = int(bin(pixel[2]).replace("0b", "")[-1:] + "0000000", 2)

        return [r, g, b]


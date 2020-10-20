from PIL import Image
import numpy as np

class Encoder:
    def __init__(self, base_image, secret_image):
        self.base_image = base_image
        self.secret_image = secret_image

        # TODO: Check dimensions!

    def encode(self):
        base_pixels = np.array(base_image)
        secret_pixels = np.array(secret_image)

        new_pixels = np.ones_like(base_pixels)

        for i, row in enumerate(base_pixels):
            for j, base_pixel in enumerate(row):
                secret_pixel = secret_pixels[i][j]
                new_pixel = pack_bits(base_pixel, secret_pixel)
                new_pixels[i][j] = new_pixel

        new_image = Image.fromarray(new_pixels)

        return new_image

    def pack_bits(base_pixel, secret_pixel):
        o_r = bin(secret_pixel[0]).replace("0b", "")[:2]
        o_g = bin(secret_pixel[1]).replace("0b", "")[:2]
        o_b = bin(secret_pixel[2]).replace("0b", "")[:2]

        b_r = bin(base_pixel[0]).replace("0b", "").zfill(8)[:6]
        b_g = bin(base_pixel[1]).replace("0b", "").zfill(8)[:6]
        b_b = bin(base_pixel[2]).replace("0b", "").zfill(8)[:6]

        n_r = int(b_r + o_r, 2)
        n_g = int(b_g + o_r, 2)
        n_b = int(b_b + o_r, 2)

        return [n_r, n_g, n_b]


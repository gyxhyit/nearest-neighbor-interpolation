import numpy as np
from PIL import Image


def nearest(image_path, output_path, scale):
    img = np.array(Image.open(image_path))
    width, height, _ = img.shape
    n_width = width * scale
    n_height = height * scale
    n_img = np.zeros((n_width, n_height, 3))

    for k in range(3):
        for i in range(n_width):
            for j in range(n_height):
                n_img[i, j, k] = img[round((i - 1) / scale), round((j - 1) / scale), k]  # Mapping

    result_img = Image.fromarray(np.uint8(n_img))
    result_img.save(output_path)


# Example usage:
default_image_path = 'C:/Users/admin/Desktop/999.jpg'
default_output_path = 'default_output_path4.jpg'
scale_factor = 2

nearest(default_image_path, default_output_path, scale_factor)
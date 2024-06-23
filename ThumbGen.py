from PIL import Image
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def generate_thumbnails(directory_path: str, save_path: str):
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    for filename in os.listdir(directory_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(directory_path, filename)
            try:
                with Image.open(file_path) as img:
                    new_height = img.width
                    crop_area = (0, 0, img.width, new_height)
                    cropped_img = img.crop(crop_area)
                    cropped_img.save(os.path.join(save_path, f"cropped_{filename}"))
                    logging.info(f"Processed and saved: {filename}")
            except Exception as e:
                logging.error(f"Error processing {filename}: {e}")


if __name__ == "__main__":
    directory = input("Please enter the path of the source images folder: ")
    save = input("Please enter the path of the destination images folder: ")

    generate_thumbnails(directory, save)

    print("Image processing complete.")

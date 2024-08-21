from PIL import Image
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')


def generate_thumbnails(directory_path: str, save_path: str, custom: str):
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    for filename in os.listdir(directory_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(directory_path, filename)
            try:
                with Image.open(file_path) as img:
                    if img.height > img.width:
                        crop_area = (0, 0, img.width, img.width)
                        cropped_img = img.crop(crop_area)
                    elif img.width > img.height:
                        crop_area = (0, 0, img.height, img.height)
                        cropped_img = img.crop(crop_area)
                    else:
                        cropped_img = img
                    if custom.startswith('prefix'):
                        save_filename = f"{custom.split(' ')[1]}_{filename}.webp"
                    elif custom.startswith('suffix'):
                        save_filename = f"{filename.split('.')[0]}_{custom.split(' ')[1]}.webp"
                    else:
                        save_filename = f"cropped_{filename}.webp"

                    cropped_img.save(os.path.join(save_path, save_filename), "webp", optimize=True, quality=70)
                    logging.info(f"Processed and saved: {filename}")
            except Exception as e:
                logging.error(f"Error processing {filename}: {e}")


if __name__ == "__main__":
    directory = input("Please enter the path of the source images folder: ")
    save = input("Please enter the path of the destination images folder: ")
    customization = input("Please enter a string to append to the final filename in the format of "
                          "<prefix|suffix> <string>: ")

    generate_thumbnails(directory, save, customization)

    logging.getLogger().handlers[0].flush()
    print("Image processing complete.")

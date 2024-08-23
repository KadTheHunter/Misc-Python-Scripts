import os
import re
import logging

logger = logging.getLogger(__name__)


def generate_yaml(gal_type, image_source_folder, output_folder, alt_text):
    """
    Generates a YAML list of image files from a specified source folder,
    sorted by either their numeric prefix or modification time.

    Parameters:
    gal_type (str): The sorting type of the generated gallery. Can be 'numbered' or 'date'.
    image_source_folder (str): The path to the folder containing the image files.
    output_folder (str): The path to be used in the generated YAML.
    alt_text (str): The alt text to be used for each image in the YAML output.

    Returns:
    None
    """
    image_files = [f for f in os.listdir(image_source_folder) if os.path.isfile(os.path.join(image_source_folder, f))]

    sorted_files = []
    if gal_type in ["n", "num", "numb", "numbered"]:
        # Sort the image files by their numeric prefix
        sorted_files = sorted(image_files, key=lambda x: int(re.search(r'\d+', x).group()))
        # Sort the image files by their modification time (descending)
    elif gal_type in ["d", "dat", "date"]:
        sorted_files = sorted(image_files, key=lambda x: os.path.getmtime(os.path.join(image_source_folder, x)),
                              reverse=True)

    yaml_output = []
    for image_file in sorted_files:
        if "_Thumb" in image_file:
            continue

        full_image_path = os.path.join(output_folder, image_file)
        thumbnail_image_path = os.path.join(output_folder, f"{os.path.splitext(image_file)[0]}_Thumb.webp")

        yaml_output.append(f"- url: {full_image_path}\n  image_path: {thumbnail_image_path}\n  alt: {alt_text}")

    print("\n".join(yaml_output))


if __name__ == "__main__":
    gallery_type = input("Enter the type of gallery (numbered or date): ")
    if gallery_type not in ["n", "num", "numb", "numbered", "d", "dat", "date"]:
        logger.error("Invalid gallery type. Please enter 'numbered' or 'date'")
        exit(1)
    image_folder = input("Enter the path to the image source folder: ")
    if not os.path.exists(image_folder) or not os.path.isdir(image_folder):
        logger.error("Image folder does not exist or is not a directory.")
        exit(1)
    yaml_folder = input("Enter the path to the output folder: ")
    alt = input("Enter the alt text for the images: ")

    generate_yaml(gallery_type, image_folder, yaml_folder, alt)

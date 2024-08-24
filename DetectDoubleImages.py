from PIL import Image
import imagehash
import os


def find_duplicate_images(directory):
    image_hashes = {}

    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                img = Image.open(os.path.join(root, filename))
                img = img.convert('RGBA')
                img_hash = str(imagehash.phash(img))

                if img_hash in image_hashes:
                    image_hashes[img_hash].append(os.path.join(root, filename))
                else:
                    image_hashes[img_hash] = [os.path.join(root, filename)]

    duplicates = [filenames for filenames in image_hashes.values() if len(filenames) > 1]

    return duplicates


if __name__ == '__main__':
    direc = input("Enter the directory path: ")
    dupli = find_duplicate_images(direc)
    for duplicate_list in dupli:
        truncated_list = [os.path.relpath(os.path.normpath(filepath),
                                          start=os.path.dirname(os.path.dirname(os.path.dirname(filepath)))) for
                          filepath in duplicate_list]
        truncated_list = [path.replace('\\', '/') for path in truncated_list]
        print(truncated_list)

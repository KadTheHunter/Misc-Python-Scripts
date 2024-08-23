# Miscellaneous Python Scripts
A collection of miscellaneous Python scripts I've created for various tasks.

## Contents

### Bedrock Command Automation
[`BedrockCommandAutomation.py`](BedrockCommandAutomation.py) automates the execution of a list of commands in Minecraft Bedrock. Place your commands in the `commands = []` list, and the script will execute them one at a time. The process involves pressing the chat key, pasting the command, and pressing enter, with a slight delay between each action. Despite the rather crude method, it works effectively.

This script serves as an alternative to using RCON due to issues with color codes and long command sequences.

### Coordinate Drift Correction
[`CoordinateDriftCorrection.py`](CoordinateDriftCorrection.py) scans a specified CSV file for Coordinates in rows whose 5th and 6th columns meet certain (hardcoded) criteria, then modifies them by an amount and operation provided by the user.

This script was created to correct coordinates provided in [The Shulker Archives Database](https://kadthehunter.github.io/ShulkerArchives/database/) when I shifted multiple categories in the Map down so that the spare/blank cutout was in a more useful position.

### Deleting Duplicate Clips
[`DeletingDoubleClips.py`](DeletingDoubleClips.py) scans a specified folder and deletes files matching given patterns. 

This script was developed to help sort through old PS4/PS5 gameplay clips, many of which were duplicated during transfers between consoles, USB drives, and computers over the years.

### Thumbnail Generator
[`ThumbGen.py`](ThumbGen.py) processes images from a source folder, crops them to a square size (top-aligned), and saves them in a destination folder with the supplied prefix or suffix appended. 

This script was designed to manage a large collection of posts from 4chan, which I have been organizing and sharing on my [personal website](https://kadthehunter.github.io/greentexts/). Many images have irregular sizes, causing display issues in grids or galleries; this script addresses that by creating uniformly sized thumbnails.

### Gallery Generator
[`GalleryGen.py`](GalleryGen.py) takes a source folder of images, sorts them by the given method (numbered or descending modification date), and prints a YAML frontmatter gallery of images in the terminal using the supplied path and alt text.

This script was made to generate galleries for my personal website, specifically the [AI](https://kadthehunter.github.io/ai/) and [Greentexts](https://kadthehunter.github.io/greentexts/) pages. Because of this, the script is a bit more focused on my specific use cases (needing to sort the gallery by numbers in the file names, having `_Thumb.webp` thumbnails, etc.), but should still be usable by others.

## How to Use
1. **Bedrock Command Automation**:
    - Edit the `commands = []` list with your desired commands.
    - Run the script to automate command execution in Minecraft Bedrock.

2. **Coordinate Drift Correction**:
   - Provide the folder path, axis, operation and amount
   - Run the script to modify the coordinates to specifications

3. **Deleting Duplicate Clips**:
    - Provide the folder path and patterns to match.
    - Execute the script to delete files matching the patterns.

4. **Thumbnail Generator**:
    - Specify the source and destination folder paths, and a prefix or suffix to be appended to the filename.
    - Run the script to crop and save images in the destination folder.

## Notes
- Ensure you have the necessary Python libraries installed (`pyautogui`, `pyperclip`, `PyYaml`, `Pillow`, etc.).
- Modify the scripts as needed to fit your specific use cases.
- Contributions and suggestions are welcome to improve these scripts.

## License
This project is open-source and available under The Unlicense.
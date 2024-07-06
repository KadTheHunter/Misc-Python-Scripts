# Miscellaneous Python Scripts
A collection of miscellaneous Python scripts I've created for various tasks.

## Contents

### Bedrock Command Automation
[`BedrockCommandAutomation.py`](BedrockCommandAutomation.py) automates the execution of a list of commands in Minecraft Bedrock. Place your commands in the `commands = []` list, and the script will execute them one at a time. The process involves pressing the chat key, pasting the command, and pressing enter, with a slight delay between each action. Despite the rather crude method, it works effectively.

This script serves as an alternative to using RCON due to issues with color codes and long command sequences.

### Deleting Duplicate Clips
[`DeletingDoubleClips.py`](DeletingDoubleClips.py) scans a specified folder and deletes files matching given patterns. 

This script was developed to help sort through old PS4/PS5 gameplay clips, many of which were duplicated during transfers between consoles, USB drives, and computers over the years.

### Thumbnail Generator
[`ThumbGen.py`](ThumbGen.py) processes images from a source folder, crops them to a square size (top-aligned), and saves them in a destination folder. 

This script was designed to manage a large collection of Greentexts from 4chan, which I have been organizing and sharing on my [personal website](https://kadthehunter.github.io/greentexts/). Many images have irregular sizes, causing display issues in grids or galleries; this script addresses that by creating uniformly sized thumbnails.

## How to Use
1. **Bedrock Command Automation**:
    - Edit the `commands = []` list with your desired commands.
    - Run the script to automate command execution in Minecraft Bedrock.

2. **Deleting Duplicate Clips**:
    - Provide the folder path and patterns to match.
    - Execute the script to delete files matching the patterns.

3. **Thumbnail Generator**:
    - Specify the source and destination folder paths.
    - Run the script to crop and save images in the destination folder.

## Notes
- Ensure you have the necessary Python libraries installed (`pyautogui`, `pyperclip`, `Pillow`, etc.).
- Modify the scripts as needed to fit your specific use cases.
- Contributions and suggestions are welcome to improve these scripts.

## License
This project is open-source and available under The Unlicense.
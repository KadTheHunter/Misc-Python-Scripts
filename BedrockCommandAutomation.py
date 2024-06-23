import pyautogui
import time
import pyperclip
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

commands = []

delay = 1  # Minecraft WILL shit itself if this value is lower, because Bedrock has horrible UI design


def automate_commands(command_list: list, delay_between_commands: int):
    if not command_list:
        logging.warning("No commands provided to automate.")
        return

    for command in command_list:
        try:
            pyautogui.press('t')
            pyautogui.press('enter')
            time.sleep(0.5)
            pyperclip.copy(command)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(delay_between_commands)
            logging.info(f"Executed command: {command}")
        except Exception as e:
            logging.error(f"Error executing command '{command}': {e}")


if __name__ == "__main__":
    input("Press Enter to start the automation...")
    time.sleep(5)  # Gives user time to focus on the application
    automate_commands(commands, delay)
    logging.info("Automation process complete.")

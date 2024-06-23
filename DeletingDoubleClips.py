import os
import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def delete_specific_files(root_directory: str, patterns: list):
    if not os.path.exists(root_directory):
        logging.error(f"Provided root directory does not exist: {root_directory}")
        return

    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if any(filename.endswith(pattern) for pattern in patterns):
                file_path = os.path.join(dirpath, filename)
                try:
                    os.remove(file_path)
                    logging.info(f"Deleted: {file_path}")
                except Exception as e:
                    logging.error(f"Error deleting {file_path}: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        logging.error("Usage: python DeleteDoubleClips.py <directory> <pattern1> [<pattern2> ...]")
        sys.exit(1)

    root_directory_to_scan = sys.argv[1]

    patterns_to_match = sys.argv[2:]

    delete_specific_files(root_directory_to_scan, patterns_to_match)

    logging.info("File deletion process complete.")

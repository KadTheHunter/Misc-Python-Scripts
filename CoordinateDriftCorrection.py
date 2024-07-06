import csv


def modify_coordinates(csv_file, amount, operation, axis):
    rows = []
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        # Read all rows from the CSV and store them in a list
        for row in reader:
            rows.append(row)

        # Modify the list in memory based on the conditions
        for i, row in enumerate(rows):
            if row[5].strip() == "Kit" and row[4].strip() in ["PvP-Related", "Abuse", "Utility", "Misc. Func."]:
                coordinates = row[2].split()

                # Only check for the beginning of the coordinates string
                if coordinates[0] == '/tp' and coordinates[1] == '@s':
                    try:
                        # Select the appropriate coordinate index based on the axis ('x' -> 2, 'y' -> 3, 'z' -> 4)
                        index = {'x': 2, 'y': 3, 'z': 4}[axis]
                        current_value = float(coordinates[index])

                        # Determine the new coordinate value based on the operation
                        new_value = current_value + amount if operation == "add" else current_value - amount

                        print(
                            f"Original {axis.upper()} coordinate in row {i + 1}: {coordinates[index]}, New {axis.upper()}: "
                            f"{new_value}")  # Debug print

                        coordinates[index] = str(new_value)
                        row[2] = ' '.join(coordinates)  # Update the coordinates in the row
                        rows[i] = row  # Update the row in the list
                        print(f"Row {i + 1} modified.")  # Confirm modification
                    except ValueError:
                        print(f"Invalid coordinate value in row {i + 1}: {coordinates[index]}")

    # Write the modified list back to the CSV file
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


if __name__ == "__main__":
    database = input("Enter the path of the CSV file to modify: ").strip('"').strip()

    xyz = input("Enter the axis to modify (x, y, or z): ").strip().lower()
    while xyz not in ["x", "y", "z"]:
        xyz = input("Invalid axis. Please enter 'x', 'y', or 'z': ").strip().lower()

    op = input("Enter the operation (add or subtract): ").strip().lower()
    while op not in ["add", "subtract"]:
        op = input("Invalid operation. Please enter 'add' or 'subtract': ").strip().lower()

    try:
        num = float(input(f"Enter the amount to modify the {xyz.upper()} coordinate by: ").strip())
        modify_coordinates(database, num, op, xyz)
    except ValueError:
        print("Invalid amount. Please enter a numerical value.")

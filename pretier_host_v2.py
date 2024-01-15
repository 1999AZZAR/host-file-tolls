import re

def update_hosts_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        updated_lines = []

        for line in lines:
            if line.startswith("#"):
                continue
            elif re.match(r"# \[.*\]", line) or line.strip() == '':
                continue
            else:
                updated_line = line.replace("127.0.0.1", "0.0.0.0")
                updated_lines.append(updated_line)

        with open(file_path, 'w') as file:
            file.writelines(updated_lines)

        print("Update successful.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to your text file
file_path = "/home/azzar/Downloads/host files/spotofy.txt"

# Call the function to update the hosts file
update_hosts_file(file_path)

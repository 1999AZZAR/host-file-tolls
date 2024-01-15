def combine_and_remove_duplicates(input_files, output_file):
    try:
        unique_lines = set()

        for file_path in input_files:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if line.startswith("0.0.0.0") and line.strip() != '':
                        unique_lines.add(line)

        unique_lines = sorted(list(unique_lines))

        with open(output_file, 'w') as output:
            output.writelines(unique_lines)

        print("Combination, removal of duplicates, and sorting successful.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the paths to your input text files
input_files = ["/home/azzar/Downloads/host files/yoyo.txt", "/home/azzar/Downloads/host files/spotofy.txt", "/home/azzar/Downloads/host files/hosts.txt", "/home/azzar/Downloads/host files/adaway.txt", "/home/azzar/Downloads/host files/GoodbyeAds.txt"]

# Specify the path to your output text file
output_file = "/home/azzar/Downloads/host files/new_host.txt"

# Call the function to combine and remove duplicates
combine_and_remove_duplicates(input_files, output_file)


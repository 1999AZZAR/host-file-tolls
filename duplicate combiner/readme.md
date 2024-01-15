# SimpleDuplicateCombiner

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Example](#example)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

SimpleDuplicateCombiner is a Python script designed to efficiently combine multiple text files, remove duplicate lines, and produce a sorted output file. This tool is particularly useful when dealing with host files or similar configurations where duplicate entries need to be eliminated.

## Features

- Combines content from multiple input text files.
- Removes duplicate lines.
- Produces a sorted output file.
- Robust error handling for a smooth user experience.

## Installation

No installation is required. Simply download the script and run it using Python.

```bash
python simple_duplicate_combiner.py
```

## Usage

The script takes a list of input file paths and an output file path as parameters. Ensure that the input files exist and the output file path is writable.

```python
# Specify the paths to your input text files
input_files = ["/path/to/file1.txt", "/path/to/file2.txt", "/path/to/file3.txt"]

# Specify the path to your output text file
output_file = "/path/to/output.txt"

# Call the function to combine and remove duplicates
combine_and_remove_duplicates(input_files, output_file)
```

## Example

In this example, we have three input files (`file1.txt`, `file2.txt`, and `file3.txt`). The script will combine their content, remove duplicate lines, and generate a sorted output file (`output.txt`).

```python
# Specify the paths to your input text files
input_files = ["/path/to/file1.txt", "/path/to/file2.txt", "/path/to/file3.txt"]

# Specify the path to your output text file
output_file = "/path/to/output.txt"

# Call the function to combine and remove duplicates
combine_and_remove_duplicates(input_files, output_file)
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

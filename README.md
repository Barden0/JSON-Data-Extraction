# JSON Data Extraction

This Python script allows you to extract specific data from a JSON file. I used JSON data stored in a text file that contained values assigned to "id" that I wanted to extract.

## Prerequisites

- Python 3.x installed on your system

## Getting Started

1. **Clone the repository:**

   ```
   git clone https://github.com/Barden0/JSON-Data-Extraction
   cd json-data-extraction
   ```

2. **Run the script:**

   ```
   python extract_ids.py
   ```

   The script will prompt you to enter the path to the text file containing the JSON data. It will then extract and display all the "id" values found in the file.

## How It Works

The script uses regular expressions to find all occurrences of `"id": "12345"`-like patterns in the text file. It extracts the "id" values and prints them to the console. 
You can edit the script to find specific values you want.

## Contributing

If you find any issues with the script or have suggestions for improvements, feel free to open an issue or create a pull request. Contributions are welcome!

import re

def extract_ids_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            ids = re.findall(r'"id":\s*"(\d+)"', data)
            return ids
    except FileNotFoundError:
        return "File not found."

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    extracted_ids = extract_ids_from_file(file_path)
    if extracted_ids:
        print("Extracted IDs:")
        for id_number in extracted_ids:
            print("id =", id_number)
    else:
        print("No 'id' values found in the file.")

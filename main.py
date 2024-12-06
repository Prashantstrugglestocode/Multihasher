import hashlib
from base64 import b64decode

hash_string = 'Y2FybG9zOjQ2Zjk0YzhkZTE0ZmIzNjY4MDg1MDc2OGZmMWI3ZjJh'
list1 = []

# Read file contents into list1
with open("passwords.txt", "r") as file:
    text = file.readlines()

for line in text:
    new_line = line.strip()  # Remove any trailing newline or spaces
    list1.append(new_line)

print(f"Passwords read from file: {list1}")

def convert_to_base64(hash_str: str) -> str:
    """Decode a Base64 encoded string."""
    try:
        decoded_bytes = b64decode(hash_str)
        decoded_string = decoded_bytes.decode("utf-8")
        print(f"The value after Base64 decode is: {decoded_string}")
        return decoded_string
    except Exception as e:
        print(f"Error decoding Base64: {e}")
        return ""

def extract_md5_part(decoded_str: str) -> str:
    """Extract the MD5 part from the decoded string."""
    try:
        md5_string = decoded_str.split(":", 1)[1]
        print(f"The MD5 part in the string is: {md5_string}")
        return md5_string
    except IndexError:
        print("Error: Unable to extract MD5 part from the string.")
        return ""

def find_string_for_md5(hash_list: list[str], md5_value: str) -> str:
    """Find the string that matches the given MD5 hash."""
    for item in hash_list:
        # Generate MD5 hash for each string
        md5_hash = hashlib.md5(item.encode()).hexdigest()
        if md5_hash == md5_value:
            print(f"Match found! The string is: {item}")
            return item
    print("No matching string found.")
    return None

# Process the hash and find the string
base64_hash = convert_to_base64(hash_string)  # Decode the Base64 hash
md5_hash = extract_md5_part(base64_hash)  # Extract the MD5 part
matching_string = find_string_for_md5(list1, md5_hash)  # Find the string for the MD5 hash

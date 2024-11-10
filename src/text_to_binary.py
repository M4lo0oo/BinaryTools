def text_to_binary(text):
    """Convert a string of text to binary."""
    binary_code = ''.join(format(ord(char), '08b') for char in text)
    return binary_code

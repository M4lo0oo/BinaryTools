def binary_to_text(binary_code):
    """Convert binary code back to text."""
    text = ''.join(chr(int(binary_code[i:i+8], 2)) for i in range(0, len(binary_code), 8))
    return text

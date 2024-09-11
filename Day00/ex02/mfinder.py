import sys

def check_pattern(image):
    """Checks if the image has the correct 3x5 size and contains the correct 'M' pattern."""
    # The expected positions of '*' in the M pattern
    m_pattern = [
        [0, 4],  # * positions in row 1
        [0, 1, 3, 4],  # * positions in row 2
        [0, 2, 4]  # * positions in row 3
    ]
    
    # Check if the input is 3x5
    if len(image) != 3 or any(len(line) != 5 for line in image):
        return "Error"
    
    # Validate the M pattern
    for row_index, row in enumerate(image):
        for col_index, char in enumerate(row):
            if col_index in m_pattern[row_index]:  # If it should be a '*'
                if char != '*':
                    return "False"
            else:  # If it should not be a '*'
                if char == '*':
                    return "False"
    
    return "True"

if __name__ == "__main__":
    # Read all lines from standard input (no limit on number of lines)
    image = [line.strip() for line in sys.stdin]
    
    # Check the pattern and print the result
    result = check_pattern(image)
    print(result)

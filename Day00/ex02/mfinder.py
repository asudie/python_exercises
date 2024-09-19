import sys

def check_pattern(image):
    m_pattern = [
        [0, 4],
        [0, 1, 3, 4],
        [0, 2, 4]
    ]
    
    if len(image) != 3 or any(len(line) != 5 for line in image):
        return "Error"
    
    for row_index, row in enumerate(image):
        for col_index, char in enumerate(row):
            if col_index in m_pattern[row_index]:
                if char != '*':
                    return "False"
            else:
                if char == '*':
                    return "False"
    
    return "True"

if __name__ == "__main__":
    image = [line.strip() for line in sys.stdin]
    
    result = check_pattern(image)
    print(result)

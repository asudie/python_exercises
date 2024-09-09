import sys

def validate_line(line):
    line = line.strip()
    return len(line) == 32 and line.startswith('00000') and not line.startswith('000000')

def main():
    if len(sys.argv) < 2:
        print("Please provide the number of lines to process.")
        sys.exit(1)
    
    try:
        num_lines = int(sys.argv[1])
    except ValueError:
        print("The argument should be a valid number.")
        sys.exit(1)
    
    processed_lines = 0

    # Read from stdin line by line
    for line in sys.stdin:
        if processed_lines >= num_lines:
            break
        
        if validate_line(line):
            print(line.strip())
            processed_lines += 1

if __name__ == "__main__":
    main()

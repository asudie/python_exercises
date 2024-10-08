def get_user_input(answers):
    while True:
        try:
            # Display answer choices
            for idx, answer in enumerate(answers, start=1):
                print(f"{idx}. {answer}")
            
            # Get user's choice
            user_input = int(input("Choose your answer by entering the corresponding number: "))
            
            # Validate if the input is within the valid range
            if 1 <= user_input <= len(answers):
                return user_input
            else:
                print(f"Invalid input. Please choose a number between 1 and {len(answers)}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

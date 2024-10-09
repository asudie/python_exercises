def get_user_input(answers):
    """
    Prompt the user to select an answer from the provided list of options.

    This function displays a list of possible answers, numbered sequentially, and repeatedly prompts the user to choose an 
    answer by entering the corresponding number. It validates the input to ensure it's an integer within the range of options.

    Args:
        answers (list): A list of answer choices presented to the user.

    Returns:
        int: The number corresponding to the user's selected answer.

    Notes:
        - The function will continue to prompt the user until a valid selection is made.
        - It handles non-integer inputs by prompting the user to re-enter a valid integer.
        - It also ensures the selected number is within the range of the available answers.
    """
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

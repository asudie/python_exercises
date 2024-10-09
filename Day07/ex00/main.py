import json
from .logic import decide
from .utils import get_user_input

def load_questions(file_path='questions.json'):
    """
    Load questions from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing questions. Defaults to 'questions.json'.

    Raises:
        FileNotFoundError: If the file is not found.
        ValueError: If the file is empty or contains invalid JSON.

    Returns:
        list: A list of questions loaded from the JSON file.
    """
    try:
        with open(file_path, 'r') as f:
            questions = json.load(f)
            if not questions:
                raise ValueError("The question file is empty.")
            return questions
    except FileNotFoundError:
        raise FileNotFoundError("The 'questions.json' file is missing.")
    except json.JSONDecodeError:
        raise ValueError("The 'questions.json' file contains invalid JSON.")


def validate_physiological_data(data, min_value, max_value, label):
    """
    Validate physiological data against the given range.

    Args:
        data (str): The input data as a string, which will be converted to an integer.
        min_value (int): The minimum allowed value for the physiological data.
        max_value (int): The maximum allowed value for the physiological data.
        label (str): The label describing the data (e.g., "Respiration").

    Raises:
        ValueError: If the data cannot be converted to an integer or if the value is outside the given range.

    Returns:
        int: The validated integer value of the physiological data.
    """
    try:
        value = int(data)
        if value < min_value or value > max_value:
            raise ValueError(f"{label} must be between {min_value} and {max_value}.")
        return value
    except ValueError:
        raise ValueError(f"Invalid input for {label}. Please enter an integer between {min_value} and {max_value}.")


def main():
    """
    Main function that runs the Voight-Kampff test.

    This function loads questions from a file, collects user input for each question, and 
    gathers physiological data such as respiration, heart rate, blushing level, and pupillary dilation.
    The function then uses the collected data to decide whether the subject is human or a replicant.

    Raises:
        Exception: If any error occurs during the process, it will be caught and printed.
    """
    try:
        questions = load_questions()
        user_responses = []
        for question in questions:
            print(question['question'])
            response = get_user_input(question['answers'])
            user_responses.append(response)

        respiration = validate_physiological_data(input("Respiration (BPM): "), 12, 20, "Respiration")
        heart_rate = validate_physiological_data(input("Heart rate: "), 60, 100, "Heart rate")
        blushing_level = validate_physiological_data(input("Blushing level (1-6): "), 1, 6, "Blushing level")
        pupil_size = validate_physiological_data(input("Pupillary dilation (mm): "), 2, 8, "Pupil size")

        result = decide(user_responses, respiration, heart_rate, blushing_level, pupil_size)
        if result:
            print("Subject is a human.")
        else:
            print("Subject is a replicant.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

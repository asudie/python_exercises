import json
from .logic import decide
from .utils import get_user_input

def load_questions(file_path='questions.json'):
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
    try:
        value = int(data)
        if value < min_value or value > max_value:
            raise ValueError(f"{label} must be between {min_value} and {max_value}.")
        return value
    except ValueError:
        raise ValueError(f"Invalid input for {label}. Please enter an integer between {min_value} and {max_value}.")

def main():
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

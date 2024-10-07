import json
from logic import decide
from utils import get_user_input

def load_questions():
    with open('questions.json', 'r') as f:
        return json.load(f)

def main():
    questions = load_questions()
    user_responses = []
    for question in questions:
        print(question['question'])
        response = get_user_input(question['answers'])
        user_responses.append(response)

    respiration = int(input("Respiration (BPM): "))
    heart_rate = int(input("Heart rate: "))
    blushing_level = int(input("Blushing level (1-6): "))
    pupil_size = int(input("Pupillary dilation (mm): "))

    result = decide(user_responses, respiration, heart_rate, blushing_level, pupil_size)
    if result:
        print("Subject is a human.")
    else:
        print("Subject is a replicant.")

if __name__ == "__main__":
    main()

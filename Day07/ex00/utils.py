def get_user_input(choices):
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")
    selected = int(input("Choose an option: "))
    return choices[selected - 1]

def is_exit_command(question):
    return question.strip().lower() == "exit"

def is_empty_input(question):
    return not question.strip()


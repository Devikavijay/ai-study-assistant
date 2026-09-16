from utils import is_exit_command, is_empty_input

def test_exit_command():
    assert is_exit_command("exit") 
    assert is_exit_command(" Exit ")
    assert not is_exit_command("What is AI?")

def test_empty_input():
    assert is_empty_input("")
    assert is_empty_input("  ")
    assert not is_empty_input("What is AI?")
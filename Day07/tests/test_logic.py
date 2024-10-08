import pytest
import json
from ex00.main import load_questions, validate_physiological_data

# Modified load_questions to accept a file path for testing purposes
def test_load_questions_empty_file(tmp_path):
    # Create a temporary empty JSON file
    empty_file = tmp_path / "questions.json"
    empty_file.write_text("[]")
    
    # Modify load_questions to accept a file path for testing
    with pytest.raises(ValueError, match="The question file is empty."):
        load_questions(str(empty_file))

def test_load_questions_invalid_json(tmp_path):
    # Create a temporary invalid JSON file
    invalid_file = tmp_path / "questions.json"
    invalid_file.write_text("{invalid_json}")
    
    with pytest.raises(ValueError, match="The 'questions.json' file contains invalid JSON."):
        load_questions(str(invalid_file))

def test_load_questions_file_not_found():
    with pytest.raises(FileNotFoundError, match="The 'questions.json' file is missing."):
        load_questions("non_existent_file.json")

def test_validate_physiological_data_valid():
    assert validate_physiological_data("15", 12, 20, "Respiration") == 15

def test_validate_physiological_data_out_of_range():
    with pytest.raises(ValueError, match="Invalid input for Respiration. Please enter an integer between 12 and 20"):
        validate_physiological_data("10", 12, 20, "Respiration")

def test_validate_physiological_data_invalid_type():
    with pytest.raises(ValueError, match="Invalid input for Respiration."):
        validate_physiological_data("abc", 12, 20, "Respiration")

# python -m pytest tests/

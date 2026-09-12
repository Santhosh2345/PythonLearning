from validators import is_valid_status_code, is_valid_response_time

def test_valid_status_codes():
    assert is_valid_status_code(200) == True
    assert is_valid_status_code(201) == True
    assert is_valid_status_code(204) == True

def test_invalid_status_codes():
    assert is_valid_status_code(404) == False
    assert is_valid_status_code(500) == True

def test_response_time_within_limit():
    assert is_valid_response_time(300) == True

def test_response_time_exceeds_limit():
    assert is_valid_response_time(600) == False
import response_checks
import pytest

def test_check_response_valid():
    #   - a valid, fast response (should return True)
    assert response_checks.check_response(200, 500) == True

def test_check_response_valid_false():
    #   - a valid, slow response (should return False)
    assert response_checks.check_response(201, 501) == False

#   - an invalid status code (should raise ValueError — use pytest.raises)
def test_check_statusCode_invalid():
    #   - a negative response time (should raise ValueError)
    with pytest.raises(ValueError):
        response_checks.check_response(300, 501)

def test_check_responseTime_invalid():
    #   - a negative response time (should raise ValueError)
    with pytest.raises(TypeError):
        response_checks.check_response(201, -501)


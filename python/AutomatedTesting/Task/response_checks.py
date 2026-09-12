# In a file called response_checks.py:
def check_response(status_code, response_time_ms):
    if status_code not in [200, 201, 204]:
        raise ValueError(f"Invalid status code: {status_code}")
    if response_time_ms < 0:
        raise ValueError("Response time cannot be negative")
    return response_time_ms <= 500   # returns True if "fast enough", False otherwise

# In test_response_checks.py:
# Write tests covering:
#   - a valid, fast response (should return True)
#   - a valid, slow response (should return False)
#   - an invalid status code (should raise ValueError — use pytest.raises)
#   - a negative response time (should raise ValueError)
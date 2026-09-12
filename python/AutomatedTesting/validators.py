def is_valid_status_code(code):
    return code in [200, 201, 204]

def is_valid_response_time(time_ms, max_allowed=500):
    return time_ms <= max_allowed
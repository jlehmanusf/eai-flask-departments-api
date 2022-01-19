def successful_response():
    return {"response": 0, "responseMessage": "Data retrieved successfully", "data": "", "errors": []}


def error_response():
    return {"response": -1, "responseMessage": "Unsuccessful", "data": "", "errors": []}

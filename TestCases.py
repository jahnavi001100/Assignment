import requests
from pact_python.consumer import Consumer

consumer = Consumer('Dashboard')

def test_get_employees():
    # Create a mock server for the Employee service
    pact = consumer.start_mocking()

    # Define the expected response
    expected_response = {
        "employees": [
            {"id": 1, "name": "John Doe"},
            {"id": 2, "name": "Jane Doe"},
        ]
    }

    # Make the request to the mock server
    response = requests.get('http://localhost:8080/employees')

    # Verify the response
    assert response.status_code == 200
    assert response.json() == expected_response

    # Write the pact
    consumer.pact_with(provider).publish_pact()

if __name__ == '__main__':
    test_get_employees()

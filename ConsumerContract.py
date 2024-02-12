import pytest
import requests
from pact_python.matches import like
from pact_python.consumer import Consumer

consumer = Consumer('Dashboard')

@consumer.has_pact_with('Employee_Service', port=8080)
def test_get_all_employees(pact):
    # Define the interaction
    interaction = Interaction()
    interaction.get_path('/employees')
    interaction.with_state('there are some employees')
    interaction.will_respond_with(200, body={
        'employees': [
            {'id': like(1), 'name': like('John Doe'), 'age': like(30), 'department': like('HR')},
            {'id': like(2), 'name': like('Jane Doe'), 'age': like(25), 'department': like('IT')},
        ]
    })

    # Verify the interaction
    pact.given('there are some employees').
        upon_receiving('a request to get all employees').
        with_request('GET', '/employees').
        will_respond_with(200, body={'employees': [
            {'id': 1, 'name': 'John Doe', 'age': 30, 'department': 'HR'},
            {'id': 2, 'name': 'Jane Doe', 'age': 25, 'department': 'IT'},
        ]})

if __name__ == '__main__':
    consumer.pact_with().assert_pact()

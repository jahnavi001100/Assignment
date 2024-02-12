import requests
from pact_python.provider import Provider
from pact_python.matches import like

provider = Provider('Employee_Service')

@provider.given('there are some employees')
def given_employees():
    # Set up the state of the provider
    pass

@provider.upon_receiving('a request to get all employees')
def upon_receiving_get_all_employees():
    # Define the interaction
    provider.given('there are some employees')
    provider.upon_receiving('a request to get all employees')
    provider.with_request('GET', '/employees')
    provider.will_respond_with(200, body={
        'employees': [
            {'id': like(1), 'name': like('John Doe'), 'age': like(30), 'department': like('HR')},
            {'id': like(2), 'name': like('Jane Doe'), 'age': like(25), 'department': like('IT')},
        ]
    })

if __name__ == '__main__':
    provider.start_mocking()

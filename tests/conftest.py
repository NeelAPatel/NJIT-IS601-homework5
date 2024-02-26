# pylint: disable=unnecessary-dunder-call, invalid-name, line-too-long, trailing-whitespace, missing-final-newline
# conftest.py
""" This File tests the configuration of the faker library and generates randomized parameters for testing """
from decimal import Decimal
import pytest
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()


@pytest.fixture
def num_records(request):
    """Provide the number of records as specified by the command-line option."""
    return request.config.getoption("--num_records")

def pytest_addoption(parser):
    """Enables --num_records as an optional flag for pytest"""
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def generate_test_data(num_records): 
    """ Generates testing parameterized data for calculation"""
    # uses functions imported from calc.operations to randomly generate one of the ops
    operation_maps = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    #For every record we need to generate
    for i in range(num_records): 
        #Generate two random numbers;
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2))
        # generate operation
        operation_name = fake.random_element(elements=list(operation_maps.keys())) #returns index
        operation_func = operation_maps[operation_name]

        #Check if 'divide' and b=0; if true, then expect error
        if operation_func == divide:
            b = Decimal('1') if b == Decimal('0') else b # Set b value to 1 so it doesn't immediately fail

        # Fall back check incase b somehow changes
        try:
            # IF b somehow is still 0 + divide... 
            if operation_func == divide and b == Decimal('0'):
                expected = "ZeroDivisionError" #Expect an error to show
            else:
                expected = operation_func(a, b) #otherwise perform function as intended
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        # Yield executes a generator function generate the below variables (still confused on this)
        #Generates for each record in num_records
        yield a, b, operation_name, operation_func, expected

def pytest_generate_tests(metafunc):
    """ Generates tests based on test-data """
    # Check if the test is expecting any of the dynamically generated fixtures
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        # Adjust the parameterization to include both operation_name and operation for broad compatibility
        # Ensure 'operation_name' is used for identifying the operation in Calculator class tests
        # 'operation' (function reference) is used for Calculation class tests.
        parameters = list(generate_test_data(num_records))
        # Modify parameters to fit test functions' expectations
        modified_parameters = [(a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)
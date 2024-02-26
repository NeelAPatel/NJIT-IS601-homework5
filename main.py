# pylint: disable=unnecessary-dunder-call, invalid-name, line-too-long, trailing-whitespace, missing-final-newline
import sys
from decimal import Decimal, InvalidOperation
from calculator import Calculator

def run_calculations(a:Decimal, b:Decimal, operation_name:str):
    # uses functions imported from calc.operations to randomly generate one of the ops
    operation_maps = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }


    # Unified error handling for decimal conversion
    try:
        #Test if a and b can be set to decimal
        a_decimal = Decimal(a)
        b_decimal = Decimal(b) 
        
        #Use .get to handle unknown operations from the dictionary
        curr_operation = operation_maps.get(operation_name) 
        
        if curr_operation:
            print(f"Result: {a} {operation_name} {b} = {curr_operation(a_decimal, b_decimal)}")
        else:
            print(f"Unknown operation: {operation_name}")

    except InvalidOperation: # not a number
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError: # Dividing by zero
        print("Error: Division by zero.")
    except Exception as e: # Catch-all for unexpected errors
        print(f"An error occurred: {e}")

def main():
    # Control the input
    # 4 inputs only 
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)
    
    #Set arguments
    a = sys.argv[1]
    b = sys.argv[2]
    operation = sys.argv[3]  
    
    #Take system args and run as a function
    run_calculations(a, b, operation)

if __name__ == '__main__':
    main()
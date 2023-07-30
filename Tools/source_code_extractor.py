import re

def calculate_N1_for_each_function(file_path):
    with open(file_path, 'r') as f:
        source_code = f.read()

    # Split the source code into functions
    contracts = re.split(r'\bcontract\b', source_code)

    results = {}

    for i, contract in enumerate(contracts):
        # Skip the first split result, as it is the pragma
        if i == 0:
            continue

        print(contract)
        print("---------")
        
    


calculate_N1_for_each_function("..\\Contracts\\Contract2.sol")

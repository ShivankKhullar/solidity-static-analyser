import re

def extract_contract_source_code(file_path):
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
        
    


extract_contract_source_code("..\\Contracts\\Contract2.sol")

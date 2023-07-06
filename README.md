## Project Documentation

### Prerequisites
- Python 3.x installed
- Git installed

### Setting Up the Project

1. Clone the project repository:
   ```
   git clone https://github.com/ShivankKhullar/Static-Analysers-Research
   ```

2. Create a virtual environment:
   ```
   python -m venv myenv
   // myenv is just a name.
   ```

3. Activate the virtual environment:
   - For Windows:
     ```
     myenv\Scripts\activate
     ```
   - For macOS/Linux:
     ```
     source myenv/bin/activate
     ```

4. Install project dependencies:
   ```
   pip install slither
   pip install solc-select

   // If solc-select gives troubles try running - npm install -g solc

   // In the future we can create a text file with all dependencies.
   // pip install -r requirements.txt
   ```


### Using `solc-select`

`solc-select` is a command-line tool that allows you to manage and switch between different versions of the Solidity compiler.


#### Selecting a Solidity Version

1. Install a specific Solidity version:
   ```
   solc-select install <version>
   ```
   Replace `<version>` with the desired Solidity version, e.g., `0.8.0`.

2. Use a specific Solidity version:
   ```
   solc-select use <version>
   ```
   Replace `<version>` with the desired Solidity version, e.g., `0.8.0`.

### Running the Program

1. Ensure that the desired Solidity version is selected using `solc-select`.

2. Execute the program:
   ```
   python count_contracts.py
   ```

The program will scan the `Contracts` directory, count the number of contracts in each Solidity file, and display the results.

### Additional Notes

- To deactivate the virtual environment, run:
  ```
  deactivate
  ```

- If you encounter any issues with `solc-select`, refer to the `solc-select` documentation for troubleshooting and advanced usage instructions.

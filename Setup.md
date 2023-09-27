## Getting Started with the Static Analyser Project

### Prerequisites
- **Python**: Ensure you have Python 3.x installed. You can verify this with `python --version`.
- **Git**: Ensure Git is installed. You can verify this with `git --version`.

### Setting Up the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ShivankKhullar/Static-Analysers-Research
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv myenv
   ```
   > Note: `myenv` is just a name. You can choose any name for your virtual environment.

3. **Activate the Virtual Environment**:
   - For Windows:
     ```bash
     .\myenv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     source myenv/bin/activate
     ```

4. **Install Project Dependencies**:
   ```bash
   pip install slither
   pip install solc-select
   ```
   > If `solc-select` gives troubles, try running `npm install -g solc`.

   > In the future, we might provide a `requirements.txt` file to simplify dependency installation: `pip install -r requirements.txt`.

### Working with `solc-select`

`solc-select` is a tool that lets you manage and switch between different versions of the Solidity compiler. The version switching has been automated within the project, but you might need the initial setup.

#### Selecting a Solidity Version

1. **Install a Specific Version**:
   ```bash
   solc-select install <version>
   ```
   Replace `<version>` with the desired Solidity version, e.g., `0.8.0`.

2. **Switch to a Specific Version**:
   ```bash
   solc-select use <version>
   ```
   Replace `<version>` with the desired Solidity version, e.g., `0.8.0`.

### Running the Program

1. Ensure the desired Solidity version is active using `solc-select`.

2. **Execute the Program**:
   ```bash
   python count_contracts.py
   ```

### Additional Notes

- To deactivate the virtual environment, simply run:
  ```bash
  deactivate
  ```

## Useful Resources 📚

For those interested in diving deeper into the technologies and concepts used in this project, here are some valuable resources:

- **Slither API**: A static analysis framework for Solidity that converts Ethereum smart contracts into Python objects for easy metric extraction. [Learn more](https://crytic.github.io/slither/slither.html)

- **solc-select**: A tool by Crytic to switch between different versions of the Solidity compiler easily. [GitHub Repository](https://github.com/crytic/solc-select)

- **ANTLR 4**: A powerful parser generator for reading, processing, executing, or translating structured text or binary files. [Documentation](https://github.com/antlr/antlr4/blob/master/doc/index.md)

- **Control Flow Graph (CFG)**: An essential concept in software engineering that represents the flow of a program. [Learn more](https://www.geeksforgeeks.org/software-engineering-control-flow-graph-cfg/)

- **Halstead's Software Metrics**: A set of software metrics that provide a theoretical foundation for the empirical studies on software complexity. [Learn more](https://www.geeksforgeeks.org/software-engineering-halsteads-software-metrics/)

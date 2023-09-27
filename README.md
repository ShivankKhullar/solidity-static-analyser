# Solidity Static Analyser 🛡️

Welcome to the Solidity Static Analyser project. This tool is designed to analyze Solidity smart contracts to uncover potential vulnerabilities, ensuring the robustness and security of Ethereum projects.

## Introduction 🌟

Developed by [Shivank Khullar](https://github.com/ShivankKhullar) during a summer internship at Brunel University, this project was guided by [Dr. Rumyana Neykova](https://www.brunel.ac.uk/people/rumyana-neykova). The collaboration aimed to create a tool that not only identifies vulnerabilities in smart contracts but also serves as a foundation for future research papers in the domain.

## Key Achievements 🏆

- **Metrics Extraction**: The current version of the tool is primarily focused on extracting a variety of metrics from smart contracts, including Halstead, OOP metrics, and count metrics.
- **Rapid Development**: A significant accomplishment, especially considering the project's development spanned just one month.

## Purpose & Future Directions 🚀

- **Insightful Analysis**: Beyond its immediate functionality, the insights derived from this tool will contribute to forthcoming research papers, shedding light on the intricacies of smart contract vulnerabilities.
- **Comprehensive Dashboard**: The primary goal is to provide clients with a comprehensive dashboard to assess the quality of Ethereum projects.
- **Ongoing Development**: The analysis part, aimed at interpreting the extracted metrics to identify vulnerabilities, is currently under development and will be a part of future releases.

Certainly! Here's the "Technologies Used" section with the updated information:

## Technologies Used 💼

- **Python**: The primary language used for developing the project, which required the application of various data structures and algorithms.

- **ANTLR Lexer**: Utilized to tokenize Solidity code, aiding in the preliminary stages of analysis. [Learn more](https://www.antlr.org/)

- **Slither API**: This API was employed to convert Solidity programs into objects, allowing for the extraction of vital information. Specifically, it was used to access the Control Flow Graph (CFG) of the smart contracts, which was instrumental in extracting critical metrics and insights. [Learn more](https://crytic.github.io/slither/slither.html)

## Getting Started 🚀

For detailed instructions on setting up and running the project, please refer to the [How to Setup the Project](Setup.md) guide.

// Specifies the version of Solidity that the code is written in
pragma solidity ^0.8.0;

// Defines a contract named `SimpleStorage`
contract SimpleStorage {
    // Declares a state variable `number` of type `uint` (unsigned integer)
    uint private number;

    // Defines a function `store` that accepts one argument `num` and stores it in the `number` state variable
    function store(uint num) public {
        number = num;
    }

    // Defines a function `retrieve` that returns the value of the `number` state variable
    function retrieve() public view returns (uint){
        return number;
    }
}


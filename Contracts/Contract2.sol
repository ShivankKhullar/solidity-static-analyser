// Contract 1
pragma solidity ^0.8.0;

contract Contract1 {
    uint public contract1Value;
    
    constructor(uint _value) {
        contract1Value = _value;
    }
    
    function setValue(uint _newValue) public {
        contract1Value = _newValue;
    }
    
    function getValue() public view returns (uint) {
        return contract1Value;
    }
}

// Contract 2
contract Contract2 {
    string public contract2Message;
    
    constructor(string memory _message) {
        contract2Message = _message;
    }
    
    function setMessage(string memory _newMessage) public {
        contract2Message = _newMessage;
    }
    
    function getMessage() public view returns (string memory) {
        return contract2Message;
    }
}

// Contract 3
contract Contract3 {
    address public owner;
    
    constructor() {
        owner = msg.sender;
    }
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function.");
        _;
    }
    
    function transferOwnership(address _newOwner) public onlyOwner {
        owner = _newOwner;
    }
}

// Contract 4
contract Contract4 {
    uint public contract4Value;
    
    function setValue(uint _newValue) public {
        contract4Value = _newValue;
    }
    
    function getValue() public view returns (uint) {
        return contract4Value;
    }
}


pragma solidity ^0.8.0;

// Contract1 does not interact with any other contracts, so its CBO is 0.
contract Contract1 {
    uint256 public data;

    function setData(uint256 _data) public {
        data = _data;
    }
}

// Contract2 interacts with Contract1, so its CBO is 1.
contract Contract2 {
    Contract1 public contract1;

    constructor(Contract1 _contract1) public {
        contract1 = _contract1;
    }

    function setData(uint256 _data) public {
        contract1.setData(_data);
    }
}

// Contract3 interacts with both Contract1 and Contract2, so its CBO is 2.
contract Contract3 {
    Contract1 public contract1;
    Contract2 public contract2;

    constructor(Contract1 _contract1, Contract2 _contract2) public {
        contract1 = _contract1;
        contract2 = _contract2;
    }

    function setData(uint256 _data) public {
        contract1.setData(_data);
        contract2.setData(_data);
    }
}

// Contract4 interacts with all the other contracts, so its CBO is 3.
contract Contract4 {
    Contract1 public contract1;
    Contract2 public contract2;
    Contract3 public contract3;

    constructor(Contract1 _contract1, Contract2 _contract2, Contract3 _contract3) public {
        contract1 = _contract1;
        contract2 = _contract2;
        contract3 = _contract3;
    }

    function setData(uint256 _data) public {
        contract1.setData(_data);
        contract2.setData(_data);
        contract3.setData(_data);
    }
}
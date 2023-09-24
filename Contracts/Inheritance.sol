// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Base {
    function doSomething() public pure returns (uint) {
        return 1;
    }
}

contract Derived1 is Base {
    function doSomethingElse() public pure returns (uint) {
        return 2;
    }
}

contract Derived2 is Derived1 {
    function doAnotherThing() public pure returns (uint) {
        return 3;
    }
}

contract Derived3 is Derived2 {
    function doYetAnotherThing() public pure returns (uint) {
        return 4;
    }
}
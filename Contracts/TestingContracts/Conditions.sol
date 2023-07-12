// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SampleContract {
    uint public count = 0;

    function incrementCount() public {
        count += 1;
    }

    function decrementCount() public {
        if (count > 0) {
            if(count > 3){
                count++;
                if(count>4){
                    count++;
                }
            }
            else if(count < 5){
                count ++;
            }
            count -= 1;
        }
        else if(count<0){
            count--;
        }
         else {
            revert("Count is already zero");
        }
    }

    function resetCount() public {
        count = 0;
    }

    function complexFunction() public {
        // Function call
        resetCount();

        // Loop
        for (uint i = 0; i < 2; i++) {
            // Nested if-else
            if (i % 2 == 0) {
                incrementCount();
                if(i==5){
                    if(i>6){
                        i++;
                        }
                    i--;
                }
                else if (i != 5){
                    i++;
                }
            }
            else if(i>2){
                i--;
            }
            else {
                decrementCount();
            }
        }
    }
}

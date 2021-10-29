pragma solidity ^0.8.7;

contract uTodaycontract {
    
    string private name;
    uint private age;
    
        function setName(string memory newName) public {
            name=newName;
        }
        function getName() view public returns(string memory){
            return name;
        }
        function setAge(uint newAge) public {
            age=newAge;
        }
        function setName() view public returns(uint){
         return age;
        }
}
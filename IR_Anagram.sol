###
Two words are Anagram when re-arrange of letter produces another meaningful word, or two words have same number of letters and frequesncy.
###
pragma solidity ^0.8.0;

contract AnagramChecker {
    
    function checkIfAnagram(string memory str1, string memory str2) public pure returns (bool) {
        
        bytes32 hash1 = keccak256(bytes(str1));
        bytes32 hash2 = keccak256(bytes(str2));
        
        if (hash1.length != hash2.length) {
            return false;
        }
        
        for (uint i = 0; i < hash1.length; i++) {
            if (hash1[i] != hash2[i]) {
                return false;
            }
        }
        
        return true;
    }
}

###
The `checkIfAnagram` function takes two `string` arguments and returns a `bool` indicating whether they are anagrams of each other. It first calculates the keccak256 hash of each string, which is a 256-bit hash that uniquely identifies the string. It then compares the two hashes to check if they have the same length and contain the same characters. If they do, it returns `true`; otherwise, it returns `false`. Note that this implementation is case-sensitive, so "hello" and "Hello" would not be considered anagrams.
##

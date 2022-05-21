#include <cstdint>
#include <iostream>
#include <fstream>
#include <unordered_map>

uint64_t collatz_chain_length(uint64_t n0, std::unordered_map<uint64_t, uint64_t>* chain_length_dict){

    // If we know this chain, we return the known length
    auto search_key = chain_length_dict->find(n0);
    if(search_key != chain_length_dict->end()){
        return search_key->second;
    }

    uint64_t n;
    
    if (n0 % 2 == 0) n = 1 + collatz_chain_length(n0 / 2, chain_length_dict); 
    else n = 1 + collatz_chain_length( (3*n0)+1, chain_length_dict); 
    
    (*chain_length_dict)[n0] = n; 
    return n;
}

uint64_t run(){
    std::unordered_map<uint64_t, uint64_t> chain_length_dict = {{1,1}};

    uint64_t length_max = 0;
    uint64_t key_max = 0;

    for(uint64_t n = 500000; n < 1000000; n++){
        uint64_t length = collatz_chain_length(n, &chain_length_dict);
        if (length>length_max){
            length_max = length;
            key_max = n;
        }
    }

    return key_max;
}

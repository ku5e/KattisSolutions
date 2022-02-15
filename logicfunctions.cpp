#include <iostream>
#include "logicfunctions.h"

// Compute xor
void exclusive(bool x, bool y, bool& ans){
	ans = x ^ y;
	//also could be x != y (just saying)
}

// Compute implication
void implies(bool x, bool y, bool& ans){
	ans = !x || y; //Thanks to my student and friend Quan!
	//ans = x && y || !x && y || !x && !y; //Really damn ugly
	//could be if x then ans = y else  //not elegant but works
}

// Compute equivalence
void equivalence(bool x, bool y, bool& ans){
	ans = x == y;
}


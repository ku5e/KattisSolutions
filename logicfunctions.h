#include <iostream>

void exclusive(bool x, bool y, bool& ans);
void implies(bool x, bool y, bool& ans);
void equivalence(bool x, bool y, bool& ans);

using namespace std;

void checkAns(bool val, bool expected) {
    if (val != expected) {
        cout << "FAIL - expected " << expected << endl;
        exit(1);
    }
}

int main(){
    bool ans;
    
    cout << "xor's" << endl;
    exclusive(true, true, ans);
    cout << ans << endl;
    exclusive(true, false, ans);
    cout << ans << endl;
    exclusive(false, true, ans);
    cout << ans << endl;
    exclusive(false, false, ans);
    cout << ans << endl;
    
    cout << "implications" << endl;
    implies(true, true, ans);
    cout << ans << endl;
    implies(true, false, ans);
    cout << ans << endl;
    implies(false, true, ans);
    cout << ans << endl;
    implies(false, false, ans);
    cout << ans << endl;


    cout << "equivalents" << endl;
    equivalence(true, true, ans);
    cout << ans << endl;
    equivalence(true, false, ans);
    cout << ans << endl;
    equivalence(false, true, ans);
    cout << ans << endl;
    equivalence(false, false, ans);
    cout << ans << endl;
    
}
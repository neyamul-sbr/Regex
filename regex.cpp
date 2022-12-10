#include<iostream>
#include<regex>
#include<iterator>
#include <string>
using namespace std;

int main(){

    string s = "I Love You";

    regex r("(.*)ove(.*)");

    if(regex_match(s,r)){
            cout<<"True"<<endl;

    }
    else{
        cout<<"False"<<endl;
    }






}

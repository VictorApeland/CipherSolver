#include <iostream>
#include <string>
#include <algorithm>

std::string word;
std::string encrypted_word;

int equation(int a, int b, char x){
    return (a*(x-65)+b)%26+65;
}


std::pair<int, int> decrypt(){
    std::string result;
    for(int a = 1; a<26; a += 2){
        for(int b = 0; b<26; ++b){
            result = "";
            for(std::string::iterator it = word.begin(); it != word.end(); it++){
                result.push_back(equation(a,b,*it));
            }
            if(result == encrypted_word){
                return std::make_pair(a,b);
            }
        }
    }
    return std::make_pair(0,0);
}


int main(){
    std::cout << "Guessed word = " << std::flush;
    std::getline(std::cin, word);
    std::cout << "Encrypted word = " << std::flush;
    std::getline(std::cin, encrypted_word);

    transform(word.begin(), word.end(), word.begin(), toupper);
    transform(encrypted_word.begin(), encrypted_word.end(), encrypted_word.begin(), toupper);

    std::pair<int,int> result = decrypt();
    int a = result.first;
    int b = result.second;
    std::cout << "Value of a: " << a << "\n" << "Value of b: " << b << std::endl;
    
    system("pause");
}
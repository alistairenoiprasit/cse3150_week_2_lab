//
// Created by Alistaire Noiprasit on 8/9/2025.
//
#include "../include/parser.h"
#include <iostream>
#include <string>

std::string getInput(std::string request_text) {
    using namespace std;
    cout << request_text;
    string in_string;
    getline(std::cin, in_string);
    return in_string;
}

int main(void) {

    // Programming by contract
    using namespace std;
    string fullName = getInput("Enter your fullname... ");
    string email = getInput("Enter your email... ");

    string* firstName = new std::string();
    string* lastName = new std::string();

    using namespace StringUtils;

    parseName(fullName, firstName, lastName);
    cout << '\n' << "First Name: " << *firstName << endl;
    cout << "Last Name: " << *lastName << endl;
    cout << "Username: " << StringUtils::getUsername(email) << endl;

    free(firstName);
    free(lastName);
    return 0;
}
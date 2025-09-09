//
// Created by Alistaire Noiprasit on 8/9/2025.
//
#include "../include/parser.h"
#include <iostream>
#include <string>
#include <sstream>

using namespace StringUtils;

void StringUtils::parseName(const std::string& fullName, std::string* firstName,
    std::string* lastName) {
    std::stringstream(fullName) >> *firstName >> *lastName;
}

std::string StringUtils::getUsername(const std::string& email) {
    using namespace std;
    return email.substr(0, email.find("@"));
}

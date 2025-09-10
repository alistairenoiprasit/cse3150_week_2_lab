//
// Created by Alistaire Noiprasit on 8/9/2025.
//
#include "../include/parser.h"
#include <iostream>
#include <string>
#include <sstream>

using namespace StringUtils;
using std::string;

void StringUtils::parseName(const std::string& fullName, std::string* firstName,
    std::string* lastName) {

    size_t first_space_index = fullName.find(" ");
    size_t last_space_index = fullName.rfind(" ");

    *firstName = fullName.substr(0, first_space_index);
    if (last_space_index < fullName.length()) {
        *lastName = fullName.substr(last_space_index + 1, fullName.size());
    } else {
        *lastName = ""; // undefined
    }

}

std::string StringUtils::getUsername(const std::string& email) {
    using namespace std;
    return email.substr(0, email.find("@"));
}

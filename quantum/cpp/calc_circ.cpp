#include <iostream>
#include <string>
#include <map>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cmath>

std::map<std::string, int> d;

void init() {
	d.insert(std::map<std::string, int>::value_type("x0", 0));
	d.insert(std::map<std::string, int>::value_type("x1", 0));
	d.insert(std::map<std::string, int>::value_type("x2", 0));
	d.insert(std::map<std::string, int>::value_type("x3", 0));
	d.insert(std::map<std::string, int>::value_type("x4", 0));
	d.insert(std::map<std::string, int>::value_type("x5", 0));
	d.insert(std::map<std::string, int>::value_type("x6", 0));
	d.insert(std::map<std::string, int>::value_type("x7", 0));
	d.insert(std::map<std::string, int>::value_type("1", 0));
}

int main() {
    std::ifstream file("zou_circ.txt");
    if (!file.is_open()) {
        std::cerr << "无法打开文件 zou_circ.txt" << std::endl;
        exit(-1);
    }
    std::string line;
    while (std::getline(file, line)) {
		std::vector<std::string> var;
		std::stringstream ss(line);
		std::string word;
		while (ss >> word) {
			var.push_back(word);
		}
		if (var.size() == 2) {
			std::string x = var[0], y = var[1];
			if (d.count(x)) {
				d[x] = std::max(d[x], d[y] + 1);
			} else {
				d[x] = d[y] + 1;
			}
		} else {
			std::string x = var[0], y = var[1], z = var[2];
			if (d.count(x)) {
				d[x] = std::max(d[x], std::max(d[y] + 1, d[z] + 1));
			} else {
				d[x] = std::max(d[y] + 1, d[z] + 1);
			}
		}
    }
    file.close();
	int ans = 0;
	for (auto &pr : d) {
		ans = std::max(ans, pr.second);
	}
	std::cout << ans << std::endl;
	return 0;
}
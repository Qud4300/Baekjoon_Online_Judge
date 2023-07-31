#include <iostream>
#include <map>
#include <string>
using namespace std;

float gradeTofloat(const string &grade) {
  map<char, float> gradePoints{
      {'A', 4.0}, {'B', 3.0}, {'C', 2.0}, {'D', 1.0}, {'F', 0.0}};
  if (grade[1] == '+')
    return gradePoints[grade[0]] + 0.5;
  else
    return gradePoints[grade[0]];
}

int main() {
  string name, point, grade;
  float score = 0.0f, total = 0.0f;
  for (int i = 0; i < 20; i++) {
    cin >> name >> point >> grade;
    if (grade.compare("P") == 0)
      continue;
    total += stof(point);
    score += stof(point) * gradeTofloat(grade);
  }
  cout << score / total << endl;
  return 0;
}
void main() {
  List num = [1, 2, 90, 4, 5, 10, 8];
  int n = num[0];
  for (int i in num) {
    if (i>n) {
      n = i;
    }
  }
  print(n);
}

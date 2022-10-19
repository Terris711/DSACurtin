int main():
int x = 5;
int y = 10;
int* v = &x;
int** k = &v;
**k = *v*y;
printf("%d",**k)

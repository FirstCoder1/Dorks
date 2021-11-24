#include <stdio.h>

double mini(double a, double b){
    if(a<b){
        return a;
    }
    return b;
}

int main(){
    double num,nim,nom,min;
    printf("Enter the numbers:\n");
    scanf("%lf %lf %lf", &num, &nim, &nom);
    min= mini(nim, mini(num,nom));
    printf("The minimum between %lf and %lf and %lf is %lf\n", num, nim, nom, min);
    return 0;
}
double mini(double a, double b);
#method 1
# a=int(input("Enter first number = "))
# b=int(input("Enter first number = "))
# c=int(input("Enter first number = "))
#
# if a>b and b>c:
#     print("a is largest " , a)
# elif b > c and b > a:
#     print("b is largest ", b)
# else:
#     print("C is larget ",c)
#
#
#method 2
a=5
b=10
c=15
print(a>b, "b is larget")


#print prime numbe rtill 20 in java
# // Online Java Compiler
# // Use this editor to write, compile and run your Java code online
#
# class Main {
#     public static void main(String[] args) {
#         //prime number : divid by same number and 1
#         for (int i=1;i<=20;i++)
#         {
#             if(isPrime(i)){
#                 System.out.println("Its a prime number "+i);
#             }
#         }
#     }
#     public static boolean isPrime(int Number){
#         int count = 0;
#         for (int i=1;i<=Number;i++)
#         {
#             if (Number %i ==0){
#                 count++;
#             }
#         }
#         if (count==2){
#     //    System.out.println("Its a prime number");
#         return true   ;
#         }else {
#             return false;
#         }
#
#     }}

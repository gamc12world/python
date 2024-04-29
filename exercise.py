import random
def sum_of_array(arr:list):
    sum=0
    for i in arr:
        sum=sum+i
        print(i)
    print(f"sum of array is = {sum}")
    pass

sum_of_array([1,2,3,4,5,6,7])
def largest_element_arr(arr:list):
    max=0
    for i in arr:
        if i>max:
            max=i
    print(max)
    pass
largest_element_arr([1,6,3,4])


def _prime_number(n):
    if n==1:
        print("nothing")
    pass

_prime_number(1)

def arm_strong_no(n):
    x1=str(n)
    sum=0
    for i in x1:
        x3=int(i)
        print(x3**3)
        sum=sum+x3**3
        pass
    if sum==n:
        print("armstrong_no.")
    else:
        print("not armstrong.no")
    pass
arm_strong_no(350)
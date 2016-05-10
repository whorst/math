def factorial(num, perm = None):

#Ten students and five chairs on page 6. Solution on page 7. Using the discrete mathematics textbook from Dr. Liao's undergaduate.

    prod = ruleofproduct(num)

    if perm == None:

        return prod

    else:

        r = perm
        i = 1

        while(i<perm):
            if (r - i == 0):
                break
            perm=perm*(r-i)
            i+=1

        j= prod/perm


    print(j)

def ruleofproduct(num):
    i=1
    q = num
    w = num

    while (i < q):
            if (w - i == 0):
                break
            num = num*(w-i)
            i+=1

    return num


#print(factorial(10)/(factorial(4)*factorial(3)*factorial(1)*factorial(1)*factorial(1)))
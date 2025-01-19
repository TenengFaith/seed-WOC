def odd_sum():
    sum=0
    i=1
    while i<=15:
        if i%2!=0:
            sum+=i
        i+=1
    print(sum)
odd_sum()
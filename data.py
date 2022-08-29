def number_count(numberlist):
    odd_list=[]
    even_list=[]
    odd = 0
    even = 0
    for i in numberlist:
        if i%2==0:
            even+=1
            even_list.append(i)
        elif i%2!=0:
            odd+=1
            odd_list.append(i)


    return f"There Are {even} even numbers {even_list} & {odd} odd numbers {odd_list} in your list"


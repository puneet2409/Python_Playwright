
def test_even():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res =[]

    for i in l:
        if i % 2 == 0:
            res.append(i)
    print(res)

print(test_even())

def test_loop():
   list =[2,3,4,5,6,7,8]
   res = [val for val in list if val%2==0]
   print(res)
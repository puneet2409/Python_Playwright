
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


def reversal():
    list = [2, 3, 4, 5, 6, 7, 8]
    print(list[::-1])

def test_fil():
    l = [2, 3, 4, 5, 6, 7, 8]
    even_no = list(filter(lambda i:i%2==0,l))
    print(even_no)

def test_map():
    l = [2, 3, 4, 5, 6, 7, 8]
    res = list(map(lambda i:i*2,l))
    print(res)

def test_main():
    def test_repeat_element():
        arr = [10, 5, 3, 4, 3, 5, 6]
        seen =[]
        for val in arr:
             if val in seen:
                 return val
             seen.append(val)
        return -1

    print(test_repeat_element())

def test_count_zeros():
        arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
        count = 0
        i = -1
        while arr1[i] != 1:
            count = count + 1
            i = i - 1
        print(count)

def test_FlooringSortedArray ():
   arr = [1, 2, 8, 10, 10, 12, 19]
   x = 11
   position = -1

   for i in range(len(arr)):
       if arr[i] <= x:
            position = i

   print(position)


def test_array_is_sorted():
    arr = [101, 20, 30, 40, 50]

    if arr == sorted(arr):
        print("Sorted")
    else:
       print("Non-sorted")

def test_main2():
    def merge_sort(arr):
        if len(arr)>1:
            left_arr = arr[:len(arr)//2]
            right_arr =arr[len(arr)//2:]

            #recursive
            merge_sort(left_arr)
            merge_sort(right_arr)

            #merge
            i = 0 # left indx
            j = 0 #right inx
            k = 0 #sorted indx

            while i < len(left_arr) and j < len(right_arr):
               if left_arr[i] < right_arr[j]:
                   arr[k] = left_arr[i]
                   i += 1
               else:
                   arr[k] = right_arr[j]
                   j += 1
               k += 1

            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1

            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1


    arr = [0, 0, 1, 1, 0]
    merge_sort(arr)
    print(arr)


def test_main3():
    def wave(arr):
       for i in range(0,len(arr)-1,2):
           arr[i], arr[i+1] = arr[i+1], arr[i]

    arr = [1, 2, 3, 4, 5]
    wave(arr)
    print(arr)


#Merge Two Sorted Arrays Without Extra Space
def test_main3():
    def merg(a,b):

        for i in range(len(b)-1,-1,-1):

            if a[-1] > b[i]:

                last = a[-1]
                j = len(a)-2
                while j >= 0 and a[j] > b[i]:
                    a[j+1] = a[j]
                    j -=1

                a[j+1] = b[i]
                b[i] = last

    arr = [1, 2, 3, 4, 5, 10]
    brr = [6, 7, 8, 9]
    merg(arr,brr)

    print(arr," ",brr)

def test_main4():
    def test_intersection( a, b):
        n, m = len(a), len(b)
        i, j = 0, 0
        result = []

        while i < n and j < m:
            # If both elements are equal
            if a[i] == b[j]:
                # Avoid duplicates in the result
                if len(result) == 0 or result[-1] != a[i]:
                    result.append(a[i])
                # Move both pointers forward after adding the element
                i += 1
                j += 1

            # Move pointer `i` if a[i] is smaller
            elif a[i] < b[j]:
                i += 1

            # Move pointer `j` if b[j] is smaller
            else:
                j += 1

        print(result)
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3, 6, 7]
    test_intersection(a,b)


def test_reverseString():
    s = "Geeks"
    rev =""
    for i in s:
        rev = i + rev

    print(rev)


def test_is_binary():
    s = "101010"
    for char in s:
        if char not in ('0', '1'):
            return False
    print("rue")

def test_camel():
    s = "i got intern at geeksforgeeks"
    s= s.lower()
    for i in range(0,len(s)):
        if s[i] ==" ":
            s[i+1] = s[i+1].capitalize()

    s = s.replace(" ","")
    print(s)

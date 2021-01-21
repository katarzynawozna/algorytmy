def binary_search(list, item):
    #sorted list and item which position in this list I want to know

    low = 0
    high = len(list) - 1 #low and high lets us control which part of the list is being searched

    while low <= high: #as long as we looking thourgh more than one element
        mid = round((low + high) / 2 )#we pick the middle of the section we're looking thourgh
        guess = list[mid]
        if guess == item: #postion of item found!
            return mid
        if guess > item: #guessed number is too big
            high = mid - 1 #lowering section we're looking thourgh
        else: #guessed numer is too low
            low = mid + 1 
    return None #when there is no such item in the list

my_list = [3, 4, 78, 99, 100, 101]

print(binary_search(my_list, 4))
print(binary_search(my_list, 98))
#List Searching & Sorting

print("List Searching and Sorting")

word_list = ["apple", "banana", "orange", "dragonfruit", "grape"]
number_list = [46, 3, 75, 14, 25, 85, 38, 96]
number_list2 = [80, 37, 25, 1, 48, 56, 79, 25, 7, 18]
number_list3 = [45, 26, 19, 76, 52, 74, 33, 6, 98, 82]

print("\nLinear Search")
print("Linear Search searches the list by searching each element from the element from index")
print("zero sequentially until it reaches the end of the list. \n")

search_linear = "dragonfruit"
print(word_list)
print("The word we are trying to find is", search_linear)

exist = False
for counter in range(len(word_list)):
    
    if word_list[counter] == search_linear:
        exist = True
        break
    else:
        print("Word number", counter+1, "is", word_list[counter], ", it is not the word we are looking for.")
        
if exist == True:
    print("\'", search_linear, "\' is the number", counter+1, "element on the list.")   
else:
    print("\'", search_linear, "\' does not exist in this list. ")


print("\nBinary Search")
'''
Binary Search first sorts the list in acsending order, then checks if the middle value of
the list matches the number the search is looking for, if not, it will then see if the target
is bigger or smaller than the middle value, then it will continue its search using the same
method with the closer half. These steps will repeat until the target number is found. 
'''
search_binary = 75
print(number_list)
print("The number we are trying to find is", search_binary)

number_list.sort()
print(number_list)
start = 0
end = len(number_list)
for mid in range(start, end):
    mid = start + int((end-start)/2)
    if number_list[mid] == search_binary:
        break
    elif number_list[mid] > search_binary:
        end = mid
    else:
        start = mid
    print("Now, we only search", number_list[start:end])

print("\'", search_binary, "\' is the number", mid+1, "element on the list.")


print("\nSelection Sort")
'''
Selection sort sorts a list by selecting the left-most spot in a list, comparing each element
to find the element that fits in that spot, then moves on to the second spot. 
'''
print("Original list is", number_list2)

period = len(number_list2)-1
hold = 0
hold_list = ()
for x in range(period):
    for y in range(period - x):
        calc = number_list2[y] - number_list2[y+1]
        if calc > 0:
            hold = number_list2[y]
            number_list2[y] = number_list2[y+1]
            number_list2[y+1] = hold
    if hold_list == tuple(number_list2):
        break
    else:
        print("In step", x+1, ", the list is", number_list2)
        hold_list = tuple(number_list2)


print("\nInsertion Sort")
'''
Insertion sort sorts a list by inserting each element one by one, then immediately puts it in
the correct spot in the list by comparing each pre-existing number from biggest to smallest
'''
print("Original list is", number_list3)

sorted_list = [0]
for ele in number_list3:
    for step in range(len(sorted_list)):
        if ele > sorted_list[step]:
            step += 1
            if step >= len(sorted_list):
                sorted_list.append(ele)
                break
        else:
            sorted_list.insert(step, ele)
            break

sorted_list.pop(0)
print("sorted list = ", sorted_list)

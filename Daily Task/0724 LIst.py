
number_list = [123, 354353, 463, 754, 89059, 2414, 12, 433534, 65, 75, 214, 87, 9, 1,24, 213, 45563, 5, 2, 21, 3, 5, 5, 765]
cord_list = [(4,3),(12,5),(134,1),(2,41),(15,4)]


def find_largest_num_from_list(list): 
    largest = 0
    for i in range (len(list)):
        try:
            n = list[i]
            if n > largest:
                largest = n
        except TypeError:
            print('Please only provide numbers')
        except:
            print("Unknown Error")
    return largest
        
def sort_list(list):   #Challenge 3
    sorted_list = [find_largest_num_from_list(list)]
    print(sorted_list)
    for i in range(len(list)):
        n = list[i]                              # Doesn't Work Yet
        list.pop(i)
        for i in range(len(sorted_list)):
            if n < sorted_list[i]:
                sorted_list.insert(i,n)
            else:
                sorted_list.append(n)

    return sorted_list

def multiply_list(list): # Challenge 1
    n = 1
    for i in range(len(list)):
        n = n*list[i]
    return n




#largest = find_largest_num_from_list(number_list)
#print (largest)

print(sort_list(number_list))

#print(multiply_list(number_list))


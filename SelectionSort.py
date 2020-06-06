
#make an array for the sorting of the selection
array = [13, 4, 9, 5, 3, 16, 12]

#creation of function to sort the array
def selectionSort(array):

    #creation of variable for array length
    n = len(array)

   #whatever the length of the array is how many times you are going to run the for loop
    for i in range(n): 

        #Initially assume the first element of the unsorted part as the minimum
        minimum = i
        #loop through run through each number on the array
        for j in range(i+1, n):
            #comparing minimum to rest of array
            if (array[j] < array[minimum]): #comparison operator
                #updating position of minimum if smaller value is found
                minimum = j

        #swapping the index of i
        temp = array[i]
        #swapping number 
        array[i] = array[minimum]
        #setting new minimum
        array[minimum] = temp
    #returning array
    return array
#printing array onto screen
print(selectionSort(array))
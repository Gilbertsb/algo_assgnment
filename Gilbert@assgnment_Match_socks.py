#!/usr/bin/env python
# coding: utf-8

# In[47]:


def sort_pairs_socks(array, number_of_element):
    pairs = 0
    array.sort()    #sorting the Array
    i = 0

    while i < (number_of_element-1):
        if (array[i] == array[i + 1]):    #Checking pairs
            pairs += 1
            i = i + 2       #discluding the element for the current pairs
        else:
            i += 1
    return pairs
if __name__ == "__main__":
    
    arr1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
    arr2 = [11,12,13,14,15,16,17,18,19,20,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    number1 = len(arr1)
    number2 = len(arr2)
    
            
    print(sort_pairs_socks(arr1, number1)) #Calling the count pairs function
    print(sort_pairs_socks(arr2, number2)) 


# In[ ]:





# In[ ]:





def intersection(arrays):
    
    l = len(arrays)
    ht = {}
    result = []
    
    for i in range(l):
        
        array = arrays[i]
        
        for value in array:
            
            if value in ht:
                
                ht[value] += 1
            
            else:
                
                ht[value] = 1
                
            if i == l - 1 and ht[value] == l:

                result.append(value)
    
    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))

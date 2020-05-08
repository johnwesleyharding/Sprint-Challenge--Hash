def has_negatives(a):
    
    ht = {}
    result = []

    for value in a:
        
        i = abs(value)
        
        if i in ht:
            
            if ht[i] == value * -1:
                
                result.append(i)
                ht[i] = 0
        
        else:
            
            ht[i] = value

    return result

if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))

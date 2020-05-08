def get_indices_of_item_weights(weights, length, limit):
    
    if length < 2:
        
        return None

    ht = {}

    for i in range(length):

        a = weights[i]

        for j in range(i + 1, length):

            b = weights[j]
                
            ht[a + b] = (j, i)
            
    return ht[limit]

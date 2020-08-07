def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    lookup = {}

    ##### Brute Force
    # for i in range(len(weights)):
    #     for j in range(len(weights)):
    #         if i != j and weights[i] + weights[j] == limit:
    #             if weights[i] > weights[j]:
    #                 return (i, j)
    #             else:
    #                 return (j, i)

    ##### Following ReadMe:
    for i in range(len(weights)):
        limit_diff = limit - weights[i]
        if weights[i] not in lookup:
            lookup[weights[i]] = i
        
        if limit_diff in lookup and lookup[limit_diff] != i:
            second_weight = lookup[limit_diff]
            if second_weight > i:
                return (second_weight, i)
            else:
                return (i, second_weight)
        
        

    return None








weights = [ 4, 6, 10, 15, 16 ]
length = 5
limit = 21

print(get_indices_of_item_weights(weights, length, limit))
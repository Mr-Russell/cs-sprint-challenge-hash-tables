def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    positive = {}
    negative = {}
    result = []

    # for i in a:
    #     if i < 0 and i not in cache:
    #         cache[abs(i)] = 1
    #     elif i > 0 and i in cache:
    #         cache[i] += 1
    #         if cache[i] > 1:
    #             result.append(i)

    for i in a:
        if i < 0:
            if i not in negative:
                negative[i] = 0
            i = i * -1
            if i in positive:
                result.append(i)
        
        else:
            if i not in positive:
                positive[i] = 0
            i = i * -1
            if i in negative:
                result.append(abs(i))




    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
    # Should return [1, 2, 4]

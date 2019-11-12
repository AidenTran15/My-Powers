def largest_product(inputArray):
    max = -100
    
    for i in range(len(inputArray)-1):
        current_result = inputArray[i] * inputArray[i + 1]
        if current_result > max:
            max = current_result

    return max

print(largest_product([-23, 4, -3, 8, -12]))



        
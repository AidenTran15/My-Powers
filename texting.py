def almostIncreasingSequence(sequence):
    remove = 0
    i = 0
    j = 1

    while remove < 2 and j <= len(sequence) - 1:
        if sequence[j] <= sequence[i]:
            remove += 1
            j += 1
        else:
            i += 1
            j += 1

    if remove < 2: 
        return True
    else: 
        return False

        # for i in range(len(sequence)-1):
    #     if sequence[i+1] < sequence[i]:
    #         remove += 1
    #         if remove > 1:
    #             return False

    # return True
    

            


print(almostIncreasingSequence([1, 3, 2, 1]))
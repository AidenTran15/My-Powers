def checkParliment(inputString):
    list_input = list(inputString)
    list_input.reverse()
    join_input = ''.join(list_input)

    if inputString == join_input:
        return True
    else:
        return False

    return join_input

print(checkParliment("aabaa"))
def isanswer(answer, letters):
    a = sorted(list(set(list(answer))))
    b= sorted(letters)
    
    if a != b:
        return False
    else:
        return True
print(isanswer('apple', ['a', 'p', 'l','e']))
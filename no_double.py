def palin(word):
    re_word = list(reversed(list(word)))
    if list(word)==re_word:
        print(word)
        print('입력하신 단어는 회문(Palindrome)입니다.')
    else:
        print(word)
        print('입력하신 단어는 회문이(Palindrome)아닙니다.')

palin('eye')
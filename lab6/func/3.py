#def check_palindrome(word):
#    t = word
#    if t == word[::-1]:
#       print("Ok, this is  the palindrome")
#    else:
#        print("Nope")
#x = input()
#check_palindrome(x)
def check_palindrome(sequence):
    ok = True
    for n, m in zip(sequence, reversed(sequence)):
        if n != m:
           ok  =  False
        else:
            ok = True
    if ok:
        print('Ok')
    else:
        print('Nope')
x = input()
check_palindrome(x)
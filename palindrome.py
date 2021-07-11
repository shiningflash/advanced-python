def is_palindrome(str: str) -> bool:
    length = len(str)
    j = length - 1
    for i in range(int(length/2)):
        if str[i] != str[j]:
            return False
        j -= 1
    return True     
        

if __name__ == '__main__':
    str = "MADAm"
    print('Palindrome' if is_palindrome(str.lower()) else 'Not palindrome')
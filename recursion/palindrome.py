def palindrome(string: str) -> bool:
    if len(string) <= 1:
        return True
        
    return string[0] == string[1] and palindrome(string[1:-1])

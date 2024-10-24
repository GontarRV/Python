def palindrome(string: str, move:int = 0) -> bool:
    if len(string) // 2 <= move:
        return True
        
    return string[move] == string[-1 - move] and palindrome(string, move + 1)

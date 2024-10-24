def palindrome(string: str, move:int = 0) -> bool:
    if len(string) // 2 <= move:
        return True

    if string[move] != string[-1 - move]:
        return False
        
    return palindrome(string, move + 1)

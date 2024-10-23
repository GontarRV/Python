def palindrome(string: str, move: int = 0) -> bool:
    if len(string) <= 1:
        return True

    first_character_with_move = string[0]
    last_character_with_move = string[-1]
    if first_character_with_move != last_character_with_move:
        return False
    
    string = string[1:-1]
    return palindrome(string)
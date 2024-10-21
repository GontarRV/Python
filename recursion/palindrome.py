def palindrome(string: str, move: int = 0) -> bool:
    if move >= len(string) // 2:
        return True

    first_character_with_move = string[move]
    last_character_with_move = string[-1 - move]
    if first_character_with_move != last_character_with_move:
        return False

    return palindrome(string, move + 1)
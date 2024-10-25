def palindrome_recursive(string: str, move:int) -> bool:
    if len(string) // 2 <= move:
        return True

    if string[move] != string[-1 - move]:
        return False

    return palindrome_recursive(string, move + 1)


def palindrome(string: str):
    if len(string) == 0:
        return True

    return palindrome_recursive(string, 0)

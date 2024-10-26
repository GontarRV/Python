def generate_balanced_brackets(number_of_brackets: int) -> list:

    if number_of_brackets == 0:
        return [""]
    
    return generate_brackets("", number_of_brackets, 0, 0, [])

def generate_brackets(balanced_brackets, number_of_brackets, open_count, close_count, combinations_of_balanced_brackets):

    if len(balanced_brackets) == 2 * number_of_brackets:
        combinations_of_balanced_brackets.append(balanced_brackets)
    
    if open_count < number_of_brackets:
        generate_brackets(balanced_brackets + "(", number_of_brackets, open_count + 1, close_count, combinations_of_balanced_brackets)

    if close_count < open_count:
        generate_brackets(balanced_brackets + ")", number_of_brackets, open_count, close_count + 1, combinations_of_balanced_brackets)
    
    return combinations_of_balanced_brackets
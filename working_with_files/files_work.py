import random


# задание 3.1
for i in range(1, 11):
    file_name = str(i) + '.txt'
    with open (file_name, 'w') as f:
        for j in range(2):
            f.write(str(random.randint(1, 100)) + '\n')
        f.write(str(random.randint(1, 100)))

# задание 3.2
def get_sum_numbers(file_number_one, file_number_two):

    file1 = str(file_number_one) + '.txt'
    with open (file1, 'r') as f:
        sum1 = 0
        try:
            number_lines = 0
            number = int(f.readline().rstrip())
            while number != '':
                sum1 += int(number)
                number_lines += 1
                number = f.readline().rstrip()
        except:
            raise Exception('Invalid file')
        
        if number_lines != 3:
            raise Exception('Wrong line count')  


    file2 = str(file_number_two) + '.txt'
    with open (file2, 'r') as f:
        sum2 = 0
        try:
            number_lines = 0
            number = int(f.readline().rstrip())
            while number != '':
                sum2 += int(number)
                number_lines += 1
                number = f.readline().rstrip()

        except:
            raise Exception('Invalid file')
        
        if number_lines != 3:
            raise Exception('Wrong line count')
 
    return sum1 + sum2
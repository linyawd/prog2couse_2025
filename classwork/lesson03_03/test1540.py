def can_form_23(numbers):
    from itertools import permutations

    for nums in permutations(numbers):
        for op1 in ['+', '-', '*']:
            for op2 in ['+', '-', '*']:
                for op3 in ['+', '-', '*']:
                    for op4 in ['+', '-', '*']:
                        # Обчислюємо значення виразу зліва направо
                        result = nums[0]
                        result = apply_op(result, nums[1], op1)
                        result = apply_op(result, nums[2], op2)
                        result = apply_op(result, nums[3], op3)
                        result = apply_op(result, nums[4], op4)
                        if result == 23:
                            return True
    return False

def apply_op(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

while True:
    line = input().strip()
    numbers = list(map(int, line.split()))
    if numbers == [0, 0, 0, 0, 0]:
        break
    if can_form_23(numbers):
        print("Possible")
    else:
        print("Impossible")
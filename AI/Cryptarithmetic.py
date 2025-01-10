def find_value(words, assigned):
    total = 0
    for word in words:
        num = 0
        for char in word:
            num = num * 10
            num += assigned[char]
        total += num
    return total


def is_valid_assignment(words, result, assigned):
    # First letter of any word cannot be zero.
    for word in words + [result]:
        if assigned[word[0]] == 0:
            return False
    return True


def _solve(words, result, letters, assigned, solutions):
    if not letters:
        if is_valid_assignment(words, result, assigned):
            total = find_value(words, assigned)
            num_result = find_value([result], assigned)
            if total == num_result:
                solutions.append(
                    (f"{' + '.join(str(find_value([w], assigned)) for w in words)} = {num_result}", assigned.copy()))
        return

    for num in range(10):
        if num not in assigned.values():
            cur_letter = letters.pop()
            assigned[cur_letter] = num
            _solve(words, result, letters, assigned, solutions)
            assigned.pop(cur_letter)
            letters.append(cur_letter)


def solve_puzzle(words, result):
    letters = sorted(set(''.join(words) + result))
    if len(letters) > 10:
        print('0 Solutions! (Too many unique letters)')
        return

    solutions = []
    _solve(words, result, letters, {}, solutions)
    if solutions:
        print(f'\nSolutions for {" + ".join(words)} = {result}:')
        for soln in solutions:
            print(f'{soln[0]}\t{soln[1]}')
    else:
        print(f"No solution for {' + '.join(words)} = {result}")


if __name__ == '__main__':
    print('CRYPTARITHMETIC PUZZLE SOLVER')
    words=list(input("ENTER THE WORDS : ").split(" "))
    result=input("ENTER THE RESULT : ")
    solve_puzzle(words, result)

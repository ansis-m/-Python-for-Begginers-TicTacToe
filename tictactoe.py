def win(chars):
    count = ""

    for i in range(3):
        if chars[i * 3] == chars[i * 3 + 1] and chars[i * 3] == chars[i * 3 + 2]:
            count += chars[i * 3]
        if chars[i] == chars[i + 3] and chars[i] == chars[i + 6]:
            count += chars[i]
    if chars[0] == chars[4] and chars[0] == chars[8]:
        count += chars[0]
    if chars[2] == chars[4] and chars[2] == chars[6]:
        count += chars[2]

    return count


def count_chars(chars):
    X = 0
    O = 0

    for ch in chars:
        if ch == 'X':
            X += 1
        elif ch == 'O':
            O += 1

    return X, O


def impossible(chars):

    X, O = count_chars(chars)
    if (X - O) ** 2 >  1 or len(win(chars)) > 1:
        return True

    return False


def draw(chars):
    X, O = count_chars(chars)
    return True if X + O == 9 else False


def main():

    chars = input()
    print("---------")
    print("| {} {} {} |".format(chars[0], chars[1], chars[2]))
    print("| {} {} {} |".format(chars[3], chars[4], chars[5]))
    print("| {} {} {} |".format(chars[6], chars[7], chars[8]))
    print("---------")

    if impossible(chars):
        print("Impossible")
    elif win(chars) == 'X' or win(chars) == 'O':
        print("{} wins".format(win(chars)))
    elif draw(chars):
        print("Draw")
    else:
        print("Game not finished")

if __name__ == "__main__":
    main()
# Password Generator Project
def password_generator():
    import random
    randoms = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        '!', '#', '$', '%', '&', '(', ')', '*', '+'
    ]
    password = ""

    # random password
    for number in range(0, random.randint(11, 15)):
        password += random.choice(randoms)

    # Function Convert String
    def CovertString(string):
        list = []
        list[:0] = string
        return list

    # process random password
    passwords = CovertString(password)
    random_count = len(passwords)
    adv_password = ""
    while True:
        rd_number = random.randint(0, random_count - 1)
        adv_password += passwords[rd_number]
        passwords.remove(passwords[rd_number])
        random_count = len(passwords)
        if random_count == 0:
            break

    # print(f"Advanced Password: {adv_password}")
    return adv_password

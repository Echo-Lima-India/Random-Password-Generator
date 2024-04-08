import random as ran

def passwordGenerator():
    password = []
    for i in range(0,15):  #edit range from 0 to x get desired key length
        charDetermine = ran.randint(1,4)
        if charDetermine == 1:
            password.append(chr(ran.randint(97,122)))
        elif charDetermine == 2:
            password.append(chr(ran.randint(65, 90)))
        elif charDetermine == 3:
            randomNum = ran.randint(0, 9)
            password.append(str(randomNum))
        elif charDetermine == 4:
            specialCharDetermine = ran.randint(1, 4)
            if specialCharDetermine == 1:
                password.append(chr(ran.randint(33, 46)))
            elif specialCharDetermine == 2:
                password.append(chr(ran.randint(58, 63)))
            elif specialCharDetermine == 3:
                password.append(chr(ran.randint(91, 96)))
            elif specialCharDetermine == 4:
                password.append(chr(ran.randint(123, 126)))
    return "".join(password)

print(passwordGenerator())
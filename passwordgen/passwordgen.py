import string
import random
import sys

chars = list(string.ascii_letters + string.digits + string.punctuation)
n = int(input("\n Enter password length: "))


def input_error():
    print(
        "passwordgen-py \n",
        "USAGE: \n",
        "   passwordgen [PASS LENGTH INT < 2048]"
    )


if n == "":
    input_error()
    sys.exit()
elif n > 2048:
    input_error()
    sys.exit()

passwd = []
for idk in range(n):
    passwd.append(random.choice(chars))

random.shuffle(passwd)
print("".join(passwd))

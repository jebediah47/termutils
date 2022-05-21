import sys

balls = str(input("Enter Your e-mail: ")).strip()


def input_error():
    if balls == "":
        print(
            "USAGE: \n",
            "   slicemail [EMAIL < 512]"
        )
        sys.exit()
    elif len(balls) > 512:
        print(
            "USAGE: \n",
            "   slicemail [EMAIL < 512]"
        )
        sys.exit()


class email_slicer:
    uname = balls[:balls.index('@')]
    domain = balls[balls.index('@') + 1:]
    print(f"Your username is {uname} & domain is {domain}")


if __name__ == "__main__":
    email_slicer()
    input_error()

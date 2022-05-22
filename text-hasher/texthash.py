import hashlib
import sys

balls = input("Enter the text to be hashed: ")
md5_object = hashlib.md5(str(balls).encode("utf-8"))
sha256_object = hashlib.sha256(str(balls).encode("utf-8"))


def input_error():
    if balls == "":
        print(
            "USAGE: \n",
            "   passhash [PASS < 2048]"
        )
        sys.exit()
    elif len(balls) > 2048:
        print(
            "USAGE: \n",
            "   texthash [PASS < 2048]"
        )
        sys.exit()


def output_hashes():
    print("MD5: " + md5_object.hexdigest())
    print("SHA256: " + sha256_object.hexdigest())


if __name__ == "__main__":
    input_error()
    output_hashes()

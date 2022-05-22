import hashlib
import qrcode
import sys

data = input("Enter data to be made to a QR-code: ")


def input_error():
    if data == "":
        print(
            "USAGE: \n",
            "   qrcodegen [DATA < 2048]"
        )
        sys.exit()
    elif len(data) > 2048:
        print(
            "USAGE: \n",
            "   qrcodegen [DATA < 2048]"
        )
        sys.exit()


def make_qrcode():
    md5 = hashlib.md5(str(data).encode("utf-8"))
    qr = qrcode.make(data)
    qr.save(f"{md5.hexdigest()}.jpg")


if __name__ == "__main__":
    input_error()
    make_qrcode()

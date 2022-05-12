from stegano import lsb

def createSave(path: str, msg: str, alt: str):
    print(path)
    print(msg)
    print(alt)

    secret = lsb.hide(path, msg)

    secret.save(alt)
    print("save successful")


def reveal(path: str):
    print(path)
    message = lsb.reveal(path)
    print(message)

    return message

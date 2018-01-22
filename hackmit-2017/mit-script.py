import sys

def decode(message):
    message = message.lower()
    result = ""
    for i in range(len(message)):
        temp = message[i]
        if temp.isalpha():
            num = ord(temp) - 14
            if num < 97:
                num = num + 26
            temp = chr(num)
        result = result + temp
    return result

if __name__ == "__main__":
    message = ""
    for word in sys.argv[1:]:
        message = message + word + " "
    print(decode(message))

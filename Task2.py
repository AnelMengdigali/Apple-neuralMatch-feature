# Task2: version of the Apple neuralMatch feature
import os
from pathlib import Path


def menu2():

    print("         Welcome to the neuralMatch          ")
    print(" Choose the desired operation                ")
    print(" 1) to check a file                          ")
    print(" 2) to check all files a directory           ")

    option = input("Please enter operation (1 or 2): ")
    phrase = input("Please enter your a name: ")

    # creating a database of controlled files named as repository.txt:
    sha1 = hashlib.sha1()
    path = Path.cwd()

    files = os.listdir(path)
    for file in files:
        with open(file, "rb") as opened_file:
            content = opened_file.read()
            sha1.update(content.encode())

        with open("repository.txt", "w") as repository:
            repository.write(sha1.hexdigest())

    return int(option), phrase


def oneFile(name):

    sha1 = hashlib.sha1()
    check = false

    # obtaining hash value of a file:
    with open(file, "rb") as opened_file:
        content = opened_file.read()
        sha1.update(content.encode())
        hash = sha1.hexdigest()

    # check if database contains that file:
    with open("repository.txt") as repository:
        if hash in repository.read():
            check = true

    return check


def allFiles(name):

    sha1 = hashlib.sha1()
    check = false
    fileName = ""

    # obtaining hash value of each file in a directory:
    files = os.listdir(name)
    for file in files:

        with open(file, "rb") as opened_file:
            content = opened_file.read()
            sha1.update(content.encode())
            hash = sha1.hexdigest()

        # check if database contains that file:
        with open("repository.txt") as repository:
            if hash in repository.read():
                check = true
                fileName = file

        return check, file


operation, name = menu2()

if operation == 1:

    check = oneFile(name)
    if check == true:
        print(
            "The contents of that file have been seen before (a new file is a member of that set of controlled files)"
        )
    else:
        print("The contents of that file have not been seen before")

elif operation == 2:

    check, fileName = allFiles(name)
    if check == true:
        print("The contents of this file have been seen before: ", fileName)
    else:
        print("The contents of that file have not been seen before: ", fileName)

else:
    print("Error")

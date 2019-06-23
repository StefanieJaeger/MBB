


def getCredentials(string):
    cred = {}

    for line in open("credentials"):
        cred[line.split("=")[0]] = line.split("=")[1].strip("\n")

    return cred[string]

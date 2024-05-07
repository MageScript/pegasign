
def readSignatures(signFilename):
    signatures = []

    with open(signFilename, 'r') as file:
        for line in file:
            values = line.strip().split(' ')
            dataTuple = tuple(map(int, values))
            signatures.append(dataTuple)

    return signatures


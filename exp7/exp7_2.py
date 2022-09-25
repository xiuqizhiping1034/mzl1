def main():
    infile1 = open(r"input.txt", "r")
    infile2 = open(r"output.txt", "w")

    allLines = infile1.readlines()

    # lines = allLines.split('\n')

    for line in allLines:
        l1 = line.replace('the', '')
        infile2.write(l1)

    #print(infile2)
    infile1.close()
    infile2.close()


main()

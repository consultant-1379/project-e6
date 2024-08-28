# TODO needs a way to make sure file is not empty
def makeReadable(file, outputFileName="output.csv"):
    # step 1 clean up the configs
    dealWithConfigs(file)
    # step 2 deal with extra @'s
    dealWithDelimeters(outputFileName)


def dealWithConfigs(file):
    # open the temp file to which the update lines will be written to
    original = open(file, 'r')
    temp = open("temp.csv", 'w')
    line = original.readline()
    while line != "":
        if "@" in line:
            temp.write("\n" + line.replace('\n', ''))
        else:
            temp.write(line.replace('\n', ''))
        line = original.readline()
    original.close()  # close the unstructure file
    temp.close()  # close the temp file containing new structure


# deal with the delimeters
def dealWithDelimeters(output):
    # open the temp file to which the update lines will be written to
    temp = open("temp.csv", 'r')
    output = open(output, 'w')

    line = temp.readline()
    while line != "":

        if line.count('@') == 3:

            # print(line, end="")
            output.write(line.replace('\n', '') + "@NaN" + "\n")
        else:
            output.write(line.replace('\n', '') + "\n")
        line = temp.readline()

    temp.close()  # close the temp file
    os.remove("temp.txt")
    output.close()  # close the now structured file


# Read using pandas
def readReadable(file):
    # creating a data frame
    os.remove("temp.txt")
    print(df)


def convertCompleteCsvFile(unstructuredFile, structuredFile):

    makeReadable(unstructuredFile)

    readReadable(structuredFile)


#You must make and submit your own test file and txt file with this assignment.

def toString(newFile):
    #This function returns the text from a given file.
    #Any new lines are written as \n
    f = open(newFile)
    out = ""
    for line in f:
        out += line
    return out
#print(toString("ExampleText.txt")=="Here is the text\ni am another line")

def longestLine(newFile):
    #Given a file return the longest line from within that file
    f = open(newFile)
    longest = 0
    answer = ""
    for line in f:
        x = len(line)
        if longest < x:
            longest = x
            answer = line
    return answer

def toBinary(binaryText):
    #Given a file that is only 0's and 1's return a list of the file broken into bytes.
    #An example return might be ['01101001', '00101010', '1010']
    f = open(binaryText)
    binarylist = []
    line = f.read(8)
    binarylist.append(line)
    while len(line)>0:
        line = f.read(8)
        binarylist.append(line)
    return binarylist




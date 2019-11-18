# Sydney Purdom
# CSCI 102 - Section A
# Week 12 - Part A

def PrintOutput(string):
    print("OUTPUT", string)

def LoadFile(file):
    lines = []
    with open(file) as f:
        for line in f:
            for lin in line.split():
                lines.append(lin)
    return lines

def UpdateString(string, char, num):
    str2list = list(string)
    str2list[num] = char
    update = ""
    updatestr = update.join(str2list)
    print("OUTPUT", updatestr)
    
def FindWordCount(list1, string):
    occur = 0
    for i in range(len(list1)):
        if list1[i] == string:
            occur += 1
    return occur

def ScoreFinder(list1, list2, string):
    stringLower = string.lower()
    newList = []
    for i in range(len(list1)):
        list1Lower = list1[i].lower()
        newList.append(list1Lower)
        if newList[i] == stringLower:
            score = list2[i]
            print("OUTPUT", list1[i], "got a score of", score)
    if stringLower not in newList:
        print("OUTPUT player not found")

def Union(list1, list2):
    combine = list1 + list2
    good = list(dict.fromkeys(combine))
    return good

def Intersection(list1, list2):
    inter = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                inter.append(list1[i])
    return inter

def NotIn(list1, list2):
    notIn = []
    for i in range(len(list1)):
        if list1[i] not in list2:
            notIn.append(list1[i])
    return notIn

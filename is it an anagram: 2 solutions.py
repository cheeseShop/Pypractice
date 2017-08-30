# converting strings to lists and then sorting
def anagramSolution1(s1,s2):
    aList1 = list(s1)
    aList2 = list(s2)

    aList1.sort()
    aList2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if aList1[pos] == aList2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

print(anagramSolution1("abcde", "edcba"))

#an anagram will have the same number of a's,b's etc.
#count the number of times each character occurs in each word
#if the two counters are identical then it must be an anagram
def anagramSolution2(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord("a")
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord("a")
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK

print(anagramSolution2("apple", "leapp"))

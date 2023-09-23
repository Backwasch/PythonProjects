def RansomNote(ransomNote,magazine):
    dic = {}
    if len(ransomNote) > len(magazine):
        return False
    for x in range(len(magazine)):
        currentElement = dic.get(magazine[x - 1])
        if currentElement == None:
            dic[magazine[x - 1]] = 1
        else:
            dic[magazine[x - 1]] = currentElement + 1

    for x in range(len(ransomNote)):
        currentLetter = dic.get(ransomNote[x - 1])
        if currentLetter == None or currentLetter < 1:
            return False
        dic[ransomNote[x - 1]] = currentLetter - 1
    return True

print(RansomNote("aabc","abcd"))

def RansomNote(ransomNote,magazine):
    if len(ransomNote) > len(magazine):
        return False
    dic = {}
    for x in range(len(magazine)):
        dic[magazine[x - 1]] = dic.get(magazine[x - 1],0) +1

    for x in range(len(ransomNote)):
        if dic.get(ransomNote[x - 1],0) == 0:
            return False
        dic[ransomNote[x - 1]] -= 1
    return True
print(RansomNote("aabc","abcd"))

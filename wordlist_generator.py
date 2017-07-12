import os

with open("wordlist1.txt", "r") as wordlist:

    new_list = []

    for x in wordlist:
        new_list.append(x.strip())

    iterate = len(new_list)

    for word1 in new_list:
        for word2 in new_list:
            for word3 in new_list:
                print "%s%s%s" % (word1, word2, word3)

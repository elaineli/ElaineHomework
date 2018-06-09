# Write a Python function that takes a list of words and
# returns the length of the longest one

# myTest = ['this', 'is', 'a', 'list', 'of', 'words']

def maxLen(list):
    maxLen = 0
    for e in list:
        if len(e) > maxLen:
            maxLen = len(e)
    return maxLen


print(maxLen(['this', 'is', 'a', 'list', 'of', 'words']))

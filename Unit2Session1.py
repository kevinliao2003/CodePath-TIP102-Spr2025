from collections import defaultdict

# Advanced Problem Set Version 1 - Problem 2: Pirate Message Check
def can_trust_message(message):
    """
    U - Understand
    - message contains only lowercase English letters + whitespace
    - messasge is not empty

    P - Plan
    variables:
    - dictionary

    loop through the message
        increment the frequency of the letter

    return true if the size of dic is 26 and no 0 exists in the values

    I - Implement
    - see code below
    """

    dic = defaultdict(int)
    for letter in message:
        if letter.isalpha():
            dic[letter] += 1

    return len(dic) == 26 and 0 not in dic.values()

message1 = "sphinx of black quartz judge my vow"
res = can_trust_message(message1)
assert res == True
message2 = "trust me"
res = can_trust_message(message2)
assert res == False

# Advanced Problem Set Version 1 - Problem 3: Find All Duplicate Treasure Chests in an Array
def find_duplicate_chests(chests):
    """
    U - Understand
    - all values in the chest are in the range [1, n]
    - each integer appears once or twice

    P - Plan
    variables:
    - dic to map each char to its frequency
    - res (array to return)

    loop through the chests
        increment the frequency in dic
        if the freq of the current char is 1
            add it to res

    return res

    I - Implement
    - see code below
    """

    dic = defaultdict(int)
    res = []
    for num in chests:
        dic[num] += 1
        if dic[num] == 2:
            res.append(num)

    # print(chests, res)
    return res

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
res = find_duplicate_chests(chests1)
assert res == [2, 3]
chests2 = [1, 1, 2]
res = find_duplicate_chests(chests2)
assert res == [1]
chests3 = [1]
res = find_duplicate_chests(chests3)
assert res == []
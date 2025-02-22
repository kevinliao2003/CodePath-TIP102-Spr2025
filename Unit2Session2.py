from collections import defaultdict

# Advanced Problem Set Version 1 - Problem 6: Counting Divisible Collections in the Gallery
def count_divisible_collections(collection_sizes, k):
    """
    U - Understand
    - array contains only integers
    - array can't be empty

    P - Plan
    brute force:
        check every subarray (O(n^2) time complexity)

    I - Implement
    - see code below
    """

    n = len(collection_sizes)
    res = 0 # count to return
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += collection_sizes[j]
            if curr_sum % k == 0:
                res += 1
    
    return res

nums1 = [4, 5, 0, -2, -3, 1]
k1 = 5
res = count_divisible_collections(nums1, k1)
assert res == 7
nums2 = [5]
k2 = 9
res = count_divisible_collections(nums2, k2)
assert res == 0

# Advanced Problem Set Version 1 - Problem 5: Assigning Unique Nicknames to Contestants
def assign_unique_nicknames(nicknames):
    """
    U - Understand
    - all names are unique
    - add a suffix where k is the smallest integer to make the name unique

    P - Plan
    variables:
    - dictionary to keep track of the frequency

    loop through names
        if name is unique
            do nothing
        else
            add the frequency to the end of the current name
    return names

    I - Implement
    - see code below
    """

    dic = defaultdict(int)
    for i, name in enumerate(nicknames):
        if dic[name] > 0:
            nicknames[i] = f"{name}({dic[name]})"
        dic[name] += 1
    
    return nicknames

nicknames1 = ["Champ","Diva","Champ","Ace"]
res = assign_unique_nicknames(nicknames1)
# print(res)
assert res == ["Champ","Diva","Champ(1)","Ace"]
nicknames2 = ["Ace","Ace","Ace","Maverick"]
res = assign_unique_nicknames(nicknames2)
assert res == ["Ace","Ace(1)","Ace(2)","Maverick"]
nicknames3 = ["Star","Star","Star","Star","Star"]
res = assign_unique_nicknames(nicknames3)
assert res == ["Star","Star(1)","Star(2)","Star(3)","Star(4)"]
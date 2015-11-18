__author__ = 'Henry Pan'


def is_anagram_1(str1, str2):
    list1 = list(str1)
    list2 = list(str2)
    if len(list1) != len(list2):
        return False
    if sorted(list1) == sorted(list2):
        return True
    return False


def is_anagram_2(str1, str2):
    c1 = [0] * 128
    c2 = [0] * 128

    if len(str1) != len(str2):
        return False
    for a in str1:
        c1[ord(a)] += 1
    for b in str2:
        c2[ord(b)] += 1

    if c1 == c2:
        return True
    else:
        return False


if __name__ == '__main__':
    one = 'heart'
    two = 'earth'
    # sorting usually takes O(n2) or O(nlogn)
    print is_anagram_1(one, two)
    # count based on ascii value. O(n)
    print is_anagram_2(one, two)

    one = 'REdbox'
    two = 'ErdxoB'
    print is_anagram_1(one, two)
    print is_anagram_2(one, two)
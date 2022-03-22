# Shahriyar Mammadli
# LeetCode problem '205. Isomorphic Strings' solution

def isIsomorphic(s, t):
    s_index = [[] for i in range(128)]
    t_index = [[] for i in range(128)]
    for index in range(len(s)):
        s_index[ord(s[index])].append(index)
        t_index[ord(t[index])].append(index)
    for ind_list in s_index:
        if ind_list and ind_list not in t_index:
            return False
    return True

print(isIsomorphic("abca", "baab"))
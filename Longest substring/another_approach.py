def longest_substring(s):
    sub = {}
    cur_sub_start = 0
    cur_len = 0
    longest = 0

    for index, letter in enumerate(s):

        if letter in sub and sub[letter] >= cur_sub_start:
            cur_sub_start = sub[letter] + 1
            cur_len = index - sub[letter]
            sub[letter] = index

        else:
            sub[letter] = index
            cur_len += 1
            if cur_len > longest:
                longest = cur_len
    return longest


value = longest_substring("abccdfh")
print(value)

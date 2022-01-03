def is_in(str1, str2):
    if str1 in str2:
        print(f'{str1} is in {str2}')
    elif str2 in str1:
        print(f'{str2} is in {str1}')
    else:
        print('Neither string found in the other')


def test_is_in(strs1, strs2):
    for s1 in strs1:
        for s2 in strs2:
            is_in(s1, s2)


strs1 = ('alpha', 'beta', 'gamma', 'delta')
strs2 = ('delta', 'gamma', 'beta', 'alpha')

test_is_in(strs1, strs2)

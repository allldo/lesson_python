import itertools
print('input')
combo = int(input())

all_num = {
    1: '',
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'psqrs',
    8: 'tuv',
    9: 'wxyz',
}
asd = []
for x in str(combo):
    asd.append(all_num.get(int(x)))
qwe = ''
qwe = qwe.join(asd)
comba = list(itertools.combinations(qwe, 3))
print(len(comba))
# IRizerX
# Instagram : @_irizerx_

separator = input('Enter Separator Example (: - /) : ')
list1 = open('IRizerX1.txt', 'r').read().splitlines()
list2 = open('IRizerX2.txt', 'r').read().splitlines()
with open('Combo-List.txt', 'a') as f:
    for item1 in list1:
        for item2 in list2:
            f.write(f'{item1}{separator}{item2}\n')
    input('All Done!')

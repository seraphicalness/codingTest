vote_list = [input() for _ in range(9)]

tiger = vote_list.count('Tiger')
lion = vote_list.count('Lion')

if lion < tiger:
    print('Tiger')
else:
    print('Lion')
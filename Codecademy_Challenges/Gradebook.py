#Lists practice
subjects = ['MDE', 'MTH', 'ACC', 'ENG']
grades = [98, 97, 85, 88]
gradebook = [['MDE', 98], ['MTH', 97], ['ACC', 85], ['ENG', 88]]

print(gradebook)

gradebook.append(['CS', 100])
gradebook.append(['VA', 93])

print(gradebook)

gradebook[-1][-1] = 98

print(gradebook)


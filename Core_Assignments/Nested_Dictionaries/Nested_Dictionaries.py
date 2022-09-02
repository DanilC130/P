# x = [[5, 2, 3], [10, 8, 9]]
# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'}
# ]
# sports_directory = {
#     'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer': ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [{'x': 10, 'y': 20}]

# x[1][0] = 15

# students[0]['last_name'] = 'Bryant'

# sports_directory['soccer'][0] = 'Andres'

# z[0]['y'] = 30

# print(z)


# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]


# def iterateDictionary(students):
#     for dict in students:
#         for key in dict:
#             print(key,dict[key])

# iterateDictionary(students)


# def iterateList(someKey, students):
#     for bob in students:
#         print(bob[someKey])


# iterateList("first_name", students)
# iterateList("last_name", students)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


# def printInfo(dojo):
#     print(len(dojo['locations']))
#     for location in dojo['locations']:
#         print(location)
#     print()
#     print(len(dojo['instructors']), "INSTRUCTORS")
#     for instructor in dojo['instructors']:
#         print(instructor)


def printInfo(dojo):


    printInfo(len(dojo['locations']))
    for val in dojo['locations']:
        print(val)

printInfo(dojo) 

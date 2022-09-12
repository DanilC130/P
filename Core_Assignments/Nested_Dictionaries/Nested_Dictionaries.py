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



# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:


def function4(some_dict):

    for key in some_dict:
        print(key, len(some_dict[key]))

        for item in some_dict[key]:
            print(item)

# print(some_dict['locations'])

function4(dojo)


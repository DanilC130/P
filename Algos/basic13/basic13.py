# for i in range(1,256):
#     print(i)


# Print integers from 0 to 255, and with each integer print the sum so far.

# sum = 0
# for i in range(0,256):
#     sum - sum + i
#     sum += i
#     print(f"num: {i}, sum: {sum}")

# Given an array, find and print its largest element.

# def largestElement(list):
#     max = 0
#     for i in list:
#         if i > max:
#             max = i
#     print(max)

# myList = [4,9,-1,0,0,14,9,8,19,100,-43,98]
# largestElement(myList)
# myOtherList = [4,9,-1,0,2,-14,149,-2,0]
# largestElement(myOtherList)

# Create an array with all the odd integers between 1 and 255 (inclusive).

# odds = []
# for i in range(1,256):
#     if i % 2 == 1:
#         odds.append(i)
# print(odds)


# Given an array and a value Y, count and print the number of array values greater than Y.

# def greaterCount(list, y):
#     count = 0
#     for val in list:
#         if val > y:
#             print(val)
#             count += 1
#     print(count)
# myList = [4,9,-1,0,2,-14,149,-2,0]
# greaterCount(myList,10)

# def maxMinAverage(list):
#     max = list[0]
#     min = list[0]
#     sum = 0
#     avg = 0
#     for i in list:
#         sum += i
#         if i < min:
#             min = i
#         if i > max:
#             max = i
#     avg = sum/len(list)
#     print(f"max: {max}, min: {min}, avg: {avg}")


# myList = [4, 9, -1, 0, 0, 14, 9, 8, 19, 100, -43, 98]
# maxMinAverage(myList)
# myOtherList = [4, 9, -1, 0, 2, -14, 149, -2, 0]
# maxMinAverage(myOtherList)

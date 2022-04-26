# #Given a string after every y add an ! and after every s add a peroid and make every w and g capital
# #Make a Function that takes a string as input and returns the adjusted string.
# s="Hey welcome to doing whiteboard problems get prepared to figure our a problem on the fly"
# #output= Hey! Welcome to doinG Whiteboard problems. Get prepared to fiGure our a problem on the fly!

# def puntuation(s):
#     for letters in s:
#         if letters == "y":
#             print('!')


# print(s)


color = input("What's your favorite color?:")
result_string = "Oh {}, that's mine too ".format(color)
print(result_string)

if 'v' not in color:
    print("I didnt't say v")

if 'v' in color:
    print('omg that is such a pretty color')
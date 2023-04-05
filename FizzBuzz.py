# from oop basics

fb_list = [], []


while user_names.strip().lower() != 'leave':
    fb_list[0].append(user_number)
    fb_list[1].append(user_names)
    user_names = str(input("what would you want to call your number ? /nType 'leave' when done: "))
    if user_names.strip().lower() == 'leave':
        break
    else:
        user_number = int(input("Type the number: "))

# append values to list using dict, convert list to a zip, similar to a dict structure, mutable, zip is used to make a
#     bridge between
fb_zip = zip(fb_list[0]. fb_list[1])
fb_dict = dict(fb_zip)









# class FizzBuzz:
#     def play(self):
#         for counter in range(300):
#             output = ""
#             for number
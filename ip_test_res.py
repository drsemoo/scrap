import os

print(os.popen('ping 156.219.198.'+str(4)).read())

# for i in range(254):
#     x = os.popen('ping 156.219.198.'+str(4)).read()
#     if x :
#         print(x)

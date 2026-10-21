try:
    f=open('simple.txt','r')
    f.write('Test write to simple text !')
except IOError:
    print("Error couldn't find the file ")
finally:
    print('i always runs')
# else:
#     print("Success")
#     f.close()

# f=open('simple.txt','r')
# f.write('Test write to simple text !')
# print("Hello")
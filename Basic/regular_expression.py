import re
patterns=['term1','term2']

text='This is the string with term1 , not the other !'

for pattern in patterns:
    print("I m searching for :"+pattern)

    if re.search(pattern,text):
        print('Match')
    else:
        print('Not match')

# search --> pattern & text


match=re.search('term1',text)

print(type(match))
print((match.start()))

split_term="@"
email="user@gmai.com"

match=re.split(split_term,email)

print(match)


a=re.findall('match','test phase match is middle match')
print(a)


def multi_re_find(patterns,phase):

    for pat in patterns:
        print("Searching for the pattern {}".format(pat))
        print(re.findall(pat,phase))
        print("\n")

test_phase='sdsd...ssdddd!.sdddsdd.dsds..dssssss...sddddd'

#* is zero to more
#+ is 1 or more
#? is zero or more
#{n,n} is number of times, list of number
#[s] is string 
#^ exclude
# [a-z] list of lowercase
# [A-Z] list of uppercase


test_patterns=['[a-z]+']

multi_re_find(test_patterns,test_phase )


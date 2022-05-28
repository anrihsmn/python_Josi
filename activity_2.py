
# how to count character or index

# name = "Kazuo Ishiguro"
# vegetables = ['cabbage','cucamber','lettuce']

# print(len(name))
# print(len(vegetables))


string1 = "harukimurakami"
string2 = "sosekinatsume"

print(string1 == string2)


username = input('enter your name: ')
userpassword = input('enter your password: ')

if len(username) >= 8 and len(userpassword) >= 8:
    if username == 'testusername' and userpassword == 'testpassword':
      print('login success')
    else:
      print('login failed')
else:
  print('username and password must be at least 8 characters')





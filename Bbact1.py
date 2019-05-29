class Account:

    def setUsername(self,uname):
        self.username = uname
    def setPassword(self,pword):
        self.password = pword
    def setName(self,name):
        self.name = name

userFile = open(r'userinfo.csv','r')

user = Account()
accountBasis = Account()
uName = input("Username: ")
pWord = input("Password: ")


if uName.__len__() > 0 and pWord.__len__() > 0:
    user.setUsername(uName)
    user.setPassword(pWord)
    num = 0
    for fileLine in userFile.readlines():
      userInfo = fileLine.split(',')
      accountBasis.setUsername(userInfo[0])
      accountBasis.setPassword(userInfo[1])
      accountBasis.setName(userInfo[2])

      if user.username == accountBasis.username and user.password == accountBasis.password:
        user.setName(accountBasis.name)
        print("Hello " + user.name[:-1] + "! You have successfully logged in.")
        num = 2
      elif user.username == accountBasis.username and user.password != accountBasis.password:
          num = 1

    userFile.close()

    if num == 1:
        print("Wrong password entered")
    elif num < 1:
        print("The account does not exist")
else:
    print("CANNOT ACCEPT BLANK INPUTS!")
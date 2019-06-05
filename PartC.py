if uName.__len__() > 0 and pWord.__len__() > 0:
    user.setUsername(uName)
    user.setPassword(pWord)
    num = 0
    for fileLine in userFile.readlines():
      userInfo = fileLine.split(',')
      accountBasis.setUsername(userInfo[0])
      accountBasis.setPassword(userInfo[1])
      accountBasis.setName(userInfo[2])

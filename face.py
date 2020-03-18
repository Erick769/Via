#face
userdict = {"x" : "x"}
def connectuser():
  user= input ("Email ou telefone ")
  senha=input('Senha ')
  if user in userdict and userdict[user] == senha:
    print ("login feito com sucesso!")
  else:
    print ("Usuario ou senha invalidos!")
connectuser()

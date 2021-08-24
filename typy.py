"""
classe destinada a tipagem de dados em python.

uso:
    declarar:
        v = typy(<valor>,<tipo>)
    modificar valor:
        v.set(<valor>)
    buscar valor:
        v.get()
        v.getType()
    converter para variavel não tipada:
        typy(<[variavel,list contendo variavel,dicionario contendo variavel]>,"wt").wt()

dicas:
    caso n saiba o tipo especifico usar typy(<variavel>,type(<variavel>))
"""
class typy:
    value = None
    tipo = None
    v_wt = {}
    def __init__(self,x,tipo):
        if x != None:
            if tipo == "wt":
                self.v_wt = x
            else:
                if type(x) == tipo:
                    self.value = x
                    self.tipo = tipo
                else:
                    self.error("tipo da variavel e "+str(tipo)+" e não "+str(type(x))) 
        else:
            self.tipo = tipo            

    def wt(self):
        if type(self.v_wt) == type({}):
            self.v_wt = self.strObj(self.v_wt)
        elif type(self.v_wt) == type([]):
            self.v_wt = self.strLst(self.v_wt)
        return self.v_wt

    def strLst(self,l):
        lst = []
        c = typy("",str)
        c2 = []
        c3 = {}
        for i in l:
            if type(i) == type(c):
                lst.append(i.get())
            elif type(i) == type(c2):
                lst.append(self.strLst2(i))
            elif type(i) == type(c3):
                lst.append(self.strObj(i))    
            else:
                lst.append(i)
        return lst
    
    def strLst2(self,l):
        lst = []
        c = typy("",str)
        c2 = []
        c3 = {}
        for i in l:
            if type(i) == type(c):
                lst.append(i.get())
            elif type(i) == type(c2):
                lst.append(self.strLst(i))
            elif type(i) == type(c3):
                lst.append(self.strObj(i))    
            else:
                lst.append(i)
        return lst
    
    def strObj(self,x):
        obj = {}
        for i in x.items():
            c = typy("",str)
            c2 = []
            c3 = {}
            if type(i[1]) == type(c):
                obj[i[0]] = i[1].get()
            elif type(i[1]) == type(c2):
                obj[i[0]] = self.strLst(i[1])    
            elif type(i[1]) == type(c3):
                obj[i[0]] = self.strObj2(i[1])
            else:
                obj[i[0]] =i[1]
        return obj

    def strObj2(self,x):
        obj = {}
        for i in x.items():
            c = typy("",str)
            c2 = []
            c3 = {}
            if type(i[1]) == type(c):
                obj[i[0]] = i[1].get()
            elif type(i[1]) == type(c2):
                obj[i[0]] = self.strLst(i[1])    
            elif type(i[1]) == type(c3):
                obj[i[0]] = self.strObj(i[1])
            else:
                obj[i[0]] =i[1]
        return obj

    def get(self):
        return self.value
    
    def getType(self):
        return self.tipo

    def set(self,value):
        if type(value) == self.tipo:
            self.value = value
        else:
            self.error("tipo da variavel e "+str(self.tipo)+" e não "+str(type(value)))
            self.error("o valor da variavel permanece: "+str(self.value)) 

    def error(self,x):
        print('\033[1;31m'+x+'\033[1;97m')
import random
class RandomGenerator: 
    
    def __str__(self):
        StringList=['q','w','f','a']
        SymbolList=['@','#','%','$','!']
        RandomString=random.choices(StringList,k=5)
        RandomSymbol=random.choices(SymbolList,k=3)
        String= "".join(RandomString)
        Symbol="".join(RandomSymbol)
        FinalPass=String + Symbol
        self.Password=FinalPass
        return self.Password

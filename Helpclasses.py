import re

class ilocException(Exception):
    pass

class plocException(Exception):
    pass

class Index(dict):
    def __getitem__( self, key ):
        if not self.has_key( key ):
            super(Index,self).__setitem__( key, [] )
        return super(Index,self).__getitem__( key )

    def iloc(self):
        maskeys=self.keys()
        for key in maskeys:
            if(not isinstance(key,str)):
                raise ilocException('iloc Function cannot work with dictionary with nonstring keys')
        maskeys=sorted(maskeys)
        masitems=[]
        for elem in maskeys:
            masitems.append(self[elem])
        return(masitems)


class Forploc(dict):
    def __getitem__(self,key):
        symbols=['>','<','=',0,1,2,3,4,5,6,7,8,9,'0','1','2','3','4','5','6','7','8','9']
        operations=['>','<','=','>=','<=','==']
        result=[]
        result1=dict()
        if(isinstance(key, str)):
            cons=re.findall(r'[<>=][<>=]?\d+\.?\d*',key)
            if(cons==None or len(cons)==0):
                raise plocException("Invalid key for ploc function")
                
            if(len(cons)>1):
                underkey=key.replace(')','')
                underkey=underkey.replace('(','')
                razdelitel=re.search(r'[<>=][<>=]?\d+\.?\d*((\s*[^<>=0-9]\s*))',underkey)
                if(razdelitel!=None):
                    razdelitel=(razdelitel.group(0))
                    razdelitel=razdelitel.replace(' ','')
                    #print(razdelitel)
                    razdelitel=razdelitel[-1]
                else:
                    raise plocException('No separator found')
                razdelitel=razdelitel.replace(' ','')
                if(razdelitel in symbols):
                    razdelitel=''
                checkstring1=''
                for part in range(len(cons)-1):
                    checkstring1=checkstring1+cons[part]+razdelitel
                checkstring1+=cons[-1]
            else:
                checkstring1=cons[0]
            checkstring2=key.replace(' ','')
            checkstring2=checkstring2.replace(')','')
            checkstring2=checkstring2.replace('(','')
            
            #print(key,' ',checkstring1,' ',checkstring2)
            if(checkstring1!=checkstring2):
                raise plocException('Invalid key for ploc function')
            exps=[]
            digitss=[]
            l=0
            for con in cons:
                exps.append((re.search(r'[<>=][<>=]?',con)).group(0))
                if(exps[l] in operations):
                    pass
                else:
                    raise plocException('invalid key for ploc function')
                digitss.append(float((re.search(r'\d+\.?\d*',con)).group(0)))
                l+=1
            for keyk in self.keys():
                corrected=True
                if(not isinstance(keyk,str)):
                    raise plocException('ploc Function cannot work with dictionary with nonstring keys')
                if(re.search(r'[A-Za-z]',keyk)!=None):
                    corrected=False
                else:
                    mapdigitsstr=re.findall(r'\d+\.?\d*',keyk)
                    if(len(mapdigitsstr)==len(exps)):
                        mapdigits=[]
                        for apdigitstrr in mapdigitsstr:
                            mapdigits.append(float(apdigitstrr))
                        for i in range(len(exps)):
                            if(exps[i]=='>'):
                                if(mapdigits[i]<=digitss[i]):
                                    corrected=False
                            if(exps[i]=='<'):
                                if(mapdigits[i]>=digitss[i]):
                                    corrected=False
                            if(exps[i]=='=='):
                                if(mapdigits[i]!=digitss[i]):
                                    corrected=False
                            if(exps[i]=='>='):
                                if(mapdigits[i]<digitss[i]):
                                    corrected=False
                            if(exps[i]=='<='):
                                if(mapdigits[i]>digitss[i]):
                                    corrected=False
                            if(exps[i]=='<>'):
                                if(mapdigits[i]==digitss[i]):
                                    corrected=False
                    else:
                        corrected=False
                    
                    if(corrected==True):
                        result.append(keyk)
                        result1[keyk]=self.get(keyk)
            return result1

        else:
            raise plocException("Not a string key for ploc function")


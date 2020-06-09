import math
class shusu:
    def __init__(self,num):
        self.max_num=num
        self.data=[]
        self.data.append(2)
    def __iter__(self):
        self.get_num=0
        self.index=2
        return self
    def __next__(self):
        self.get_num+=1
        if self.get_num<=len(self.data):
            return self.data[self.get_num-1] 
        if self.get_num==self.max_num:
            raise StopIteration
        self.index+=1
        flag=False;
        while flag==False:
            flag=True
            for a in range(2,int(math.sqrt(self.index))+2):
                if self.index%a==0:
                    self.index+=1
                    flag=False
                    break
        self.data.append(self.index)
        return self.index

if __name__=='__main__':
    print([a for a in shusu(10)])


                    

                
                
            
            



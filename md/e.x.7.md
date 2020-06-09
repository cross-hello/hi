1. create a generator and using next method
~~~python

def li():
    for a in range(1,11):
        yield a
if __name__=='__main__':
    l=[a for a in li()]
    print(l)
    a=li()
    print(next(a))
~~~
<img src="genertor.png" alt=" photo of experiment about generator" title="First Question screenshot" />

2. design a class calculate shusu.
~~~python
  
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
~~~

<img src="shusu.PNG" alt="class experiment of shusu" title="shusu" />                    
&copy;MMXX simple _ ~ _ All rights reserved. 

                
                
            
            



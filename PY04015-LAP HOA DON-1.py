from math import *

class kh:
    def __init__(self, ma, ten, tien):
        self.ma=ma
        self.ten=ten
        self.tien=tien
    def kq(self):
        print(self.ma,self.ten,self.tien)
 
if __name__ == '__main__':
    a=[]
    for t in range (1,int(input())+1):
        s=input()
        cu=int(input())
        moi=int(input())
        n=moi-cu
        if n<=50:
            tien=n*102
        elif n<=100:
            tien=round(n*150*1.03-2575)
        else:
            tien=n*210-7875
        if t<10:
            b=kh("KH0"+str(t),s,tien)
        else:
            b=kh("KH"+str(t),s,tien)
        a.append(b)
    a.sort(key=lambda x:(-x.tien))
    for i in a:
        i.kq()

        

        
            

            





        
    


    



        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    







        
        
        
        

                
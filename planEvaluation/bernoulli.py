import numpy as np#created a bernoulli class
 
class bernoulli():   
    def pmf(x,p):
        """
        probability mass function        
        """
        f = p**x*(1-p)**(1-x)
        return f
    
    def mean(p):
        """
        expected value of bernoulli random variable
        """
        return p
    
    def var(p):
        """
        variance of bernoulli random variable
        """
        return p*(1-p)
    
    def std(p):
        """
        standart deviation of bernoulli random variable
        """
        return bernoulli.var(p)**(1/2)
    
    def rvs(p,size=1):
        """
        random variates
        """
        rvs = np.array([])
        for i in range(0,size):
            if np.random.rand() <= p:
                a=1
                rvs = np.append(rvs,a)
            else:
                a=0
                rvs = np.append(rvs,a)
        return rvs
    
if __name__ =="__main__":
   p = 0.2 # probability of having an accident

   print(bernoulli.mean(p))
   print(bernoulli.var(p))
   print(bernoulli.std(p))
   #each execution generates random numbers, so array may be change
   print(bernoulli.rvs(p,size=10)) 
    
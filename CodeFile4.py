class IteratorClass:
    # Complete this class! It takes in three inputs when initializing.
    # input#1 x -- is a sequence, either a list or a tuple. Raise a ValueError if it is not a list or a tuple
    # input#2 y -- is a sequence, either a list or a tuple. Raise a ValueError if it is not a list or a tuple
    # input#3 operator -- is a string that can either be 'add', 'sub', 'mul', 'div' -- If the specified operator
    # is not one of these, raise a ValueError.

    # Complete the class by writing functions that will turn it into an iterator class.
    # https://www.programiz.com/python-programming/methods/built-in/iter
    # The purpose of the class is to take two lists(x and y), apply the specified operator and return the output
    # as an iterator, meaning you can do "for ele in IteratorClass(x,y,'add')"
    # NOTE: For the / operator, round to two decimal places
    # Raise ValueError when the length is not the same for both inputs
    # Raise ValueError when the operator is not add, sub, mul, or div.

    # BEGIN SOLUTION
    def __init__(self,x,y,operator):
        
        if not isinstance(x, (tuple,list)):
            raise ValueError("input 1 should be list or a tuple")
            
        elif not isinstance(y, (tuple,list)):
            raise ValueError("input 2 should be list or a tuple")
            
        elif operator not in ['add', 'sub', 'mul', 'div']:
            raise ValueError("input 3 shouldbe  'add','sub','mul','div'")
        
        elif len(x)!=len(y):
            raise ValueError("inputs x and y should have same length")
        
        self.x=x
        self.y=y
        self.operator=operator
        
        
    def __iter__(self):
        self.value=0
        return self

    def __next__(self):
        if len(self.x)>self.value:
            if self.operator=='add':
                total=self.x[self.value]+self.y[self.value]
            elif self.operator=='sub':
                total=self.x[self.value]-self.y[self.value]
            elif self.operator=='mul':
                total=self.x[self.value]*self.y[self.value]
            elif self.operator=='div':
                total=round(self.x[self.value]/self.y[self.value],2)
            self.value +=1
        else:
            raise StopIteration
        return total
    

    # END SOLUTION


class ListV2:
    # Complete this class to fulfill the following requirement
    # 1) The class only takes one input argument which is a list or a tuple;
    #    Raise ValueError if the input is not a list or tuple
    # 2) The class overload loads +,-,*,/ and returns a ListV2 object as the result
    # 3) The class can handle +,-,*,/ for both list and int/float, meaning the thing to the right of the operator
    #    can be a sequence or a number;
    # 4) The class is an iterator
    # HINT: Study the assert statements in the test file to understand how this class is being used and reverse engineer it!
    # NOTE: For the / operator, round to two decimal places

    # BEGIN SOLUTION
    
    def __init__(self,x):
        if not isinstance(x,(tuple,list)):
            raise ValueError("Input is not a list or tuple")
        else:
            self.x=x
            self.value=0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.x)>self.value:
            result=self.x[self.value]
            self.value = self.value + 1
            return result 
        else:
            raise StopIteration
            
    def __add__(self, other):
        if isinstance(self.x,(ListV2,tuple,list)) and isinstance(other,(ListV2,tuple,list)):
            return ListV2([a + b for a, b in zip(self, other)])
        if isinstance(other, (int, float)):
            return ListV2([a+other for a in self])
        
        
    def __sub__(self, other):
        if isinstance(self.x,(ListV2,tuple,list)) and isinstance(other,(ListV2,tuple,list)):
            return ListV2([a - b for a,b in zip(self, other)])
        elif isinstance(other, (int, float)):
            return ListV2([a-other for a in self])
        
    def __truediv__(self, other):
        if isinstance(self.x,(ListV2,tuple,list)) and isinstance(other,(ListV2,tuple,list)):
            return ListV2([round(a / b,2) for a,b in zip(self, other)])
        elif isinstance(other, (int, float)):
            return ListV2([round(a/other,2) for a in self])
    
    def __mul__(self, other):
        if isinstance(other,(ListV2,tuple,list)):
            return ListV2([a * b for a,b in zip(self, other)])
        elif isinstance(other, (int, float)):
            return ListV2([a*other for a in self])
        
        
    def __repr__(self):
        return f'{self.x}'


    

    # END SOLUTION
class Pound:
    """
    - class represents weight in lb and oz
    - 1 lb has 16 oz
    - add addition functionality
    - add subtraction functionality. Make sure to raise an error if the resulting value is negative. Infer the error type and message form the test.
    - add a human readable representation that looks like --> 17 lb 4 oz
    - add an unambiguous representation that looks like --> Pound(17, 4)
    
    """
    # BEGIN SOLUTION
    def __init__(self,lb,oz):
        self.lb=lb
        self.oz=oz
    
    def __add__(self,other):
        lb1=self.lb+other.lb
        oz1=self.oz+other.oz
        if oz1>=16:
            lb1=lb1+oz1//16
            oz1=oz1%16
        return Pound(lb1,oz1)
    
    def __sub__(self,other):
        lb1=self.lb-other.lb
        oz1=self.oz-other.oz
        if lb1<0:
            raise ValueError("The value is less than 0")
        if oz1 < 0:
            lb1 = lb1-1
            oz1 = oz1+16

        return Pound(lb1,oz1)
            
    def __repr__(self):
        return f"Pound({self.lb}, {self.oz})"

    def __str__(self):
        return f"{self.lb} lb {self.oz} oz"
        



    # END SOLUTION
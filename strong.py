
def factorial(number): 
  
    fact = 1
      
    if number == 0 or number == 1 : 
        return fact 
      
    for i in range(2, number + 1) : 
        fact *= i 
      
    return fact 
          
def find_strong_numbers(num_list): 
    result = [] 
      
    
    for num in num_list : 
        sum = 0
        temp = num 
          
        # loop till number is not zero 
        while num != 0 : 
              
            r = num % 10
              
            # function call 
            sum += factorial(r) 
              
            num //= 10
          
        # check number is strong or not 
        if sum == temp: 
              
            # adding number to the list 
            result.append(temp) 
           
    # return list of strong numbers    
    return result 
              
  

if __name__ == "__main__" : 
      
    num_list = [145, 375, 100, 2, 10, 40585, 0] 
      
    # function call 
    strong_num_list = find_strong_numbers(num_list) 
      
    # loop till list is not empty 
    for strong_num in strong_num_list : 
        print(strong_num, end =" ") 
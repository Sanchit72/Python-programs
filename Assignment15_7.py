#Write a lambda function using Filter() which accepts a list of string and return a list of String having length greater than 5

Greater = lambda strings : len(strings) > 5  

def main():
    
    strings = list()
    
    no = int(input("Enter how many strings you want to store : "))
    for i in range(no):
        print("Enter", i+1 ," string : ", end='')
        strings.append(input())
        
    FData = list(filter(Greater , strings))
    print("After Filter Data: ",FData)    

if __name__ == "__main__":
    main()
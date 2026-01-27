#Design a python application that create two thread thread i should compute the sum of elements from a list thread2 should compute the product of element from the same list return the result to the main thread and dispaly them
import threading
def compute_sum(data, result, index):
    total = sum(data)
    result[index] = total
def compute_product(data, result, index):
    product = 1
    for num in data:
        product *= num
    result[index] = product
    
def main():
    Data = []
    print("Enter Number of Elements: ")
    No = int(input())
    
    for i in range(No):
        print("Enter The Element:", i + 1)
        element = int(input())
        Data.append(element)
        
    print("Data is:", Data)
    
    result = [0, 0]  # To store sum and product results
    
    sum_thread = threading.Thread(target=compute_sum, args=(Data, result, 0))
    product_thread = threading.Thread(target=compute_product, args=(Data, result, 1))
    
    sum_thread.start()
    product_thread.start()
    
    sum_thread.join()
    product_thread.join()
    
    print("Sum of elements:", result[0])
    print("Product of elements:", result[1])
    
if __name__ == "__main__":
    main()
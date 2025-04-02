class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n=len(arr)
        if d>n:
            d=d%n
        temp1=arr[:d]
        temp2=arr[d:]
        
        for i in range(n-d):
            arr[i]=temp2[i]
        for i in range(d):
            arr[n-d+i]=temp1[i]
        
        
        
            
        
        return arr
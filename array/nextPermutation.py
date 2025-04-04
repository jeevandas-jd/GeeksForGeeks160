class Solution(object):


    def backTrack(self,arr,result,temparr):

        if len(temparr)==len(arr):
            result.append(temparr[:])
            return
        for i in range(len(arr)):
            if arr[i] in temparr:
                continue
            temparr.append(arr[i])
            self.backTrack(arr,result,temparr)
            temparr.remove(temparr[-1])
        return result


    def NextPermutation(self,arr):

        result=[]

        result=self.backTrack(arr,result,[])
        #print(f"result={result}")
        return result
    
def perMutation(arr,isInclude,stak):



    return arr
if  __name__=="__main__":
    arr=[2,4,1,5,7,0]

    s=Solution()
    ans=s.NextPermutation(arr)

    print(f"printing answer={ans}")
    
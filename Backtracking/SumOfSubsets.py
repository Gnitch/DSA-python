def SumOfSubsets(curSum, curEle, sumOfAll):
    ans[k] = 1
    for i in range(curEle+1, len(weight)):
        ans[i] = 0
    if curSum+weight[curEle] == sumOfEle:
        print(ans)
        
    elif curSum+weight[curEle]+weight[curEle+1] <= sumOfEle:
        SumOfSubsets(curSum+weight[curEle], curEle+1, sumOfAll-weight[curEle])
    
    if curSum+(sumOfAll-weight[curEle]) >= sumOfEle and curSum+weight[curEle+1] <= sumOfEle:
        ans[k] = 0
        SumOfSubsets(curSum, curEle+1, sumOfAll-weight[curEle])

weight = list(map(int, input("Enter Weights:").split()))
ans = [0]*len(weight)
sumOfEle = int(input("Enter sum:"))
print("\nAns:")
SumOfSubsets(0, 0, sum(weight))

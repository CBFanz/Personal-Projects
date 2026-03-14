import random

inp = list(input("Enter a word or number: "))
#lists 
abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']+list(range(0,10))

ans = list(range(len(inp)))
for i in range(len(inp)):
    for k in abc:
        ansstr = ''
        ans[i] = k


        for m in range(1+i,len(inp)):
            ans[m] = random.choice(abc)


        
        "string converter"
        for l in ans:
            ansstr += str(l)
        print(ansstr)
        
        
        if ans[i] == inp[i]:
            break






d_1ewdn1ox = input('')
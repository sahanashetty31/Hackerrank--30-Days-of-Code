
# coding: utf-8

# In[1]:


class Calculator(object):
    def power(self, n, p):
        if(n < 0) and (p < 0):
            raise exception("n and p are non-negative")
        else:
            return n ** p
myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except exception as e:
        print(e)


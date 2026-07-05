class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        for num in nums:
            pre.append(pre[-1] * num)
        
        post = [1]
        for num in nums[::-1]:
            post.append(post[-1] * num)
        post = post[::-1]

        res = []
        for i in range(len(nums)):
            res.append(pre[i] * post[i + 1])
            
        return res
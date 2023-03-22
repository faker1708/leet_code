class Solution:
    def twoSumClosest(self,nums: List[int], target_tow: int)->int:
        for j ,nb in enumerate(nums):
            diff = target_tow - nb
            # 找到地址不等于j ，但价值与nb最近的两个元素



# 好麻烦，大概就这思路，先不写了，看看人家是不是这思路再说 吧。不然写不不对，就太浪费时间了。



    def threeSumClosest(self, nums: List[int], target: int) -> int:

        # 先固定一个指针，然后把问题降级成两数
        
        nums.sort()
        # n = len(nums)
        # for i in range(0,n):
        for i ,na in enumerate(nums):
            target_tow = target-na
            # 以下，问题变成2元
            twoSumClosest(self,nums,target_tow)



        # 不想写了。下班。麻烦死了。先看吧，多看少写。
        # hr一个电话，烦人，瞬间没劲了。

        
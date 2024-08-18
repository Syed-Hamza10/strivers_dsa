def removeDuplicates( nums) -> int:
        st = set()

        for i in nums:
            st.add(i)

        idx = 0
        for i in st:
            nums[idx] = i
            idx +=1

        n = len(st)
        return (n, nums)


print(removeDuplicates([11,22,33,44,5555,66,66,77,77]))
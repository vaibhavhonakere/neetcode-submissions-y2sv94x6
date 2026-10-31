class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1

        while(m > 0 and n > 0):
            m_index = m - 1
            n_index = n - 1

            # print(last, nums1)
            if(nums1[m_index] > nums2[n_index]):
                nums1[last] = nums1[m_index]
                # last -= 1
                m -= 1
            else:
                nums1[last] = nums2[n_index]
                n -= 1
            
            # print(nums[last])
            last -= 1
        
        while(m > 0):
            m_index = m - 1 
            nums1[last] = nums1[m_index]
            last -= 1
            m -= 1

        while(n > 0):
            n_index = n - 1 
            nums1[last] = nums2[n_index]
            last -= 1
            n -= 1

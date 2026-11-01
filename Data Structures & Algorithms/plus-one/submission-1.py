class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        new_output = []

        for i in range(len(digits) - 1, -1, -1):
            num = (digits[i] + carry) % 10
            carry = (digits[i] + carry) // 10
            new_output.append(num)
        
        if(carry):
            new_output.append(carry)
        
        return new_output[::-1]
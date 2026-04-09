class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a,b,c=0,0,0

        for x,y,z in triplets:
            if(x > target[0] or y > target[1] or z > target[2]):
                continue
            if(x == target[0]):
                a=1
            if(y == target[1]):
                b=1
            if(z == target[2]):
                c=1
        

        return a==b==c==1
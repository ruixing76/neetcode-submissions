class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers represents each bar position
        # moving longer bars will always decrease the max area
        # so the only way is to move the lower bars and check if we can get larger area
        i, j=0, len(heights)-1
        max_area=0
        while i<j:
            width=j-i
            cur_area=min(heights[i],heights[j])*width
            max_area=max(max_area,cur_area)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return max_area

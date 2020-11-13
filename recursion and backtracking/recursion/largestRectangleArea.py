class Solution:
    def largestRectangleArea(self, heights):
        '''
        The idea is that we create a stack and store indices of bars in
        ascending order, and as soon as we encounter a bar that breaks the
        pattern i.e it's height is less than the top most bar in the stack,
        we calculate the areas of all the bars in the stack and compare it to the max value
        and continue forming the pattern in the stack
        '''
        heights.append(0)
        stack = [-1]
        area = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                # calculate bars area
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                area = max(area, h*w)
            stack.append(i)
        return area
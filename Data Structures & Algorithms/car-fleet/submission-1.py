class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] # times
        # sorted in closest to furthest
        cars = list(reversed(sorted(zip(position, speed))))

        for car in cars:
            time = (target - car[0]) / car[1]

            if not stack:
                stack.append(time)
            elif stack[-1] < time:
                stack.append(time)
        
        return len(stack)
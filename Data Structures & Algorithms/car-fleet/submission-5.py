class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combo = [(position[i], speed[i]) for i in range(len(speed))]
        combo.sort(key = lambda x:x[0], reverse = True)

        fleets = 1
        time = (target - combo[0][0]) / combo[0][1]

        for i in range(1, len(speed)):
            t = (target - combo[i][0]) / combo[i][1]
            if t > time:
                time = t
                fleets += 1
                
        return fleets


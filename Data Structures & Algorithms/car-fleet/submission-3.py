class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combo = [(position[i], speed[i]) for i in range(len(speed))]
        combo.sort(key = lambda x:x[0], reverse = True)

        lastTime = (target - combo[0][0]) / combo[0][1]
        count = 1

        for i in range(1, len(speed)):
            time = (target - combo[i][0]) / combo[i][1]
            if time > lastTime:
                lastTime = time
                count += 1

        return count




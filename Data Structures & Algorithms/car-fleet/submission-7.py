class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combo = [(p, s) for p, s in zip(position, speed)]
        combo.sort(key = lambda x : x[0], reverse = True)
        nFleets = 1
        initial_time = (target - combo[0][0]) / combo[0][1]

        for i in range(1, len(combo)):
            time = (target - combo[i][0]) / combo[i][1]
            if time > initial_time:
                initial_time = time
                nFleets += 1

        return nFleets

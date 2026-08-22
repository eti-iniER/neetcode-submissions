class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        fleet_count = 0
        data = []

        for i in range(n):
            time_to_reach_target = (target - position[i]) / speed[i]
            data.append((i, time_to_reach_target))
        
        data.sort(key = lambda x: position[x[0]], reverse=True)

        last_max = -1

        for i, time_to_reach_target in data:
            if time_to_reach_target > last_max:
                fleet_count += 1
                last_max = time_to_reach_target

        return fleet_count
class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        n = len(landStartTime)
        m = len(waterStartTime)

        ans = float('inf')

        for i in range(n):
            land_start = landStartTime[i]
            land_end = land_start + landDuration[i]

            for j in range(m):
                water_start = waterStartTime[j]
                water_end = water_start + waterDuration[j]

                # Case 1: land -> water
                start_land = land_start
                finish_land = start_land + landDuration[i]
                start_water = max(finish_land, water_start)
                ans = min(ans, start_water + waterDuration[j])

                # Case 2: water -> land
                start_water = water_start
                finish_water = start_water + waterDuration[j]
                start_land2 = max(finish_water, land_start)
                ans = min(ans, start_land2 + landDuration[i])

        return ans
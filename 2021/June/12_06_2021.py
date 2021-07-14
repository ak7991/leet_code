from typing import List
import bisect

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        cap_non_stop_stations = []

        pos = 0
        stops = 0
        while pos < target:
            # print("skipped stations", cap_non_stop_stations)
            # Have enough fuel to complete journey
            if pos + startFuel >= target:
                break
            # Current fuel cannot reach next station
            if stations == [] or startFuel < (stations[0][0] - pos):
                # No stations left that could have been stopped at
                if cap_non_stop_stations == []:
                    stops = -1
                    break
                # Stopping at the station providing max fuel
                elif (stations != [] and pos + startFuel < stations[0][0]) or (stations == []):
                    refuel_station_cap = cap_non_stop_stations.pop()
                    # print(f"Backtracking to stop at station that provided max fuel; {refuel_station_cap}; new possible pos: {pos+refuel_station_cap+startFuel}")
                    startFuel += refuel_station_cap
                    stops += 1
            # Current fuel can reach/cross the next station
            if pos + startFuel < target:
                pos += startFuel
                startFuel = 0
                while stations != [] and stations[0][0] <= pos:
                    possible_refuel = stations.pop(0)
                    # print(f"Skipping fueling station; pos = {pos}; {possible_refuel}")
                    cap_non_stop_stations.insert(bisect.bisect_left(cap_non_stop_stations, possible_refuel[1]), possible_refuel[1])
        return stops

if __name__ == "__main__":
    s = Solution()
    target = 120
    startFuel = 10
    stations = [[10,60],[20,30],[30,30],[60,40]]
    print(s.minRefuelStops(target, startFuel, stations))
    print(">>>>")
    target = 100
    startFuel = 50
    stations = [[25,25],[50,50]]
    print(s.minRefuelStops(target, startFuel, stations))
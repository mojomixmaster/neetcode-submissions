class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        from collections import deque
        # given an array of temperatures where each index corresponds to the temperature
        # on that index's corresponding day, find the number of days after temp[i] i.e.
        # the temp on day i, until the temperature is greater.

        # most obvious approach?
        # loop through temperatures, for each temperature
        # start a counter at 0 and loop again from temp to end of array
        # until a temp > current_temp found. append counter value to result.
        # this is O(n^2) time and O(n) space.

        # can we find an O(n) time approach?

        q = deque() # monotonically decreasing queue (queue must be in strictly decreasing order)
        result = [0] * len(temperatures)
        l = 0

        while l < len(temperatures):

            while q and temperatures[q[-1]] < temperatures[l]: # comparison needs to be with temp VALUES not indices
                i = q.pop()
                print(i)
                result[i] += l-i

            q.append(l)
            l += 1
            print(q)

        return result



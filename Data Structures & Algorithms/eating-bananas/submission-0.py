class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        # abstract the problem statement: 
        # we have a sequenece of piles of bananas. We are given h hours to eat each pile
        # and we need to find the minimum integer rate of bananas-consumed-per-hour to eat
        # each banana in each pile.

        # caveat: a maximum of ONE pile is allowed to be consumed per hour

        # naively: you try eating rates from 1, incrementing by 1 each time
        # until you hit a rate, k , that means all bananas are consumed in <= h hours.

        # for each eating rate, loop through each pile and calculate how many hours
        # required to eat pile e.g.: pile[0] = 2 and eating rate = 2 therefore
        # n_hours_required_to_consume_pile = n_bananas / k = 2/2 = 1 (must be rounded up)
        # add this value to total_hours_required sum and if total_hours_required <= h, then 
        # return this eating rate (as we want the MINIMUM ie first rate that does the job)

        # this is O(n^2)... is there a faster approach?

        # what if we gallop searched until we hit an eating rate,k, that gives total_hours_required <= h.
        # then we can binary search from 0 to k' and check if there any eating rates less than k'
        # that also satsify <= h. min_valid_eating_rate = min(k', current_k_candidate) during the actual binary search
        # section of the algorithm (2nd while loop). 2 binary searches and one loop through piles is O(nlogm)!
 
        i, k = 0, 0 # i is the exponent we raise 2 to, to obtain the value of k each iteration
        while k < max(piles):
            k = 2**i
            total_hours_required = 0
            for j in piles:
                total_hours_required += math.ceil(j / k)
                if total_hours_required > h: break # no need to continue looping through piles, we've already exceeded time limit. This value of k is too small!

            if total_hours_required <= h: # we've found the upper bound for valid k's!
                break
            
            i += 1 # our eating rate is still too small, increment i and evaluate the next k= 2**i
        
        l, r = 1, k # now we binary search within the confirmed range of k to find minimum k within it that is valid
        min_k = r # min_k is initialised to the only k (max k) that has been validated in the search window

        while l < r:
            candidate_k = l + (r-l)//2
            print(candidate_k)
            total_hours_required = 0
            for j in piles:
                total_hours_required += math.ceil(j / candidate_k) # round total eating time UP as we can only consume 1 pile an hour anyways! 
                # e.g: 4.3 hours means we need to wait 0.7 hours to start eating new pile on hour 5

                if total_hours_required > h: # no need to continue looping through piles, we've already exceeded time limit. This value of k is too small!
                    l = candidate_k+1 # discard current_k from search window as too small and slide l to the integer just after it
                    print("breaking daddy!")
                    break 
            
            if total_hours_required <= h:
                min_k = min(min_k, candidate_k)
                r = candidate_k # see if we can go even smaller

        return min_k

        








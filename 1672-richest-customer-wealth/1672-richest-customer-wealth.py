class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts)) 
        # mapping sum onto all elements of accounts then 
        # grabbing the account that has the max. value compared to the others
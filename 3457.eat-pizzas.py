class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        # Sort pizzas in descending order to prioritize larger weights
        pizzas.sort(reverse=True)
        
        n = len(pizzas)
        days = n // 4
        
        # Calculate number of odd and even days
        # Day 1 is odd, Day 2 is even, Day 3 is odd, etc.
        n_odd = (days + 1) // 2
        n_even = days // 2
        
        # On odd days, we gain the heaviest pizza (Z) in the group of 4.
        # To maximize this, we take the absolute largest pizzas.
        total_weight = sum(pizzas[:n_odd])
        
        # On even days, we gain the second heaviest pizza (Y) in the group.
        # This requires one pizza in the group to be larger than the gain (Z >= Y).
        # We use the next largest available pizzas to fill these roles.
        # For each even day, we skip one pizza (Z) and take the next (Y).
        # Start index is n_odd, skip index n_odd, take index n_odd + 1, and so on.
        even_gains_start = n_odd + 1
        even_gains_end = n_odd + 2 * n_even
        total_weight += sum(pizzas[even_gains_start : even_gains_end : 2])
        
        return total_weight

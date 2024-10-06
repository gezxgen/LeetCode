class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = 0
        L = 0
        basket = {}  # A dictionary to store the count of each type of fruit
        
        for R in range(len(fruits)):
            basket[fruits[R]] = basket.get(fruits[R], 0) + 1
            
            while len(basket) > 2:  # More than 2 types of fruits in the basket
                basket[fruits[L]] -= 1
                if basket[fruits[L]] == 0:
                    del basket[fruits[L]]  # Remove the fruit from the basket if its count becomes 0
                L += 1  # Shrink the window from the left
                
            window = max(window, R - L + 1)  # Calculate the maximum window size
        
        return window
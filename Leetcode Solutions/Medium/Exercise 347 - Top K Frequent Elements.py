# Exercise 347: Top K Frequent Elements
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        counts = Counter(nums)
        top_k = counts.most_common(k)
        for small_list in top_k:
            first_number = small_list[0]
            result.append(first_number)
        return result

# This uses Counter class to count frequencies and most_common method to get top k frequent elements.
# Writing a variation of this without Counter would involve manually counting frequencies using a dictionary.
# The variant would be less efficient and more verbose compared to using Counter.
# Writing the variant:
class SolutionVariant:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        for num in nums:
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1
# Explanation of the code above: This part counts the frequency of each number in the input list using a dictionary.
# Next, we need to sort these frequencies and extract the top k elements.
        # Create a list of (num, frequency) tuples
        freq_list = [(num, freq) for num, freq in frequency_map.items()]
        
        # Sort the list based on frequency in descending order
        freq_list.sort(key=lambda x: x[1], reverse=True)
        
        # Extract the top k elements
        result = [freq_list[i][0] for i in range(k)]
        
        return result
class Solution:
    def countSubarrays(self, nums: List[int], target_count: int) -> int:
        subarray_count = 0 # Variable to store the result
        max_element_count = 0 # Frequency of the maximum element encountered so far
        array_size = len(nums) # Size of the input array
        max_element = max(nums) # Maximum element in the array
        window_start = 0 # Start index of the sliding window

        # Iterate through the array
        for i in range(array_size):
            # If the current element is the maximum element encountered so far
            if nums[i] == max_element:
                max_element_count += 1 # Increment the frequency of the maximum element

                # If the frequency of the maximum element reaches the target count
                if max_element_count == target_count:
                    subarrays_with_max = array_size - i # Number of subarrays with the maximum element
                    # Move the start pointer until it encounters a different element
                    while nums[window_start] != max_element:
                        window_start += 1
                        subarray_count += subarrays_with_max # Increment the count by the number of subarrays with the maximum element
                    subarray_count += subarrays_with_max # Increment the count by the number of subarrays with the maximum element
                    window_start += 1 # Move the start pointer to the next index
                    max_element_count -= 1 # Decrease the frequency of the maximum element
        return subarray_count

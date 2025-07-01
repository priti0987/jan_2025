# # 26. Reverse an array in-place.
# myList= [1,3,1,5,89,56]
#
# print("Reverse an array in-place == ",myList[::-1])
#
# # 27. Find the largest and smallest element.
# print("27. Find the largest and smallest element.","largest == ",max(myList),"smallest == ",min(myList))
# # 28. Check for duplicates in an array
# # 29. Remove duplicates — return only unique values.
# unique = []
# duplicate = []
# for i in myList:
#     if i not in unique:
#         unique.append(i)
#     else:
#         duplicate.append(i)
# print("duplicate == ",duplicate)


# 30. Find the missing number from 1 to N.
def find_missing_number(arr, N):
    # Sum of first N natural numbers
    expected_sum = N * (N + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Example usage
N = 10
arr = [1, 2, 3, 4, 5, 6, 7, 8, 10]  # 9 is missing
missing = find_missing_number(arr, N)
print(f"The missing number is: {missing}")


# 31. Move all zeros to the end — keep order.
# 32. Rotate the array left/right by K positions.
# 33. Find the Kth largest/smallest element.
# 34. Merge two sorted arrays — without using extra space.
# 35. Find the intersection of two arrays.
# 36. Sort 0s, 1s, and 2s without using sort().
# 37. Find subarrays with a given sum.
# 38. Detect if a subarray sums to 0.
# 39. Find the longest increasing subsequence.
# 40. Kadane’s Algorithm — maximum subarray sum.
# 41. Check if array is sorted and rotated.
# 42. Rearrange array in max-min order alternately.
# 43. Find leaders in an array (no greater element to the right).
# 44. Calculate frequency of all elements in O(n).
# 45. Product of all elements except self.

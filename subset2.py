def subsetsWithDup(nums):
    def backtrack(start, path):
        result.append(path) 
        # what is the difference between result.append(path) and result.append(path[:])
        # result.append(path[:]) is a shallow copy of path
        # result.append(path) is a reference to path
        
        
        # what is this for loop doing?
        # for loop is iterating through the list of numbers
        # it is checking if the number is a duplicate
        # if it is a duplicate, it will skip it
        # if it is not a duplicate, it will add it to the path
        # it will then call the backtrack function again
        # the backtrack function will add the number to the path
        # it will then call the backtrack function again
        # the backtrack function will add the number to the path
        # it will then call the backtrack function again
        #  
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            backtrack(i + 1, path + [nums[i]])

    nums.sort()
    result = []
    backtrack(0, [])
    return result

nums = [1, 2, 2]
result = subsetsWithDup(nums)
print(result)
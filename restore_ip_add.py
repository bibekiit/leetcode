class Solution:
    def restoreIpAddresses(self, s: str):
        self.path = []
        self.result = []
        self.restoreIpAddressesHelper(s, 0)
        
        self.result = ['.'.join(x) for x in self.result]
        
        return self.result

    def restoreIpAddressesHelper(self, s, count):
        if count == 3:
            # check if the remaining string is a valid ip
            if self.isValid(s):
                self.result.append(self.path + [s])
            return
        # This condition is to check if the remaining string is too short
        # to be a valid ip
        if len(s) < 4 - count:
            return
        # This condition is to check if the remaining string is too long
        # to be a valid ip
        if len(s) > 3 * (4 - count):
            return
        # This is the main logic
        # We are trying to place a delimiter at every position
        # and then calling the helper function recursively
        for i in range(1, 4):
            if self.isValid(s[:i]):
                # Add the string to the path
                # Call the helper function recursively

                self.path.append(s[:i])
                self.restoreIpAddressesHelper(s[i:], count + 1)
                # Remove the string from the path
                self.path.pop()
                
        

        
    def isValid(self, s):
        # Check if the string is a valid ip
        if not s:
            return False
        if len(s) > 1 and s[0] == '0':
            return False
        if int(s) > 255:
            return False
        return True
    
s = Solution()
print (s.restoreIpAddresses("101023"))

            
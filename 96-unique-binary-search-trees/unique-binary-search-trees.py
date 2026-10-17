class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] will store the number of unique BSTs that can be formed with i nodes
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1  # An empty tree is 1 unique structure
        dp[1] = 1  # A tree with 1 node is 1 unique structure
        
        # Fill the DP table sequentially up to n
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                left_nodes = root - 1
                right_nodes = nodes - root
                dp[nodes] += dp[left_nodes] * dp[right_nodes]
                
        return dp[n]

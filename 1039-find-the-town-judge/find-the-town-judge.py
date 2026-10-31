class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        # Array to track net trust scores (indegree - outdegree) for each person.
        # Person labels are 1-indexed, so we use a size of n + 1.
        trust_scores = [0] * (n + 1)
        
        # Populate the trust scores based on the trust relationships
        for a, b in trust:
            trust_scores[a] -= 1  # Person 'a' trusts someone, outdegree increases
            trust_scores[b] += 1  # Person 'b' is trusted, indegree increases
            
        # The judge must have a net trust score of exactly n - 1
        for i in range(1, n + 1):
            if trust_scores[i] == n - 1:
                return i
                
        return -1

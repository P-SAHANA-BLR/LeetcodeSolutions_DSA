class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Create a sorted copy of the scores in descending order
        sorted_scores = sorted(score, reverse=True)
        
        # Dictionary to map each unique score to its rank string
        rank_map = {}
        
        for i, s in enumerate(sorted_scores):
            if i == 0:
                rank_map[s] = "Gold Medal"
            elif i == 1:
                rank_map[s] = "Silver Medal"
            elif i == 2:
                rank_map[s] = "Bronze Medal"
            else:
                rank_map[s] = str(i + 1)
                
        # Build the final answer using the original order of scores
        return [rank_map[s] for s in score]

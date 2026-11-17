class Solution:

    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        # 1. Precompute proper divisors for every length L (2 <= L <= n)
        divisors = [[] for _ in range(n + 1)]
        for length in range(2, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)

        # 2. Precompute min changes to make s[i:j] a semi-palindrome
        INF = float("inf")
        cost = [[INF] * (n + 1) for _ in range(n)]

        for i in range(n):
            for j in range(i + 2, n + 1):
                length = j - i
                best_cost = INF

                for d in divisors[length]:
                    changes = 0
                    # Check each of the d groups formed by step d
                    for offset in range(d):
                        left = i + offset
                        right = j - d + offset
                        while left < right:
                            if s[left] != s[right]:
                                changes += 1
                            left += d
                            right -= d
                    if changes < best_cost:
                        best_cost = changes

                cost[i][j] = best_cost

        # 3. DP to partition s[0:end] into p semi-palindromes
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            # Each partition needs at least length 2
            for end in range(2 * p, n + 1):
                for prev in range(2 * (p - 1), end - 1):
                    if dp[p - 1][prev] != INF:
                        dp[p][end] = min(
                            dp[p][end], dp[p - 1][prev] + cost[prev][end]
                        )

        return dp[k][n]

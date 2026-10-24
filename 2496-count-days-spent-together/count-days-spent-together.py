class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # Days in each month for a non-leap year
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Helper function to convert "MM-DD" to the absolute day of the year
        def date_to_day(date_str: str) -> int:
            month = int(date_str[:2])
            day = int(date_str[3:])
            # Sum up the days of all preceding months, then add the current day
            return sum(days_in_months[:month - 1]) + day
        
        # Convert all arrival and departure dates to absolute day numbers
        start_alice = date_to_day(arriveAlice)
        end_alice = date_to_day(leaveAlice)
        start_bob = date_to_day(arriveBob)
        end_bob = date_to_day(leaveBob)
        
        # The overlapping period starts at the latest arrival date 
        # and ends at the earliest departure date
        overlap_start = max(start_alice, start_bob)
        overlap_end = min(end_alice, end_bob)
        
        # Calculate overlapping days; return 0 if they don't overlap
        return max(0, overlap_end - overlap_start + 1)

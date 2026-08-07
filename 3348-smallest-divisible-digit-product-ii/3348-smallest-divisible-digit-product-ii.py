class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        # Step 1: Prime factorize t into 2, 3, 5, 7
        temp_t = t
        c2 = c3 = c5 = c7 = 0
        
        while temp_t % 2 == 0:
            c2 += 1
            temp_t //= 2
        while temp_t % 3 == 0:
            c3 += 1
            temp_t //= 3
        while temp_t % 5 == 0:
            c5 += 1
            temp_t //= 5
        while temp_t % 7 == 0:
            c7 += 1
            temp_t //= 7
            
        # If t has any prime factors other than 2, 3, 5, 7, impossible
        if temp_t > 1:
            return "-1"

        def get_min_digits(req_2, req_3, req_5, req_7):
            """Returns sorted list of digits needed to satisfy required prime factors efficiently."""
            digits = []
            # Satisfy 5s and 7s directly
            digits.extend([5] * req_5)
            digits.extend([7] * req_7)
            
            # Pack 3s into 9s (3^2)
            digits.extend([9] * (req_3 // 2))
            req_3 %= 2
            
            # Pack 2s into 8s (2^3)
            digits.extend([8] * (req_2 // 3))
            req_2 %= 3
            
            # Handle combinations of remaining 2s and 3s
            if req_2 == 2 and req_3 == 1:
                # 2*2*3 = 12 -> 8 and 3 (2*2*2=8, 3=3) or 6 and 2 -> best is 8, 3
                # Wait, factor 2^2 * 3^1 = 12 -> digits 2, 6 or 3, 4 -> min positions = 2
                digits.extend([2, 6])
            elif req_2 == 1 and req_3 == 1:
                digits.append(6)
            elif req_2 == 2 and req_3 == 0:
                digits.append(4)
            elif req_2 == 1 and req_3 == 0:
                digits.append(2)
            elif req_2 == 0 and req_3 == 1:
                digits.append(3)
                
            digits.sort()
            return digits

        def can_fit(req_2, req_3, req_5, req_7, available_len):
            """Checks if required factors can fit into available_len positions."""
            min_digits = get_min_digits(req_2, req_3, req_5, req_7)
            return len(min_digits) <= available_len

        def build_suffix(req_2, req_3, req_5, req_7, available_len):
            """Constructs the smallest valid suffix padded with '1's."""
            min_digits = get_min_digits(req_2, req_3, req_5, req_7)
            ones_count = available_len - len(min_digits)
            return "1" * ones_count + "".join(map(str, min_digits))

        # Helper to factorize a single digit 1-9
        def factor_digit(d):
            f2 = f3 = f5 = f7 = 0
            if d in (2, 4, 8, 6):
                f2 = {2: 1, 4: 2, 8: 3, 6: 1}[d]
            if d in (3, 9, 6):
                f3 = {3: 1, 9: 2, 6: 1}[d]
            if d == 5:
                f5 = 1
            if d == 7:
                f7 = 1
            return f2, f3, f5, f7

        n = len(num)

        # Precompute prefix factor demands
        # pref_factors[i] stores factors contributed by num[:i]
        pref_factors = [(0, 0, 0, 0)] * (n + 1)
        first_zero = -1

        for i in range(n):
            if num[i] == '0':
                first_zero = i
                break
            f2, f3, f5, f7 = factor_digit(int(num[i]))
            p2, p3, p5, p7 = pref_factors[i]
            pref_factors[i + 1] = (p2 + f2, p3 + f3, p5 + f5, p7 + f7)

        # Case 1: Check if num itself is zero-free and valid
        if first_zero == -1:
            p2, p3, p5, p7 = pref_factors[n]
            if p2 >= c2 and p3 >= c3 and p5 >= c5 and p7 >= c7:
                return num

        # Case 2: Try matching prefixes of length i from n-1 down to 0
        limit = n if first_zero == -1 else first_zero
        
        for i in range(limit, -1, -1):
            p2, p3, p5, p7 = pref_factors[i]
            
            # Remaining required factors
            rem_2 = max(0, c2 - p2)
            rem_3 = max(0, c3 - p3)
            rem_5 = max(0, c5 - p5)
            rem_7 = max(0, c7 - p7)
            
            if i < n:
                start_d = int(num[i]) + 1
                for d in range(start_d, 10):
                    f2, f3, f5, f7 = factor_digit(d)
                    r2 = max(0, rem_2 - f2)
                    r3 = max(0, rem_3 - f3)
                    r5 = max(0, rem_5 - f5)
                    r7 = max(0, rem_7 - f7)
                    
                    if can_fit(r2, r3, r5, r7, n - 1 - i):
                        suffix = build_suffix(r2, r3, r5, r7, n - 1 - i)
                        return num[:i] + str(d) + suffix

        # Case 3: Need a longer number (length n + 1 or more)
        # Search for smallest total length >= n + 1 that fits
        target_len = n + 1
        while True:
            if can_fit(c2, c3, c5, c7, target_len):
                return build_suffix(c2, c3, c5, c7, target_len)
            target_len += 1
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 1. Trivial structural boundary conditions
        if n == 0:
            return 1.0
        if x == 0.0:
            return 0.0
        
        is_negative_exponent = n < 0
        abs_n = abs(n)
        abs_x = abs(x)
    
        # 2. Compute log-space projection
        log_x = math.log(abs_x)
        target = abs_n * log_x
    
        # 3. Domain Guards: Catch IEEE 754 overflow/underflow boundaries immediately
        # ln(MAX_FLOAT) is approx 709.78
        if target > 709.78:
            if x < 0 and abs_n % 2 != 0:
                return float('-inf') if not is_negative_exponent else -0.0
            return float('inf') if not is_negative_exponent else 0.0
        
        # ln(MIN_FLOAT_SUBNORMAL) is approx -744.44
        if target < -744.44:
            return 0.0 if not is_negative_exponent else float('inf')
    
        # 4. Safe Initialization within bounded domain
        # Directly initialize at the target projection scale safely
        y = math.exp(target)
    
        # 5. Newton-Raphson Refinement Loop
        # Handles floating point accuracy drift to reach exact machine precision
        epsilon = 1e-13
        for _ in range(20):
            if y <= 0:
                y = epsilon
            
            # Standard update step: y_{k+1} = y_k * (1 - ln(y_k) + target)
            y_next = y * (1.0 - math.log(y) + target)
        
            if abs(y_next - y) < epsilon:
                y = y_next
                break
            y = y_next
        
        # 6. Apply alternating signs for negative bases on odd powers
        if x < 0 and abs_n % 2 != 0:
            y = -y
        
        return 1.0 / y if is_negative_exponent else y
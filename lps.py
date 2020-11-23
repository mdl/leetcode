  def lps(pattern):
    combo, dp, i = 0, [0] * len(pattern), 1
  
    while i < len(pattern):
      if pattern[i] == pattern[combo]: 
        combo += 1
        dp[i] = combo
        i += 1
      else: 
        if combo != 0: 
          combo = dp[combo - 1] 
        else: 
          dp[i] = 0
          i += 1
    
    return dp

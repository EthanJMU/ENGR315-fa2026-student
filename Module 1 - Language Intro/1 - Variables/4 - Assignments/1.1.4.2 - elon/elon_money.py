"""
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 10-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $33B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
Note that Elon's capital will be $33B.
"""

#for a 10 year bond, they pay 3.96% This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
#interest that compounds annually while a 20 year bond pays 4.32% interest that also compounds annually. 
#the formula needed for this problem is the compound interest formula: A = P(1+r/n)^(nt)
#A = final amount
# P =principal amount (initial investment)
# r = annual interest rate (decimal)
# n = number of times interest is compounded per year
# t = number of years the money is invested for

ten_year_final = 33_000_000_000 * (1 + 0.0396/1)**(1*10) 
twenty_year_final = 33_000_000_000 * (1 + 0.0432/1)**(1*20)

print("ten_year =", ten_year_final)
print("twenty_year =", twenty_year_final)
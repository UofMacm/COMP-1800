# Computes the following loan payback schedule:
#  Day 1 - $0.01
#  Day 2 - $0.02
#  Day 3 - $0.04
#  Day 4 - $0.08
#  ... etc., all the way to 30 days

total = 0           # total paid back so far
owedToday = 0.01    # amount paid back today

d = 1
while d <= 30:
    total = total + owedToday
    print("On day " + str(d) + ", you owe: $" + str(owedToday))
    print("  (total so far = $" + str(total) + ")")
    owedToday = 2*owedToday
    d = d + 1

import numpy as np
print(np.random.rand())

np.random.seed(142) #starts from seed
print(np.random.rand())
#if you generate from the same seed it generates the same number
#it esnures reproducibility

########################
#sample dice game
# NumPy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice =  np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <= 5 :
    step =  step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)


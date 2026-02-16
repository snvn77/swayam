# Consider the following Python function.
def mystery(l,v):
  if len(l) == 0:
    return (v)
  else:
    return (mystery(l[:-1],l[-1]+v))
# What does mystery([22,14,19,65,82,55],1) return?  (258)

# What is the value of triples after the following assignment?
triples = [ (x,y,z) for x in range(2,4) for y in range(2,5) for z in range(5,7) if 2*x*y > 3*z ]      # [(2,4,5), (3,3,5), (3,4,5), (3,4,6)]

# Consider the following dictionary.
runs = {"Test":{"Rahul":[90,14,35],"Kohli":[3,103,73,42],"Pujara":[53,15,133,8]},"ODI":{"Sharma":[37,99],"Kohli":[63,47]}}
# Which of the following statements does not generate an error?
#  runs["ODI"]["Rahul"].append([74])
#  runs["ODI"]["Rahul"].extend([74])
#  runs["ODI"]["Rahul"][0]=74
#  runs["ODI"]["Rahul"]=[74]         # (Right Answer)

# Assume that inventory has been initialized as an empty dictionary:
inventory = {}
# Which of the following generates an error?
#  inventory["Amul"] = ["Mystic Mocha",55]
#  inventory["Amul, Mystic Mocha"] = 55     
#  inventory[["Amul","Mystic Mocha"]] = 55      # (Right Answer)
#  inventory[("Amul","Mystic Mocha")] = 55
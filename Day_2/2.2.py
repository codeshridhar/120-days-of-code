"""Assignment 1: The Type Detective 🔍
Take 5 different values of your choice (mix of str, int, float, bool). Print each value AND its type using type(). Then convert each one to a string and print the new type.

Goal: Prove you understand all 4 types and that str() can convert anything.

"""
val1 = "name"
val2 = 10
val3 = 10.32
val4 = True

print(f"name is of {type(val1)} type")
print(f"10 is of {type(val2)} type")
print(f"10.32 is of {type(val3)} type")
print(f"True is of {type(val4)} type")

nval1 = "name"
nval2 = float(10)
nval3 = int(10.32)
nval4 = str(True)
nval5 = str(10)

print(f"name is of {type(nval1)} type which is now {nval1}")
print(f"10 is of {type(nval2)} type which is now {nval2}")
print(f"10.32 is of {type(nval3)} which is now {nval2} type")
print(f"True is of {type(nval4)} which is now {nval2} type")
print(f"10 is of {type(nval5)} which is now {nval5} type")

print(f"previous {val1} later {nval1} from {type(val1)} to {type(nval1)}")
print(f"previous {val2} later {nval2} from {type(val2)} to {type(nval2)}")
print(f"previous {val3} later {nval3} from {type(val3)} to {type(nval3)}")
print(f"previous {val4} later {nval4} from {type(val4)} to {type(nval4)}")
print(f"previous {val1} later {nval5} from {type(val1)} to {type(nval5)}")



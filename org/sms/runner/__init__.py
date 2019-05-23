
"""l=[1,2,3,4,5,6,7,8]

for index, values in enumerate(l):
    print("[{}]|{}".format(index,values))
"""
def favorite_colors(**a):
    for key, value in a.items():
        print(f"{key}'s favorite color is {value}")

favorite_colors(rusty='green', colt='blue',name="Dheeraj",age=29)

# rusty's favorite color is green
# colt's favorite color is blue

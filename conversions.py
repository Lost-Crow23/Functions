# Defining a function within the converter and use the conversion number
def cm_converter(num) -> int:
    return num * 0.01
#
print("cm = ")
num = int(input())
# enter the value of cm then should convert to metres
print(f"converting {num}cm into {cm_converter(num)} meters: ")

# Define a function feet converter and the conversion number
def feet_converter(num) ->int:
    return num * 3.281

print("in meters: ")
num = int(input())
# enter the value of metres then convert to feet
print(f"converting {num}m into {feet_converter(num)} feet")
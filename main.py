from rotator import rotate
from compressor import compress

print("----------------------- Editor program starting -----------------------\n")
filename = input("     What file would you like to edit? (.png, .jpg, etc) ")
request = input("\n     What would you like to do? (R: rotate clockwise, C: compress, Other: quit) ")
while request in ["R", "C"]:
    match (request):
        case "R":
            rotate(filename, int(input("\n     How many times would you like to rotate the image? ")))
        case "C":
            compress(filename, int(input("\n     How much would you like to compress the image by? ")))
    request = input("\n     What would you like to do? (R: rotate clockwise, C: compress, Other: quit) ")
print("\n------------------------- Exiting editor -------------------------")
# Adapted from htts://tour.golang.org/flowcontrol/8


def sqrt(x):
  # Initial guess
  z = 1.0

  #Keep getting better approximate for the square root of x until you are within two decimal places
  while abs(z*z - x) >= 0.00000001:
    print("1 in loop z ", z)
    # Get a better approximation for the square root
    z=z-((z*z)-x) / (2*z)
    #This is based on Newtons Method for the approximation of a square root
    print("2 in loop z ", z)

  return z


y = (sqrt(20.0))

print(y)

print(y*y)
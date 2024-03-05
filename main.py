nric = input('Enter an NRIC number: ')

# Type your code below
nric = nric.upper()
check = 0
checknum = 0
check_char = "a"
if nric[0] in ["S", "T", "F", "G"]:

  if nric[1:-1].isdigit():

    if len(nric[8:]) == 1 and nric[-1].isalpha():

      check = 1
      checknum += (int(nric[1]) * 2)
      checknum += (int(nric[2]) * 7)
      checknum += (int(nric[3]) * 6)
      checknum += (int(nric[4]) * 5)
      checknum += (int(nric[5]) * 4)
      checknum += (int(nric[6]) * 3)
      checknum += (int(nric[7]) * 2)

      if nric[0] in ["T", "G"]:
        checknum += 4
      remainder = checknum % 11
      if nric[0] in ["S", "T"]:
        char_table = "J  Z  I  H  G  F  E  D  C  B  A".split("  ")
        check_char = char_table[remainder]
      elif nric[0] in ["F", "G"]:
        char_table = "X  W  U  T  R  Q  P  N  M  L  K".split("  ")
        check_char = char_table[remainder]
      if nric[-1] == check_char:
        check = 1
      else:
        check = 0
else:
  check += 0

if check == 1:
  print("NRIC is valid.")
elif check == 0:
  print("NRIC is invalid.")

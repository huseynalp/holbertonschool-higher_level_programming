#!/usr/bin/python3
if __name__ == "__main__":
  count = len(argv) - 1

  if cpunt == 0:
    print("0 arguments.")
  else:
    if count == 1:
      print("1 argument:")
    else:
      print("{} arguments:".format(count))
    for i in range(1,len(argv)):
     print("{}: {}".format(i, argv[i]))

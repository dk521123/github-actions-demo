import sys

def main(args):
  print(f"Hello, world, [{args[0]}, {args[1]}]")
  return 123

if __name__ == "__main__":
    args = sys.argv
    result = main(args)

    # return value
    sys.stdout.write("This is a just test")

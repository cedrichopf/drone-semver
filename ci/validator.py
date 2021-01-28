import sys

def main():
  if len(sys.argv) < 2:
    sys.exit("Too few arguments, please provide a valid semantic version")
  version = sys.argv[1]
  semver_file = open("semver", "r", newline="\n")
  semver = semver_file.read()
  semver_file.close()
  if semver != version:
    sys.exit("Given semantic version " + version + " is not matching generated version " + semver)
  else:
    print("Validation successful. Semantic version: " + version)

main()

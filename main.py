import os, re

def main():
  semver_info = get_semver()
  if semver_info["initial_version"]:
    print("Semantic version not found, using initial version " + semver_info["semver"])
  else:
    print("Using semantic version " + semver_info["semver"])
  semver = split_semver(semver_info["semver"])
  initial_version = semver_info["initial_version"]
  increment = (os.getenv('PLUGIN_AUTOINCREMENT', 'false') == 'true')
  if increment and not initial_version:
    print("Running auto-increment")
    auto_increment(semver)
    print("Updated semantic version to " + semver_string(semver))
  save(semver)

def get_semver():
  semver = os.getenv("DRONE_SEMVER")
  if semver:
    return {
      "semver": semver,
      "initial_version": False
    }
  else:
    initial_version = os.getenv("INITIAL_VERSION") if os.getenv("INITIAL_VERSION") else "1.0.0"
    return {
      "semver": initial_version,
      "initial_version": True
    }

def split_semver(semver):
  iter = map(int, semver.split("."))
  version_list = list(iter)
  return {
    "major": version_list[0],
    "minor": version_list[1],
    "patch": version_list[2]
  }

def auto_increment(semver):
  level = increment_level()
  if level == "major":
    print("Found major changes, updating major version...")
    semver["major"] += 1
    semver["minor"] = 0
    semver["patch"] = 0
  elif level == "minor":
    print("Found minor changes, updating minor version...")
    semver["minor"] += 1
    semver["patch"] = 0
  else:
    print("No major or minor changes found, updating patch version...")
    semver["patch"] += 1

def increment_level():
  major_env = os.getenv("PLUGIN_MAJOR_KEYWORD")
  minor_env = os.getenv("PLUGIN_MINOR_KEYWORD")
  file_path = os.getenv("PLUGIN_FILE")
  expression_string = os.getenv("PLUGIN_FILE_REGEX")

  major_keyword = major_env if major_env else "Major"
  minor_keyword = minor_env if minor_env else "Minor"

  changelog = open(file_path, "r") if file_path else open("CHANGELOG.md", "r")
  content = changelog.read()
  changelog.close()
  expression = repr(expression_string) if expression_string else r"\[(\d\.){2}\d\]"
  section = re.split(expression, content)[0]
  if major_keyword in section:
    return "major"
  elif minor_keyword in section:
    return "minor"
  else:
    return "patch"
  return

def semver_string(semver):
  return str(semver["major"]) + "." + str(semver["minor"]) + "." + str(semver["patch"])

def save(semver):
  output = open("semver", "w")
  output.write(semver_string(semver))
  output.close()
  print("Saved new semantic version to semver file")

main()

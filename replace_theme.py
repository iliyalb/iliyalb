import re

def switch_theme(file_path):
  with open(file_path, "r") as f:
    file_contents = f.read()

  # Get the current theme.
  current_theme = re.search(r"theme=([^ ]+)", file_contents).group(1)

  # Switch the theme.
  if current_theme == "transparent":
    new_theme = "dark"
  else:
    new_theme = "transparent"

  # Replace the old theme with the new theme.
  file_contents = re.sub(r"theme=" + current_theme, "theme=" + new_theme, file_contents)

  # Write the updated file contents back to the file.
  with open(file_path, "w") as f:
    f.write(file_contents)

if __name__ == "__main__":
  # Get the path to the README.md file.
  readme_file_path = "README.md"

  # Switch the theme.
  switch_theme(readme_file_path)

  # Print a success message.
  print("The theme in the README.md file has been switched.")

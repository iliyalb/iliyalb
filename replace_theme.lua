function switch_theme(file_path)
    -- Read file contents
    local file = io.open(file_path, "r")
    local file_contents = file:read("*all")
    file:close()

    -- Get current theme using Lua pattern matching
    local current_theme = string.match(file_contents, "theme=([^ ]+)")

    -- Switch the theme
    local new_theme = current_theme == "transparent" and "dark" or "transparent"

    -- Replace old theme with new theme
    file_contents = string.gsub(file_contents, "theme=" .. current_theme, "theme=" .. new_theme)

    -- Write updated contents back to file
    file = io.open(file_path, "w")
    file:write(file_contents)
    file:close()
end

-- Main program
local readme_file_path = "README.md"
switch_theme(readme_file_path)
print("The theme in the README.md file has been switched.")

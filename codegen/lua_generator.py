from pathlib import Path

def generate_lua(concept):
    Path("build").mkdir(exist_ok=True)

    lua_code = f"""
-- {concept['title']}
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
    print("Welcome to {concept['title']}!")
end)
"""

    file_path = "build/main.lua"
    with open(file_path, "w") as f:
        f.write(lua_code)

    return [file_path]

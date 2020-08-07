import re
import os 
import random

# Path to the settings file of windows terminal
settings_file = "C:\\Users\\jackh\\AppData\\Local\\Packages\\Microsoft.WindowsTerminal_8wekyb3d8bbwe\\LocalState\\settings.json"
new_settings_data = ""

with open(settings_file, "r") as f:
    contents = f.read()
    f.close()
current_backgrounds = re.findall('(?:"backgroundImage") : "(.*)"', contents)
print(current_backgrounds)

# Path to a folder containg the pictures that you want rotated 
path_to_pics = "C:\\Users\\jackh\\Pictures\\terminalBackgrounds\\"

pics = (os.listdir(path_to_pics))

pictures = []
for pic in pics:
    pic = str(path_to_pics) + str(pic)
    pic = pic.replace("\\", "\\\\")
    pictures.append(pic)


new_settings_data = contents
random_choices = set()
while len(random_choices) != len(current_backgrounds):
    random_choice = (random.choice(pictures))
    if random_choice not in current_backgrounds:    
        random_choices.add(random_choice)


for old_background,new_background in zip(current_backgrounds,random_choices):
    new_settings_data = new_settings_data.replace(old_background, new_background)
    print(str(random_choices))
    with open(settings_file, "w") as f:
        f.write(new_settings_data)
        f.close()

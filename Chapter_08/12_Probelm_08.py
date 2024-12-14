def display_info(**Kawrgs):
    output = ""
    for key, value in Kawrgs.items():
        output += f"{key}:  {value}\n"

    return output.strip()  #strip remove extra white space to make text more clear.


print(display_info(name="wahab", language="python", gender="male"))
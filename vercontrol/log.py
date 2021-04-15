def log_it (a):
    with open('logver.txt', "r+") as f:
        lines = f.readlines()
        global vernumbstring
        vernumbstring = lines[0]
        vernumbstring = vernumbstring.strip()
        vernumber = int(vernumbstring)
        vernumber += 1
        lines[0] = str(vernumber) + "\n"
        f.seek(0)
        f.writelines(lines)
        f.write(vernumbstring + " " + a + "\n")
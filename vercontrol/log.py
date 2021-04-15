from datetime import datetime
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

        now=datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        f.writelines(lines)
        f.write(vernumbstring + " " + a + "\t\t\t" + dt_string + "\n")
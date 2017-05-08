import datetime
import os

# This file generate the daily fit log of one member of ec-league
USER_NAME = ""


def get_file_name():
    global USER_NAME
    name = raw_input("Please select your name? 1: EthanPark, 2: CoralineLee\n")

    log_name = ""
    prefix = datetime.datetime.now().weekday() + 1

    if name == "1" or name == "EthanPark":
        USER_NAME = "EthanPark"
        log_name = str(prefix) + "-EthanPark.log"
    elif name == "2" or name == "CoralineLee":
        USER_NAME = "CoralineLee"
        log_name = str(prefix) + "-CoralineLee.log"

    return log_name


def get_fit_minutes():
    minutes = raw_input("Please input your fit minutes?\n")

    if minutes == "":
        return 0

    if not minutes.isdigit():
        return -1

    return int(minutes)


def is_water_enough():
    flag = raw_input("Please check if you drink enough water? T or F\n")

    if flag == "y" or flag == "Y" or flag == "T" or flag == "t" or flag == "yes":
        return True
    else:
        return False


def main():
    file_name = get_file_name()

    if file_name == "":
        print "Name Invalid"
        return

    directory = get_dir()

    if not os.path.exists(directory):
        os.makedirs(directory)

    fit_minutes = get_fit_minutes()
    score = fit_minutes

    if fit_minutes == -1:
        print "Fit time Invalid"
        return

    if fit_minutes == 0:
        score = -20

    f = open("%s/%s" % (directory, file_name), "w+")

    line = "Hi," + USER_NAME
    line += "\n"
    line += "Today you workout for : "
    line += str(fit_minutes)
    line += " minutes!"
    line += "\n"
    flag = is_water_enough()

    if flag:
        line += "You have drunk enough water!"
        line += "\n"
        line += "Congratulations!"
        line += "\n"
    else:
        line += "You didn't drink enough water!"
        line += "\n"
        line += "Come on! You can do better than this!"
        line += "\n"
        score -= 20

    line += "Your total score is : %d" % score
    line += "\n"
    line += "Keep trying!"
    line += "\n"

    f.write(line)

    f.close()


def get_dir():
    now = datetime.datetime.now()
    start = now - datetime.timedelta(days=now.weekday())
    end = start + datetime.timedelta(days=6)
    dir_name = "fit-log/" + start.strftime("%Y-%m-%d") + "--" + end.strftime("%Y-%m-%d")
    return dir_name


if __name__ == '__main__':
    main()

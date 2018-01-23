import pyautogui as pg
import time
import webbrowser

points = 0

# Question
answer = pg.prompt(
"""
Which would you rather do?

a) Eat beets and watch battlestar galactica
b) Eat as many M&Ms as humanly possible
c) Finish producing Threat Level Midnight


"""
    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3





# Question
answer = pg.prompt(
"""
What is your greatest achievement?

a) Earning my green belt from sensei
b) Playing in my band
c) Founding the Dundee awards


"""
    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3


# Question
answer = pg.prompt(
"""
What is your role?

a) Salesman of the year
b) Accounting... I think...
c) Boss, but most importantly friend


"""
    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

# Question
answer = pg.prompt(
"""
Who is your arch nemesis?

a) Jim
b) Math
c) Tobey, GAAAAH


"""
    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3




# END OF SURVEY

pg.alert("You are...")

# Dwight
if points < 7:
    pg.alert("Dwight K Schrute")
    webbrowser.open("https://vignette.wikia.nocookie.net/theoffice/images/c/c5/Dwight_.jpg/revision/latest/scale-to-width-down/350?cb=20170701082424")
# Kevin
if points >=7 and points < 10:
    pg.alert("Kevin Mallone")
# Michael
if points >= 10:
    pg.alert("Michael Scott")

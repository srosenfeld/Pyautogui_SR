import pyautogui as pg
import time

pg.hotkey('command','space')
pg.typewrite('chrome\n',0.3)

schoollist = ["American School in Japan","American School in London","Beauvoir: The National Cathedral Elementary School","Berkshire School","The Bishop's School","Blair Academy","Blind Brook School District","Brookwood School","Brunswick School","Buffalo Seminary ","Canterbury School","Chico Country Day School","Columbia University of New York","Convent of the Sacred Heart","Emma Willard School","Fairfield Country Day School","Forman School","Friends Academy","Germantown Academy","Glenholme School","Greenwich Academy","Greenwich Country Day School","Greenwich Public Schools","Gunnery School","Head-Royce School","Headwaters School","Hill School","Hotchkiss School","Indian Mountain School","Kent Place School","King School","Latin School of Chicago","Lawrence Academy ","Mercersburg Academy","Miss Hall's School ","Monte Vista Christian School","Moravian Academy","New Canaan Country School","Newark Academy","Orchard School","Pine Point School ","Pomfret School","Riverdale Country School","Stanwich School","San Francisco University High School","St. John's Episcopal Preschool","St. Luke’s School","St. Thomas Church, Whitemarsh","Seminole High School","Unquowa School","Wheeler School","William's School","Williston Northampton School","Virginia Episcopal School","Worcester Academy"]
keyword = "deep learning"

for i in schoollist:
    #If Windows, change 'command' to 'ctrl' in line below
    pg.hotkey('command','t')
    pg.typewrite(i + " " + keyword + "\n",0.1)
    time.sleep(0.3)

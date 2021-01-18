import requests
from bs4 import BeautifulSoup
import time
from discord_webhook import DiscordWebhook

class UND:
    def __init__(self):
        global url
        with open("discordurl.txt", "r") as f:
            url = f.read()

    def getFlightCategory(self):    # Takes the appropriate html text and sets it to a variable
        flightCategoryClass = self.soup.find(class_="auto-style1b")
        return flightCategoryClass.get_text()

    def getRestrictions(self):  # Takes the appropriate html text and sets it to a variable
        flightRestrictionsClass = self.soup.find(class_="auto-style4")
        flightRestrictionsClass2 = self.soup.find(class_="auto-style5")
        return flightRestrictionsClass.get_text(), flightRestrictionsClass2.get_text()

    def scrape(self):
        page = requests.get("http://sof.aero.und.edu")
        self.soup = BeautifulSoup(page.content, "html.parser")

    def getInfo(self):
        return self.getFlightCategory(), self.getRestrictions()

    def discordBot(self):
        FC1 = 0
        FR1 = 0
        FR2 = 0
        now = time.gmtime()
        while 1 == 1:
            if 1 == 1:  # now[6] <= 5 and 14 <= now[3] <= 23:   # if the day of the week is not sunday, and its between 23 - 14 Zulu (GMT)      8am to 5 CST
                und.scrape()
                flightCategory = und.getFlightCategory()
                flightRestrictions1, flightRestrictions2 = und.getRestrictions()
                if flightCategory == FC1 and flightRestrictions1 == FR1 and flightRestrictions2 == FR2:
                    time1 = (now[3] - 8)
                    print("No Change", time1)  # print time it checked for debugging
                    time.sleep(300)
                elif flightCategory != FC1 or flightRestrictions1 != FR1 or flightRestrictions2 != FR2:
                    FC1 = flightCategory
                    FR1 = flightRestrictions1
                    FR2 = flightRestrictions2
                    if flightRestrictions1 == "Manager on Duty:":
                        DiscordWebhook(url=url, content=('<@&796776150578757662> %s' % flightCategory)).execute()
                        print("Posted, Closed")
                        time.sleep(300)
                    elif flightRestrictions2 == "Manager on Duty:":
                        DiscordWebhook(url=url, content=(
                                    '<@&796776150578757662> %s, %s' % (flightCategory, flightRestrictions1))).execute()
                        time.sleep(300)
                        print("Posted")
                    elif flightRestrictions2 != "Manager on Duty:":
                        DiscordWebhook(url=url, content=('<@&796776150578757662> %s, %s, %s' % (
                        flightCategory, flightRestrictions1, flightRestrictions2))).execute()
                        print("Posted")
                        time.sleep(300)
            else:
                print("Outside Time")
                time.sleep(300)
und = UND()
und.discordBot()

# tm_year=2020, tm_mon=12, tm_mday=31, tm_hour=0, tm_min=37,
# tm_sec=55, tm_wday=3, tm_yday=366, tm_isdst=0)

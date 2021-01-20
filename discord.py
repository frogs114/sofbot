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
        flightRestrictionsClass3 = self.soup.find(class_="auto-style6")
        flightRestrictionsClass4 = self.soup.find(class_="auto-style7")
        flightRestrictionsClass5 = self.soup.find(class_="auto-style8")
        return flightRestrictionsClass.get_text(), flightRestrictionsClass2.get_text(), flightRestrictionsClass3.get_text(), flightRestrictionsClass4.get_text(), flightRestrictionsClass5.get_text()

    def scrape(self):
        page = requests.get("http://sof.aero.und.edu")
        self.soup = BeautifulSoup(page.content, "html.parser")

    def discordBot(self):
        FC1 = 0
        FR1 = 0
        FR2 = 0
        FR3 = 0
        FR4 = 0
        FR5 = 0
        now = time.gmtime()
        while 1 == 1:
            if now[6] <= 5 and (now[3] >= 12 or now[3] <= 3):   # if the day of the week is not sunday, and its between 23 - 14 Zulu (GMT)      8am to 5 CST
                und.scrape()
                flightCategory = und.getFlightCategory()
                flightRestrictions1, flightRestrictions2, flightRestrictions3, flightRestrictions4, flightRestrictions5 = und.getRestrictions()
                if flightCategory == FC1 and flightRestrictions1 == FR1 and flightRestrictions2 == FR2 and flightRestrictions3 == FR3 and flightRestrictions3 == FR4 and flightRestrictions3 == FR5:
                    time1 = (now[3] - 6)
                    print("No Change", time1)  # print time it checked for debugging
                    time.sleep(300)
                else:
                    FC1 = flightCategory
                    FR1 = flightRestrictions1
                    FR2 = flightRestrictions2
                    FR3 = flightRestrictions3
                    FR4 = flightRestrictions4
                    FR5 = flightRestrictions5
                    if flightRestrictions1 == "Manager on Duty:":
                        DiscordWebhook(url=url, content=('<@&796776150578757662> %s' % flightCategory)).execute()
                        print("Posted, Closed")
                        time.sleep(300)
                    elif flightRestrictions2 == "Manager on Duty:":
                        DiscordWebhook(url=url, content=('<@&796776150578757662> %s, %s' % (flightCategory, flightRestrictions1))).execute()
                        time.sleep(300)
                        print("Posted")
                    elif flightRestrictions3 == "Manager on Duty:":
                        DiscordWebhook(url=url, content=('<@&796776150578757662> %s, %s, %s' % (flightCategory, flightRestrictions1, flightRestrictions2))).execute()
                        print("Posted")
                        time.sleep(300)
                    elif flightRestrictions4 == "Manager on Duty:":
                        DiscordWebhook(url=url, content=('<@&796776150578757662> %s, %s, %s, %s' % (flightCategory, flightRestrictions1, flightRestrictions2, flightRestrictions3))).execute()
                        print("Posted")
                        time.sleep(300)
                    elif flightRestrictions5 == "Manager on Duty:":
                        DiscordWebhook(url=url, content=('<@&796776150578757662> %s, %s, %s, %s, %s' % (flightCategory, flightRestrictions1, flightRestrictions2, flightRestrictions3, flightRestrictions4))).execute()
                        print("Posted")
                        time.sleep(300)
                    elif flightRestrictions3 != "Manager on Duty:":
                        DiscordWebhook(url=url, content=('<@&796776150578757662> %s, %s, %s, %s, %s, %s' % (flightCategory, flightRestrictions1, flightRestrictions2, flightRestrictions3, flightRestrictions4, flightRestrictions5))).execute()
                        print("Posted")
                        time.sleep(300)
            else:
                print("Outside Time")
                time.sleep(300)


und = UND()
und.discordBot()


# time.struct_time(tm_year=2021, tm_mon=1, tm_mday=19, tm_hour=1, tm_min=15, tm_sec=14, tm_wday=1, tm_yday=19, tm_isdst=0)

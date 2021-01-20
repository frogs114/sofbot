import requests
from bs4 import BeautifulSoup
import time
from discord_webhook import DiscordWebhook


class UND:
    def __init__(self):
        global url
        with open("discordurl.txt", "r") as f:
            url = f.read()

    def getFlightCategory(self):  # Takes the appropriate html text and sets it to a variable
        flightCategoryClass = self.soup.find(class_="auto-style1b")
        return flightCategoryClass.get_text()

    def getRestrictions(self):  # Takes the appropriate html text and sets it to a list if text is found
        restrictionslist = []
        try:
            flightRestrictionsClass1 = self.soup.find(class_="auto-style4")  # find text
            restrictionslist.append(flightRestrictionsClass1.get_text())  # add to list
        except AttributeError:  # if no text is found, pass to the next
            pass
        try:
            flightRestrictionsClass2 = self.soup.find(class_="auto-style5")
            restrictionslist.append(flightRestrictionsClass2.get_text())
        except AttributeError:
            pass
        try:
            flightRestrictionsClass3 = self.soup.find(class_="auto-style6")
            restrictionslist.append(flightRestrictionsClass3.get_text())
        except AttributeError:
            pass
        try:
            flightRestrictionsClass4 = self.soup.find(class_="auto-style7")
            restrictionslist.append(flightRestrictionsClass4.get_text())
        except AttributeError:
            pass
        try:
            flightRestrictionsClass5 = self.soup.find(class_="auto-style8")
            restrictionslist.append(flightRestrictionsClass5.get_text())
        except AttributeError:
            pass
        return restrictionslist

    def scrape(self):  # sets up webpage desired
        page = requests.get("http://sof.aero.und.edu")
        self.soup = BeautifulSoup(page.content, "html.parser")

    def discordBot(self):
        FC1 = 0  # memory variables
        FR1 = 0
        FR2 = 0
        FR3 = 0
        FR4 = 0
        FR5 = 0
        now = time.gmtime()  # time variable for code execution
        while 1 == 1:
            if now[6] <= 5 and (now[3] >= 12 or now[3] <= 3):  # if the day of the week is not sunday, and its between 23 - 14 Zulu (GMT) 8am to 5 CST
                und.scrape()  # gets info from page
                flightCategory = und.getFlightCategory()  # sets html text to variables
                restrictionslist2 = und.getRestrictions()
                if flightCategory == FC1 and restrictionslist2[0] == FR1 and restrictionslist2[1] == FR2 and restrictionslist2[2] == FR3 and restrictionslist2[3] == FR4 and restrictionslist2[4] == FR5:
                    time1 = (now[3] - 6)
                    print("No Change", time1)  # print time it checked for debugging
                    time.sleep(300)
                else:   # set memory variables
                    FC1 = flightCategory

                    try:    # try to set variables equal
                        FR1 = restrictionslist2[0]
                    except IndexError:  # if index error try to set individually
                        try:
                            FR1 = 0
                            restrictionslist2[0] = 0
                        except IndexError: # if index error again it dosent exist, so pass
                            pass

                    try:
                        FR2 = restrictionslist2[1]
                    except IndexError:
                        try:
                            FR2 = 0
                            restrictionslist2[1] = 0
                        except IndexError:
                            pass

                    try:
                        FR3 = restrictionslist2[2]
                    except IndexError:
                        try:
                            FR3 = 0
                            restrictionslist2[2] = 0
                        except IndexError:
                            pass

                    try:
                        FR4 = restrictionslist2[3]
                    except IndexError:
                        try:
                            FR4 = 0
                            restrictionslist2[3] = 0
                        except IndexError:
                            pass

                    try:
                        FR5 = restrictionslist2[4]
                    except IndexError:
                        try:
                            FR5 = 0
                            restrictionslist2[4] = 0
                        except IndexError:
                            pass

                    if restrictionslist2[0] == "Manager on Duty:":
                        DiscordWebhook(url=url, content=('<@&796776150578757662> %s' % flightCategory)).execute()
                        print("Posted, Closed")
                        time.sleep(300)
                    elif restrictionslist2[1] == "Manager on Duty:":
                        DiscordWebhook(url=url, content=(
                                '<@&796776150578757662> %s, %s' % (flightCategory, restrictionslist2[0]))).execute()
                        time.sleep(300)
                        print("Posted")
                    elif restrictionslist2[2] == "Manager on Duty:":
                        DiscordWebhook(url=url, content=('<@&796776150578757662> %s, %s, %s' % (
                            flightCategory, restrictionslist2[0], restrictionslist2[1]))).execute()
                        print("Posted")
                        time.sleep(300)
                    elif restrictionslist2[3] == "Manager on Duty:":
                        DiscordWebhook(url=url, content=('<@&796776150578757662> %s, %s, %s, %s' % (
                            flightCategory, restrictionslist2[0], restrictionslist2[1],
                            restrictionslist2[2]))).execute()
                        print("Posted")
                        time.sleep(300)
                    elif restrictionslist2[4] == "Manager on Duty:":
                        DiscordWebhook(url=url, content=('<@&796776150578757662> %s, %s, %s, %s, %s' % (
                            flightCategory, restrictionslist2[0], restrictionslist2[1], restrictionslist2[2],
                            restrictionslist2[3]))).execute()
                        print("Posted")
                        time.sleep(300)
                    elif restrictionslist2[2] != "Manager on Duty:":
                        DiscordWebhook(url=url, content=('<@&796776150578757662> %s, %s, %s, %s, %s, %s' % (
                            flightCategory, restrictionslist2[0], restrictionslist2[1], restrictionslist2[2],
                            restrictionslist2[3], restrictionslist2[4]))).execute()
                        print("Posted")
                        time.sleep(300)
            else:
                print("Outside Time")
                time.sleep(300)


und = UND()
und.discordBot()

# time.struct_time(tm_year=2021, tm_mon=1, tm_mday=19, tm_hour=1, tm_min=15, tm_sec=14, tm_wday=1, tm_yday=19, tm_isdst=0)

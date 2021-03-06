import slack
import requests
from bs4 import BeautifulSoup
import time


class UND:
    def __init__(self):
        global client
        with open("slacktoken.txt", "r") as f:
            token = f.read()
        client = slack.WebClient(token=token)

    def getFlightCategory(self):    # Takes the appropriate html text and sets it to a variable
        flightCategoryClass = self.soup.find(class_="auto-style1b")
        return flightCategoryClass.get_text()

    def getRestrictions(self):  # Takes the appropriate html text and sets it to a variable
        flightRestrictionsClass1 = self.soup.find(class_="auto-style4")
        flightRestrictionsClass2 = self.soup.find(class_="auto-style5")
        flightRestrictionsClass3 = self.soup.find(class_="auto-style6")
        flightRestrictionsClass4 = self.soup.find(class_="auto-style7")
        flightRestrictionsClass5 = self.soup.find(class_="auto-style8")
        return flightRestrictionsClass1.get_text(), flightRestrictionsClass2.get_text(), flightRestrictionsClass3.get_text(), flightRestrictionsClass4.get_text(), flightRestrictionsClass5.get_text()

    def scrape(self):
        page = requests.get("http://sof.aero.und.edu")
        self.soup = BeautifulSoup(page.content, "html.parser")

    def slackBot(self):
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
                if flightCategory == FC1 and flightRestrictions1 == FR1 and flightRestrictions2 == FR2 and flightRestrictions3 == FR3 and flightRestrictions4 == FR4 and flightRestrictions5 == FR5:
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
                        client.chat_postMessage(channel="#sof", text=("<!channel> %s" % flightCategory))
                        print("Posted, Closed")
                        time.sleep(300)
                    elif flightRestrictions2 == "Manager on Duty:":
                        client.chat_postMessage(channel="#sof", text=("<!channel> %s, %s" % (flightCategory, flightRestrictions1)))
                        time.sleep(300)
                        print("Posted")
                    elif flightRestrictions3 == "Manager on Duty:":
                        client.chat_postMessage(channel="#sof", text=("<!channel> %s, %s, %s " % (flightCategory, flightRestrictions1, flightRestrictions2)))
                        print("Posted")
                        time.sleep(300)
                    elif flightRestrictions4 == "Manager on Duty:":
                        client.chat_postMessage(channel="#sof", text=("<!channel> %s, %s, %s, %s" % (flightCategory, flightRestrictions1, flightRestrictions2, flightRestrictions3)))
                        print("Posted")
                        time.sleep(300)
                    elif flightRestrictions5 == "Manager on Duty:":
                        client.chat_postMessage(channel="#sof", text=("<!channel> %s, %s, %s, %s, %s" % (flightCategory, flightRestrictions1, flightRestrictions2, flightRestrictions3, flightRestrictions4)))
                        print("Posted")
                        time.sleep(300)
                    elif flightRestrictions5 != "Manager on Duty:":
                        client.chat_postMessage(channel="#sof", text=("<!channel> %s, %s, %s, %s, %s, %s" % (flightCategory, flightRestrictions1, flightRestrictions2, flightRestrictions3, flightRestrictions4, flightRestrictions5)))
                        print("Posted")
                        time.sleep(300)
            else:
                print("Outside Time")
                time.sleep(300)


# time.struct_time(tm_year=2021, tm_mon=1, tm_mday=19, tm_hour=1, tm_min=15, tm_sec=14, tm_wday=1, tm_yday=19, tm_isdst=0)

und = UND()
#   und.slackBot()

























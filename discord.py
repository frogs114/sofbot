import requests
from bs4 import BeautifulSoup
import time
from discord_webhook import DiscordWebhook


class UND:
    def __init__(self):  # location of auth code for posting to discord
        global url
        with open("discordurl.txt", "r") as f:
            url = f.read()

    def getFlightCategory(self):  # Takes the appropriate html text and sets it to a variable
        flightCategoryClass = self.soup.find(class_="auto-style1b")
        return flightCategoryClass.get_text()

    def getRestrictions(self):  # Takes the appropriate html text and sets it to a list if text is found
        restrictionslist = []
        for y in range(4, 15):
            location = "auto-style"
            location += str(y)
            try:
                flightRestrictionsClass1 = self.soup.find(class_=location)  # find text
                restrictionslist.append(flightRestrictionsClass1.get_text())  # add to list
            except AttributeError:  # if no text is found, pass to the next
                pass
        return restrictionslist

    def setVariables(self, flightCategory, FRlist, restrictionslist2):  # creates memory variables.
        FC1 = flightCategory
        try:  # try to set variables equal
            FRlist[0] = restrictionslist2[0]
        except IndexError:  # if index error try to set individually
            pass

        try:
            FRlist[1] = restrictionslist2[1]
        except IndexError:
            pass

        try:
            FRlist[2] = restrictionslist2[2]
        except IndexError:
            pass

        try:
            FRlist[3] = restrictionslist2[3]
        except IndexError:
            pass

        try:
            FRlist[4] = restrictionslist2[4]
        except IndexError:
            pass
        return FC1, FRlist

    def scrape(self):  # sets up webpage desired and updates html text pulled
        page = requests.get("http://sof.aero.und.edu")
        self.soup = BeautifulSoup(page.content, "html.parser")

    def discordBot(self):  # main function to post scraped text to discord
        FC1 = 0  # memory variable for flight category
        printlist = []  # final list to be sent to discord
        FRlist = []  # list for memory, to compare one iteration from the next
        und.scrape()
        restrictionslist2 = und.getRestrictions()
        for x in restrictionslist2:  # creates an initial list based on the length of flight restrictions to avoid an index error on inital run
            FRlist.append(0)
        while 1 == 1:
            now = time.gmtime()  # time variable for code execution
            if now[6] <= 5 and (now[3] >= 12 or now[3] <= 4):  # if the day of the week is not sunday, and its between 23 - 14 Zulu (GMT) 8am to 5 CST
                und.scrape()
                flightCategory = und.getFlightCategory()  # sets html text to variables
                restrictionslist2 = und.getRestrictions()
                if flightCategory == FC1 and restrictionslist2 == FRlist:  # if nothing has changed since the last pass
                    time1 = (now[3] - 6)
                    print("No Change", time1)  # print time it checked for debugging
                    time.sleep(300)
                else:  # set memory variables for comparison later
                    FC1 = flightCategory
                    FRlist = restrictionslist2
                    #   FC1, FRlist = und.setVariables(flightCategory, FRlist, restrictionslist2)
                    if flightCategory == 'Closed':  # if the category is "Closed" only post closed
                        DiscordWebhook(url=url,
                                       content=('<@&796776150578757662> %s' % flightCategory)).execute()
                        print('Posted, Closed')
                        time.sleep(300)
                    else:  # if not "closed" iterate through each attribute in list, until "Manager on Duty" appears
                        for attribute in restrictionslist2:
                            if attribute == "Manager on Duty:":
                                string = ', '.join(printlist)
                                DiscordWebhook(url=url, content=(
                                        '<@&796776150578757662> %s, %s' % (flightCategory, string))).execute()
                                print('Posted')
                                printlist = []  # reset the list to wipe all past restrictions
                                time.sleep(300)
                                break
                            else:  # if not manager on duty, add the flight restriction to the list to be printed
                                printlist.append(attribute)

            else:
                print("Outside Time")
                time.sleep(300)


und = UND()
und.discordBot()

# time.struct_time(tm_year=2021, tm_mon=1, tm_mday=19, tm_hour=1, tm_min=15, tm_sec=14, tm_wday=1, tm_yday=19, tm_isdst=0)

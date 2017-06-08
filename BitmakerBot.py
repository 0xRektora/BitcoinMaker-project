import pyautogui
import os
from msvcrt import getch
import time
import threading
import sys
class BotMaker:
    def __init__(self):
        self.checkfile = 1
        os.system("cls")
        self.CheckFiles()
        self.mapState = {
            "withdraw" : self.Withdraw,
            "withdrawnot" : self.Withdraw,
            "BitmakerBot" : self.goToApp,
            "claimBtn" : self.goToApp,
            "crashError" : self.exceptError,
            "None" : self.WaitAds
        }

        if not self.checkfile:
            print("[-]One or more files missing.")
            exit()

        pyautogui.click(500, 2)
        # self.startThread = threading.Thread(target=self._Start)

    def _CheckFiles(self, fileName):
        #print("Checking", fileName+".")
        return os.path.isfile(fileName)

    def CheckFiles(self):
        self.checkfile = self._CheckFiles("back.png")
        self.checkfile = self._CheckFiles("booster.png")
        self.checkfile = self._CheckFiles("withdraw.png")
        self.checkfile = self._CheckFiles("withdraw2.png")
        self.checkfile = self._CheckFiles("withdrawnot.png")
        self.checkfile = self._CheckFiles("withdrawnot2.png")
        self.checkfile = self._CheckFiles("claimBtn.png")
        self.checkfile = self._CheckFiles("errorMsgBox.png")
        self.checkfile = self._CheckFiles("errorMsgBox2.png")
        self.checkfile = self._CheckFiles("errorOkBtn.png")
        self.checkfile = self._CheckFiles("booster.png")
        self.checkfile = self._CheckFiles("boosterBuyButton.png")
        self.checkfile = self._CheckFiles("boosterCheckBuy.png")
        self.checkfile = self._CheckFiles("BitmakerBot.png")

    def currentState(self, currentState=""):
        print("[+]currentState : " + currentState + ".")

    def WaitAds(self):
        self.currentState("Is ads ")
        self.ClickScreen("back.png")
        time.sleep(2)
        if self.Check_OnScreen("withdraw.png") or self.Check_OnScreen("withdrawnot.png"):
            pass
        else:
            self.ClickScreen("back.png")
            if self.Check_OnScreen("withdraw.png") or self.Check_OnScreen("withdrawnot.png"):
                pass
            else:
                self.currentState("Waiting ads")
                time.sleep(30)

    def goToApp(self, claim=False):
        if claim == False:
            print("\n[+]Returning to App.")
            time.sleep(1)
            self.ClickScreen("homeBtn.png")
            time.sleep(2)
            self.ClickScreen("BitmakerBot.png")
            time.sleep(10)
            self.ClickScreen("claimBtn.png")
            time.sleep(3)
        else:
            time.sleep(1)
            self.ClickScreen("claimBtn.png")
            time.sleep(1)

    def Check_OnScreen(self, fileName):
        time.sleep(1)
        if pyautogui.locateOnScreen(fileName) == None:
            return False
        else:
            return True

    def TakeBooster(self):
        if self.Check_OnScreen("booster.png"):
            self.ClickScreen("booster.png")
            time.sleep(2)
            if self.Check_OnScreen("boosterCheckBuy.png"):
                time.sleep(2)
                self.ClickScreen("boosterBuyButton.png")
                time.sleep(2)
            else:
                self.ClickScreen("booster.png")
                time.sleep(2)
        else:
            pass

    def exceptError(self):
        self.ClickScreen("homeBtn.png")
        time.sleep(2)
        self.ClickScreen("errorOkBtn.png")
        time.sleep(2)

    def ClickScreen(self, fileName, flag=False):
        print("Locating ", fileName)
        buttonLocation = pyautogui.locateOnScreen(fileName)
        try:
            buttonX, buttonY = pyautogui.center(buttonLocation)
            pyautogui.click(buttonX, buttonY)
        except:
            if flag:
                return False
        else:
            print("[+]ClickScreen finished for", fileName + ".")
            return True

    def Withdraw(self):
        while True:
            if self.Check_OnScreen("withdrawnot.png") or self.Check_OnScreen("withdrawnot2.png"):
                time.sleep(2)
                continue
            elif self.Check_OnScreen("withdraw.png") or self.Check_OnScreen("withdraw2.png"):
                time.sleep(1)
                if self.ClickScreen("withdraw.png"):
                    time.sleep(1)
                    self.ClickScreen("back.png")
                    time.sleep(1)
                    break
                else:
                    self.ClickScreen("withdraw2.png")
                    time.sleep(1)
                    self.ClickScreen("back.png")
                    time.sleep(1)

                    break
            else:
                print("[+]Withdraw buttons not found.")

    def GetState(self):
        if self.Check_OnScreen("withdraw.png") or self.Check_OnScreen("withdraw2.png"):
            self.currentState("withdraw")
            return "withdraw"
        elif self.Check_OnScreen("withdrawnot.png") or self.Check_OnScreen("withdrawnot2.png"):
            self.currentState("withdrawnot")
            return "withdrawnot"
        elif self.Check_OnScreen("claimBtn.png"):
            self.currentState("claimBtn")
            return "claimBtn"
        elif self.Check_OnScreen("BitmakerBot.png"):
            self.currentState("BitmakerBot")
            return "BitmakerBot"
        elif self.Check_OnScreen("errorMsgBox.png") or self.Check_OnScreen("errorMsgBox2.png") or self.Check_OnScreen("errorOkBtn.png"):
            self.currentState("errorMsgBox")
            return "crashError"
        else:
            self.currentState("None")
            return "None"

    def DoSomething(self):
        self.mapState[self.GetState()]()

    def Start(self):
        print("\n[+]Starting the bot")
        print("******************************")
        while True:
            self.DoSomething()
            time.sleep(3)
            self.TakeBooster()
            time.sleep(2)
        print("******************************\n")
        print("[+]Done")

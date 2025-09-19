from ib_insync import IB, Stock, util
import pandas as pd
import pandas_ta as ta
import yfinance as yf
import time
import sys
import requests

DiscordWebhook = ""


def conTest(ib):

    try:
        ib.reqCurrentTime()
        return True
    except: 
        return False
    
def sendAlert(message: str):

    payload = {"content": message}

    try:
        response = requests.post(DiscordWebhook, json=payload) #Discord Ping
        response.raise_for_status()
        print("Alert Sent")
    except: 
        print("Uh oh")
        return False

def calculateRSI(data, timeframe):

    RSI = ta.rsi(data['Close']['SPY'], length=timeframe)
    return RSI #consider adding .iloc[-1] if time is too slow

def calcuateMFI(data, timeframe):

    MFI = ta.mfi(data['High']['SPY'], data['Low']['SPY'],data['Close']['SPY'],data['Volume']['SPY'], length=timeframe)
    return MFI

def calculateADX(data, timeframe):
    
    ADX = ta.adx(data['High']['SPY'], data['Low']['SPY'],data['Close']['SPY'], length=timeframe)
    return ADX

def calcuateMACD(data):

    MACD = ta.macd(data['Close']['SPY'],fast=6, slow=13)
    return MACD

def calcuateATR(data, timeframe):

    ATR = ta.atr(data['High']['SPY'], data['Low']['SPY'],data['Close']['SPY'], length=timeframe)
    return ATR

def calcuateBollingerBands(data, timeframe):

    BB = ta.bbands(data['Close']['SPY'], length=timeframe, lower_std=.8, upper_std=.8)
    return BB
 







    


    
        














    
# %%
import sys
import os
import requests, random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime
from IPython.display import clear_output

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def cm_to_inch(value):
    return value/2.54;

def getCryptocurrencyData(currency = "BTC", fromCurrency = "USD", limit = 168):
    data = requests.get(f"https://min-api.cryptocompare.com/data/v2/histoday?fsym={currency}&tsym={fromCurrency}&limit={limit}").json();
    if(data["Response"] == "Error"):
        raise Exception(data["Message"]);
    return data;

def printPlot(toCurrency, fromCurrency, dateArray, priceArray):
    plt.figure(figsize=(cm_to_inch(50),cm_to_inch(30)));
    plt.plot(dateArray, priceArray, 'g-');
    plt.plot(dateArray, priceArray, 'ro');
    plt.xlabel(f'Data i godzina', fontsize=15);
    plt.ylabel(f'Wartość w {toCurrency}/{fromCurrency}', fontsize=15);
    red_patch = mpatches.Patch(color='green', label=f'Linia reprezentuje wartośc {toCurrency} -> {fromCurrency}');
    plt.legend(handles=[red_patch]);
    plt.show();

    
def prepareDateArray(responseData):
    dateArray = [];
    
    for row in responseData:
        ts = int(row["time"]);
        dateArray.append(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d'));
        
    return dateArray;

def prepareCloseArray(responseData):
    closeArray = [];
    
    for row in responseData:
        closeArray.append(row["close"])
        
    return closeArray;

def generatePlot(fromCurrency, toCurrency):
    responseData = getCryptocurrencyData(toCurrency, fromCurrency,14);
    plotDate = prepareDateArray(responseData["Data"]["Data"]);
    plotValues = prepareCloseArray(responseData["Data"]["Data"]);
    printPlot(toCurrency, fromCurrency, plotDate, plotValues);

while True:
    print('Autor Marek Derela, Indeks: 51147')
    print('Wybierz swoja opcje:');
    print('1. Lista walut');
    print('2. Pokaz wykres dowolnych walut.');
    print('3. Pokaz wykres BTC/USD');
    print('4. Pokaz wykres ETH/USD');
    print('5. Wyczyśc konsole.')
    print('6. Wyjscie.')
    x = input();
    if(x == '1'):
        print('Waluty FIAT:');
        print('USD  - $ Amerykański');
        print('EUR  - Euro');
        print('PLN  - Polski złoty');
        print('Kryptowaluty:');
        print('ETH  - Etherum');
        print('BTC  - Bitcoin');
        print('DOGE - DogeCoin');
        print('LTC  - Litecoin');
        print('XRP  - Ripple');
        print('XMR  - Monero');
        print('CHZ  - Chilliz');
    elif(x == '2'):
        try:
            print('Podaj z jakiej waluty: Np. BTC');
            fromCurrency = input();
            print('Na jaka walute: Np. USD');
            toCurrency = input();
            generatePlot(toCurrency,fromCurrency);
        except Exception as e:
            print(str(e));
    elif(x == '3'):
        generatePlot('USD','BTC');
    elif(x == '4'):
        generatePlot('USD','ETH');
    elif(x == '5'):
        clear_output(wait=True);
        clearConsole()
    elif(x == '6'):
        exit()
        

# %%

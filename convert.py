#!/usr/bin/env python
#coding: utf-8

# TODO convert time
# sec in hours
# s in h

# TODO convert weight
# kg in lbs

# TODO convert distance
# meter in inches
# m in in

from __future__ import print_function

import json
import os
import re
import sys
from subprocess import PIPE, Popen

import numpy
import requests
from bs4 import BeautifulSoup
from requests.structures import CaseInsensitiveDict

currencies = CaseInsensitiveDict()
currencies["AED"] = "United Arab Emirates Dirham (AED)"
currencies["AFN"] = "Afghan Afghani (AFN)"
currencies["ALL"] = "Albanian Lek (ALL)"
currencies["AMD"] = "Armenian Dram (AMD)"
currencies["ANG"] = "Netherlands Antillean Guilder (ANG)"
currencies["AOA"] = "Angolan Kwanza (AOA)"
currencies["ARS"] = "Argentine Peso (ARS)"
currencies["AUD"] = "Australian Dollar (A$)"
currencies["AWG"] = "Aruban Florin (AWG)"
currencies["AZN"] = "Azerbaijani Manat (AZN)"
currencies["BAM"] = "Bosnia-Herzegovina Convertible Mark (BAM)"
currencies["BBD"] = "Barbadian Dollar (BBD)"
currencies["BDT"] = "Bangladeshi Taka (BDT)"
currencies["BGN"] = "Bulgarian Lev (BGN)"
currencies["BHD"] = "Bahraini Dinar (BHD)"
currencies["BIF"] = "Burundian Franc (BIF)"
currencies["BMD"] = "Bermudan Dollar (BMD)"
currencies["BND"] = "Brunei Dollar (BND)"
currencies["BOB"] = "Bolivian Boliviano (BOB)"
currencies["BRL"] = "Brazilian Real (R$)"
currencies["BSD"] = "Bahamian Dollar (BSD)"
currencies["BTC"] = "Bitcoin (&#3647;)"
currencies["BTN"] = "Bhutanese Ngultrum (BTN)"
currencies["BWP"] = "Botswanan Pula (BWP)"
currencies["BYN"] = "Belarusian Ruble (BYN)"
currencies["BYR"] = "Belarusian Ruble (2000-2016) (BYR)"
currencies["BZD"] = "Belize Dollar (BZD)"
currencies["CAD"] = "Canadian Dollar (CA$)"
currencies["CDF"] = "Congolese Franc (CDF)"
currencies["CHF"] = "Swiss Franc (CHF)"
currencies["CLF"] = "Chilean Unit of Account (UF) (CLF)"
currencies["CLP"] = "Chilean Peso (CLP)"
currencies["CNH"] = "CNH (CNH)"
currencies["CNY"] = "Chinese Yuan (CN¥)"
currencies["COP"] = "Colombian Peso (COP)"
currencies["CRC"] = "Costa Rican Colón (CRC)"
currencies["CUP"] = "Cuban Peso (CUP)"
currencies["CVE"] = "Cape Verdean Escudo (CVE)"
currencies["CZK"] = "Czech Republic Koruna (CZK)"
currencies["DEM"] = "German Mark (DEM)"
currencies["DJF"] = "Djiboutian Franc (DJF)"
currencies["DKK"] = "Danish Krone (DKK)"
currencies["DOP"] = "Dominican Peso (DOP)"
currencies["DZD"] = "Algerian Dinar (DZD)"
currencies["EGP"] = "Egyptian Pound (EGP)"
currencies["ERN"] = "Eritrean Nakfa (ERN)"
currencies["ETB"] = "Ethiopian Birr (ETB)"
currencies["EUR"] = "Euro (&#8364;)"
currencies["FIM"] = "Finnish Markka (FIM)"
currencies["FJD"] = "Fijian Dollar (FJD)"
currencies["FKP"] = "Falkland Islands Pound (FKP)"
currencies["FRF"] = "French Franc (FRF)"
currencies["GBP"] = "British Pound (£)"
currencies["GEL"] = "Georgian Lari (GEL)"
currencies["GHS"] = "Ghanaian Cedi (GHS)"
currencies["GIP"] = "Gibraltar Pound (GIP)"
currencies["GMD"] = "Gambian Dalasi (GMD)"
currencies["GNF"] = "Guinean Franc (GNF)"
currencies["GTQ"] = "Guatemalan Quetzal (GTQ)"
currencies["GYD"] = "Guyanaese Dollar (GYD)"
currencies["HKD"] = "Hong Kong Dollar (HK$)"
currencies["HNL"] = "Honduran Lempira (HNL)"
currencies["HRK"] = "Croatian Kuna (HRK)"
currencies["HTG"] = "Haitian Gourde (HTG)"
currencies["HUF"] = "Hungarian Forint (HUF)"
currencies["IDR"] = "Indonesian Rupiah (IDR)"
currencies["IEP"] = "Irish Pound (IEP)"
currencies["ILS"] = "Israeli New Sheqel (&#8362;)"
currencies["INR"] = "Indian Rupee (&#8377;)"
currencies["IQD"] = "Iraqi Dinar (IQD)"
currencies["IRR"] = "Iranian Rial (IRR)"
currencies["ISK"] = "Icelandic Króna (ISK)"
currencies["ITL"] = "Italian Lira (ITL)"
currencies["JMD"] = "Jamaican Dollar (JMD)"
currencies["JOD"] = "Jordanian Dinar (JOD)"
currencies["JPY"] = "Japanese Yen (¥)"
currencies["KES"] = "Kenyan Shilling (KES)"
currencies["KGS"] = "Kyrgystani Som (KGS)"
currencies["KHR"] = "Cambodian Riel (KHR)"
currencies["KMF"] = "Comorian Franc (KMF)"
currencies["KPW"] = "North Korean Won (KPW)"
currencies["KRW"] = "South Korean Won (&#8361;)"
currencies["KWD"] = "Kuwaiti Dinar (KWD)"
currencies["KYD"] = "Cayman Islands Dollar (KYD)"
currencies["KZT"] = "Kazakhstani Tenge (KZT)"
currencies["LAK"] = "Laotian Kip (LAK)"
currencies["LBP"] = "Lebanese Pound (LBP)"
currencies["LKR"] = "Sri Lankan Rupee (LKR)"
currencies["LRD"] = "Liberian Dollar (LRD)"
currencies["LSL"] = "Lesotho Loti (LSL)"
currencies["LTL"] = "Lithuanian Litas (LTL)"
currencies["LVL"] = "Latvian Lats (LVL)"
currencies["LYD"] = "Libyan Dinar (LYD)"
currencies["MAD"] = "Moroccan Dirham (MAD)"
currencies["MDL"] = "Moldovan Leu (MDL)"
currencies["MGA"] = "Malagasy Ariary (MGA)"
currencies["MKD"] = "Macedonian Denar (MKD)"
currencies["MMK"] = "Myanmar Kyat (MMK)"
currencies["MNT"] = "Mongolian Tugrik (MNT)"
currencies["MOP"] = "Macanese Pataca (MOP)"
currencies["MRO"] = "Mauritanian Ouguiya (MRO)"
currencies["MUR"] = "Mauritian Rupee (MUR)"
currencies["MVR"] = "Maldivian Rufiyaa (MVR)"
currencies["MWK"] = "Malawian Kwacha (MWK)"
currencies["MXN"] = "Mexican Peso (MX$)"
currencies["MYR"] = "Malaysian Ringgit (MYR)"
currencies["MZN"] = "Mozambican Metical (MZN)"
currencies["NAD"] = "Namibian Dollar (NAD)"
currencies["NGN"] = "Nigerian Naira (NGN)"
currencies["NIO"] = "Nicaraguan Córdoba (NIO)"
currencies["NOK"] = "Norwegian Krone (NOK)"
currencies["NPR"] = "Nepalese Rupee (NPR)"
currencies["NZD"] = "New Zealand Dollar (NZ$)"
currencies["OMR"] = "Omani Rial (OMR)"
currencies["PAB"] = "Panamanian Balboa (PAB)"
currencies["PEN"] = "Peruvian Nuevo Sol (PEN)"
currencies["PGK"] = "Papua New Guinean Kina (PGK)"
currencies["PHP"] = "Philippine Peso (PHP)"
currencies["PKG"] = "PKG (PKG)"
currencies["PKR"] = "Pakistani Rupee (PKR)"
currencies["PLN"] = "Polish Zloty (PLN)"
currencies["PYG"] = "Paraguayan Guarani (PYG)"
currencies["QAR"] = "Qatari Rial (QAR)"
currencies["RON"] = "Romanian Leu (RON)"
currencies["RSD"] = "Serbian Dinar (RSD)"
currencies["RUB"] = "Russian Ruble (RUB)"
currencies["RWF"] = "Rwandan Franc (RWF)"
currencies["SAR"] = "Saudi Riyal (SAR)"
currencies["SBD"] = "Solomon Islands Dollar (SBD)"
currencies["SCR"] = "Seychellois Rupee (SCR)"
currencies["SDG"] = "Sudanese Pound (SDG)"
currencies["SEK"] = "Swedish Krona (SEK)"
currencies["SGD"] = "Singapore Dollar (SGD)"
currencies["SHP"] = "St. Helena Pound (SHP)"
currencies["SKK"] = "Slovak Koruna (SKK)"
currencies["SLL"] = "Sierra Leonean Leone (SLL)"
currencies["SOS"] = "Somali Shilling (SOS)"
currencies["SRD"] = "Surinamese Dollar (SRD)"
currencies["STD"] = "São Tomé &amp; Príncipe Dobra (STD)"
currencies["SVC"] = "Salvadoran Colón (SVC)"
currencies["SYP"] = "Syrian Pound (SYP)"
currencies["SZL"] = "Swazi Lilangeni (SZL)"
currencies["THB"] = "Thai Baht (THB)"
currencies["TJS"] = "Tajikistani Somoni (TJS)"
currencies["TMT"] = "Turkmenistani Manat (TMT)"
currencies["TND"] = "Tunisian Dinar (TND)"
currencies["TOP"] = "Tongan Pa&#699;anga (TOP)"
currencies["TRY"] = "Turkish Lira (TRY)"
currencies["TTD"] = "Trinidad &amp; Tobago Dollar (TTD)"
currencies["TWD"] = "New Taiwan Dollar (NT$)"
currencies["TZS"] = "Tanzanian Shilling (TZS)"
currencies["UAH"] = "Ukrainian Hryvnia (UAH)"
currencies["UGX"] = "Ugandan Shilling (UGX)"
currencies["USD"] = "US Dollar ($)"
currencies["UYU"] = "Uruguayan Peso (UYU)"
currencies["UZS"] = "Uzbekistani Som (UZS)"
currencies["VEF"] = "Venezuelan Bolívar (VEF)"
currencies["VND"] = "Vietnamese Dong (&#8363;)"
currencies["VUV"] = "Vanuatu Vatu (VUV)"
currencies["WST"] = "Samoan Tala (WST)"
currencies["XAF"] = "Central African CFA Franc (FCFA)"
currencies["XCD"] = "East Caribbean Dollar (EC$)"
currencies["XDR"] = "Special Drawing Rights (XDR)"
currencies["XOF"] = "West African CFA Franc (CFA)"
currencies["XPF"] = "CFP Franc (CFPF)"
currencies["YER"] = "Yemeni Rial (YER)"
currencies["ZAR"] = "South African Rand (ZAR)"
currencies["ZMK"] = "Zambian Kwacha (1968&#8211;2012) (ZMK)"
currencies["ZMW"] = "Zambian Kwacha (ZMW)"
currencies["ZWL"] = "Zimbabwean Dollar (2009) (ZWL)"


# TODO KiloJoule, cm**(-1)
# http://users.mccammon.ucsd.edu/~dzhang/energy-unit-conv-table.html

# For each energy unit, we note it's value in Joule
energies = CaseInsensitiveDict()
energies["J"] = 1
energies["au"] = 4.359745e-18
energies["eV"] = 1.6021766e-19
energies["kcal/mol"] = 6.9476e-21

# Alternative names
energies["hartree"] = energies["au"]
energies["Ha"] = energies["au"]
energies["kcal"] = energies["kcal/mol"]


def shell(cmd, shell=False):

    if shell:
        p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    else:
        cmd = cmd.split()
        p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)

    output, err = p.communicate()
    return output


def ask_wolfram_alpha(question):

    API_ERROR = """
Invalid API key.

1) Creat an account at
https://developer.wolframalpha.com/portal/signin.html

2) Create an API at
https://developer.wolframalpha.com/portal/myapps

after creating an APP API, dump the key in

~/.wolfram_api_key

"""

    try:
        f = os.path.expanduser("~/.wolfram_api_key")
        f = open(f, 'r')
        wa_key = f.next()
        wa_key = wa_key.strip()
        f.close()
    except IOError:
        print(API_ERROR)
        exit('Could not find .wolfram_api_key in your home directory')


    # Query wolfram alpha
    url =  "http://api.wolframalpha.com/v2/query"
    params = {'appid': wa_key,
              'input':question,
              'format': 'plaintext'}
    r = requests.get(url, params=params)
    data = BeautifulSoup(r.content, "lxml")

    # Parse WA

    success = data.queryresult['success']
    error = data.queryresult['error']

    if error == "true":
        quit(API_ERROR)

    if success == "false":
        quit("Sorry Wolfram Alpha did not understand your question")


    # TODO format the pod structure
    # for pid in data["queryresult"]["pod"]:
    #     print pid["subpod"]["plaintext"]

    # TODO format the | columns from the output

    output = data.find(title='Result').get_text().strip()
    print(output)

    quit()


def find_converter(args):

    value = args[0]
    unit_a = args[1]
    unit_b = args[3]

    # Energy
    if unit_a in energies and unit_b in energies:
        convert_energy(value, unit_a, unit_b)
        quit()

    # Currencey
    if unit_a in currencies and unit_b in currencies:
        convert_currency_currencyconvertapi(value, unit_a, unit_b)
        quit()

    return False


def convert_currency(value, fr, to):
    # http://www.linux-magazine.com/Online/Blogs/Productivity-Sauce/Simple-Bash-Currency-Converter
    url = "http://www.google.com/finance/converter"
    params = {'a':value,
              'from':fr,
              'to':to}
    r = requests.get(url, params=params)

    google_page = r.content # Get the html page
    parsed = BeautifulSoup(google_page, "lxml") # parse it with beautiful soup
    conversion = parsed.find(id='currency_converter_result').get_text()
    conversion = conversion.strip()
    if conversion == "": exit("Could not recognize currency: "+" ".join(args))
    print(conversion)


def convert_currency_currencyconvertapi(val, fr, to):

    fmt = "_".join([fr,to])
    params = {"q": fmt, "compact": "ultra"}
    url = "http://free.currencyconverterapi.com/api/v3/convert"

    # get r.url in json format
    r = requests.get(url, params=params)
    rate = r.json()
    rate = rate[fmt.upper()]

    print(rate*float(val), to)

    return

def convert_energy(value, unit_a, unit_b):
    value = float(value)
    conversion_factor = energies[unit_a] / energies[unit_b]
    value = value*conversion_factor
    print("{} {}".format(value, unit_b))


if __name__ == '__main__':

    args = sys.argv[1:]
    args_string = " ".join(args)

    USAGE = """Usage examples:

Energy Conversion:

    56.54 ev in kcal
    0.005 au in ev

Currency Conversion

    42 usd in dkk

Math

    42*5/80.0

Question (Using wolfram alpha)

    What is the temperature in Chicago?

"""

    converted = False
    ask_wolfram = False

    if len(args) == 0:
        exit(USAGE)

    if "in" in args or "to" in args:
        converted = find_converter(args)

    if len(args) == 2 and args[1] in currencies:
        args += ["in", "dkk"]
        converted = find_converter(args)
        quit()


    if "?" in args_string or ask_wolfram:
        ask_wolfram_alpha(" ".join(args))
        quit()

    # Evaluate argument as Python math
    print(eval(" ".join(args)))

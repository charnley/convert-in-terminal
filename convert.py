#!/usr/bin/env python
#coding: utf-8

# https://products.wolframalpha.com/short-answers-api/explorer/
# http://saironiq.blogspot.dk/2012/04/wolframalpha-cli-interface.html
# https://github.com/saironiq/shellscripts/blob/master/wolframalpha_com/wa.sh

# http://users.mccammon.ucsd.edu/~dzhang/energy-unit-conv-table.html

# TODO convert time
# sec in hours
# s in h

# TODO convert weight
# kg in lbs

# TODO convert distance
# meter in inches
# m in in

from subprocess import Popen, PIPE
import sys
import numpy
import re

CURRENCY = {}
CURRENCY["AED"] = "United Arab Emirates Dirham (AED)"
CURRENCY["AFN"] = "Afghan Afghani (AFN)"
CURRENCY["ALL"] = "Albanian Lek (ALL)"
CURRENCY["AMD"] = "Armenian Dram (AMD)"
CURRENCY["ANG"] = "Netherlands Antillean Guilder (ANG)"
CURRENCY["AOA"] = "Angolan Kwanza (AOA)"
CURRENCY["ARS"] = "Argentine Peso (ARS)"
CURRENCY["AUD"] = "Australian Dollar (A$)"
CURRENCY["AWG"] = "Aruban Florin (AWG)"
CURRENCY["AZN"] = "Azerbaijani Manat (AZN)"
CURRENCY["BAM"] = "Bosnia-Herzegovina Convertible Mark (BAM)"
CURRENCY["BBD"] = "Barbadian Dollar (BBD)"
CURRENCY["BDT"] = "Bangladeshi Taka (BDT)"
CURRENCY["BGN"] = "Bulgarian Lev (BGN)"
CURRENCY["BHD"] = "Bahraini Dinar (BHD)"
CURRENCY["BIF"] = "Burundian Franc (BIF)"
CURRENCY["BMD"] = "Bermudan Dollar (BMD)"
CURRENCY["BND"] = "Brunei Dollar (BND)"
CURRENCY["BOB"] = "Bolivian Boliviano (BOB)"
CURRENCY["BRL"] = "Brazilian Real (R$)"
CURRENCY["BSD"] = "Bahamian Dollar (BSD)"
CURRENCY["BTC"] = "Bitcoin (&#3647;)"
CURRENCY["BTN"] = "Bhutanese Ngultrum (BTN)"
CURRENCY["BWP"] = "Botswanan Pula (BWP)"
CURRENCY["BYN"] = "Belarusian Ruble (BYN)"
CURRENCY["BYR"] = "Belarusian Ruble (2000-2016) (BYR)"
CURRENCY["BZD"] = "Belize Dollar (BZD)"
CURRENCY["CAD"] = "Canadian Dollar (CA$)"
CURRENCY["CDF"] = "Congolese Franc (CDF)"
CURRENCY["CHF"] = "Swiss Franc (CHF)"
CURRENCY["CLF"] = "Chilean Unit of Account (UF) (CLF)"
CURRENCY["CLP"] = "Chilean Peso (CLP)"
CURRENCY["CNH"] = "CNH (CNH)"
CURRENCY["CNY"] = "Chinese Yuan (CN¥)"
CURRENCY["COP"] = "Colombian Peso (COP)"
CURRENCY["CRC"] = "Costa Rican Colón (CRC)"
CURRENCY["CUP"] = "Cuban Peso (CUP)"
CURRENCY["CVE"] = "Cape Verdean Escudo (CVE)"
CURRENCY["CZK"] = "Czech Republic Koruna (CZK)"
CURRENCY["DEM"] = "German Mark (DEM)"
CURRENCY["DJF"] = "Djiboutian Franc (DJF)"
CURRENCY["DKK"] = "Danish Krone (DKK)"
CURRENCY["DOP"] = "Dominican Peso (DOP)"
CURRENCY["DZD"] = "Algerian Dinar (DZD)"
CURRENCY["EGP"] = "Egyptian Pound (EGP)"
CURRENCY["ERN"] = "Eritrean Nakfa (ERN)"
CURRENCY["ETB"] = "Ethiopian Birr (ETB)"
CURRENCY["EUR"] = "Euro (&#8364;)"
CURRENCY["FIM"] = "Finnish Markka (FIM)"
CURRENCY["FJD"] = "Fijian Dollar (FJD)"
CURRENCY["FKP"] = "Falkland Islands Pound (FKP)"
CURRENCY["FRF"] = "French Franc (FRF)"
CURRENCY["GBP"] = "British Pound (£)"
CURRENCY["GEL"] = "Georgian Lari (GEL)"
CURRENCY["GHS"] = "Ghanaian Cedi (GHS)"
CURRENCY["GIP"] = "Gibraltar Pound (GIP)"
CURRENCY["GMD"] = "Gambian Dalasi (GMD)"
CURRENCY["GNF"] = "Guinean Franc (GNF)"
CURRENCY["GTQ"] = "Guatemalan Quetzal (GTQ)"
CURRENCY["GYD"] = "Guyanaese Dollar (GYD)"
CURRENCY["HKD"] = "Hong Kong Dollar (HK$)"
CURRENCY["HNL"] = "Honduran Lempira (HNL)"
CURRENCY["HRK"] = "Croatian Kuna (HRK)"
CURRENCY["HTG"] = "Haitian Gourde (HTG)"
CURRENCY["HUF"] = "Hungarian Forint (HUF)"
CURRENCY["IDR"] = "Indonesian Rupiah (IDR)"
CURRENCY["IEP"] = "Irish Pound (IEP)"
CURRENCY["ILS"] = "Israeli New Sheqel (&#8362;)"
CURRENCY["INR"] = "Indian Rupee (&#8377;)"
CURRENCY["IQD"] = "Iraqi Dinar (IQD)"
CURRENCY["IRR"] = "Iranian Rial (IRR)"
CURRENCY["ISK"] = "Icelandic Króna (ISK)"
CURRENCY["ITL"] = "Italian Lira (ITL)"
CURRENCY["JMD"] = "Jamaican Dollar (JMD)"
CURRENCY["JOD"] = "Jordanian Dinar (JOD)"
CURRENCY["JPY"] = "Japanese Yen (¥)"
CURRENCY["KES"] = "Kenyan Shilling (KES)"
CURRENCY["KGS"] = "Kyrgystani Som (KGS)"
CURRENCY["KHR"] = "Cambodian Riel (KHR)"
CURRENCY["KMF"] = "Comorian Franc (KMF)"
CURRENCY["KPW"] = "North Korean Won (KPW)"
CURRENCY["KRW"] = "South Korean Won (&#8361;)"
CURRENCY["KWD"] = "Kuwaiti Dinar (KWD)"
CURRENCY["KYD"] = "Cayman Islands Dollar (KYD)"
CURRENCY["KZT"] = "Kazakhstani Tenge (KZT)"
CURRENCY["LAK"] = "Laotian Kip (LAK)"
CURRENCY["LBP"] = "Lebanese Pound (LBP)"
CURRENCY["LKR"] = "Sri Lankan Rupee (LKR)"
CURRENCY["LRD"] = "Liberian Dollar (LRD)"
CURRENCY["LSL"] = "Lesotho Loti (LSL)"
CURRENCY["LTL"] = "Lithuanian Litas (LTL)"
CURRENCY["LVL"] = "Latvian Lats (LVL)"
CURRENCY["LYD"] = "Libyan Dinar (LYD)"
CURRENCY["MAD"] = "Moroccan Dirham (MAD)"
CURRENCY["MDL"] = "Moldovan Leu (MDL)"
CURRENCY["MGA"] = "Malagasy Ariary (MGA)"
CURRENCY["MKD"] = "Macedonian Denar (MKD)"
CURRENCY["MMK"] = "Myanmar Kyat (MMK)"
CURRENCY["MNT"] = "Mongolian Tugrik (MNT)"
CURRENCY["MOP"] = "Macanese Pataca (MOP)"
CURRENCY["MRO"] = "Mauritanian Ouguiya (MRO)"
CURRENCY["MUR"] = "Mauritian Rupee (MUR)"
CURRENCY["MVR"] = "Maldivian Rufiyaa (MVR)"
CURRENCY["MWK"] = "Malawian Kwacha (MWK)"
CURRENCY["MXN"] = "Mexican Peso (MX$)"
CURRENCY["MYR"] = "Malaysian Ringgit (MYR)"
CURRENCY["MZN"] = "Mozambican Metical (MZN)"
CURRENCY["NAD"] = "Namibian Dollar (NAD)"
CURRENCY["NGN"] = "Nigerian Naira (NGN)"
CURRENCY["NIO"] = "Nicaraguan Córdoba (NIO)"
CURRENCY["NOK"] = "Norwegian Krone (NOK)"
CURRENCY["NPR"] = "Nepalese Rupee (NPR)"
CURRENCY["NZD"] = "New Zealand Dollar (NZ$)"
CURRENCY["OMR"] = "Omani Rial (OMR)"
CURRENCY["PAB"] = "Panamanian Balboa (PAB)"
CURRENCY["PEN"] = "Peruvian Nuevo Sol (PEN)"
CURRENCY["PGK"] = "Papua New Guinean Kina (PGK)"
CURRENCY["PHP"] = "Philippine Peso (PHP)"
CURRENCY["PKG"] = "PKG (PKG)"
CURRENCY["PKR"] = "Pakistani Rupee (PKR)"
CURRENCY["PLN"] = "Polish Zloty (PLN)"
CURRENCY["PYG"] = "Paraguayan Guarani (PYG)"
CURRENCY["QAR"] = "Qatari Rial (QAR)"
CURRENCY["RON"] = "Romanian Leu (RON)"
CURRENCY["RSD"] = "Serbian Dinar (RSD)"
CURRENCY["RUB"] = "Russian Ruble (RUB)"
CURRENCY["RWF"] = "Rwandan Franc (RWF)"
CURRENCY["SAR"] = "Saudi Riyal (SAR)"
CURRENCY["SBD"] = "Solomon Islands Dollar (SBD)"
CURRENCY["SCR"] = "Seychellois Rupee (SCR)"
CURRENCY["SDG"] = "Sudanese Pound (SDG)"
CURRENCY["SEK"] = "Swedish Krona (SEK)"
CURRENCY["SGD"] = "Singapore Dollar (SGD)"
CURRENCY["SHP"] = "St. Helena Pound (SHP)"
CURRENCY["SKK"] = "Slovak Koruna (SKK)"
CURRENCY["SLL"] = "Sierra Leonean Leone (SLL)"
CURRENCY["SOS"] = "Somali Shilling (SOS)"
CURRENCY["SRD"] = "Surinamese Dollar (SRD)"
CURRENCY["STD"] = "São Tomé &amp; Príncipe Dobra (STD)"
CURRENCY["SVC"] = "Salvadoran Colón (SVC)"
CURRENCY["SYP"] = "Syrian Pound (SYP)"
CURRENCY["SZL"] = "Swazi Lilangeni (SZL)"
CURRENCY["THB"] = "Thai Baht (THB)"
CURRENCY["TJS"] = "Tajikistani Somoni (TJS)"
CURRENCY["TMT"] = "Turkmenistani Manat (TMT)"
CURRENCY["TND"] = "Tunisian Dinar (TND)"
CURRENCY["TOP"] = "Tongan Pa&#699;anga (TOP)"
CURRENCY["TRY"] = "Turkish Lira (TRY)"
CURRENCY["TTD"] = "Trinidad &amp; Tobago Dollar (TTD)"
CURRENCY["TWD"] = "New Taiwan Dollar (NT$)"
CURRENCY["TZS"] = "Tanzanian Shilling (TZS)"
CURRENCY["UAH"] = "Ukrainian Hryvnia (UAH)"
CURRENCY["UGX"] = "Ugandan Shilling (UGX)"
CURRENCY["USD"] = "US Dollar ($)"
CURRENCY["UYU"] = "Uruguayan Peso (UYU)"
CURRENCY["UZS"] = "Uzbekistani Som (UZS)"
CURRENCY["VEF"] = "Venezuelan Bolívar (VEF)"
CURRENCY["VND"] = "Vietnamese Dong (&#8363;)"
CURRENCY["VUV"] = "Vanuatu Vatu (VUV)"
CURRENCY["WST"] = "Samoan Tala (WST)"
CURRENCY["XAF"] = "Central African CFA Franc (FCFA)"
CURRENCY["XCD"] = "East Caribbean Dollar (EC$)"
CURRENCY["XDR"] = "Special Drawing Rights (XDR)"
CURRENCY["XOF"] = "West African CFA Franc (CFA)"
CURRENCY["XPF"] = "CFP Franc (CFPF)"
CURRENCY["YER"] = "Yemeni Rial (YER)"
CURRENCY["ZAR"] = "South African Rand (ZAR)"
CURRENCY["ZMK"] = "Zambian Kwacha (1968&#8211;2012) (ZMK)"
CURRENCY["ZMW"] = "Zambian Kwacha (ZMW)"
CURRENCY["ZWL"] = "Zimbabwean Dollar (2009) (ZWL)"

CONVERT = {}
CONVERT["HARTREE"] = {}
CONVERT["ELECTRONVOLT"] = {}
CONVERT["KILOCALORIESPERMOLE"] = {}

CONVERT["HARTREE"]["ELECTRONVOLT"] = 27.211396641
CONVERT["ELECTRONVOLT"]["HARTREE"]= 1.0/CONVERT["HARTREE"]["ELECTRONVOLT"]

CONVERT["HARTREE"]["KILOCALORIESPERMOLE"] = 627.509 # kcal mol-1
CONVERT["KILOCALORIESPERMOLE"]["HARTREE"] = 1.0/CONVERT["HARTREE"]["KILOCALORIESPERMOLE"]

CONVERT["KILOCALORIESPERMOLE"]["ELECTRONVOLT"] = 0.0433634
CONVERT["ELECTRONVOLT"]["KILOCALORIESPERMOLE"] = 1.0/CONVERT["KILOCALORIESPERMOLE"]["ELECTRONVOLT"]

# TODO KiloJoule, cm**(-1)

CONVERTDICT = {}
CONVERTDICT["au"] = "HARTREE"
CONVERTDICT["ev"] = "ELECTRONVOLT"
CONVERTDICT["kcal"] = "KILOCALORIESPERMOLE"

def shell(cmd, shell=False):

    if shell:
        p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    else:
        cmd = cmd.split()
        p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)

    output, err = p.communicate()
    return output


def convert_energy(value, unit_a, unit_b):
    """

    """

    value = float(value)

    key_a = CONVERTDICT[unit_a]
    key_b = CONVERTDICT[unit_b]

    value = value*CONVERT[key_a][key_b]


    return value


if __name__ == '__main__':

    args = sys.argv[1:]

    if "help" in args or len(args) == 0:
        print """
usage examples:

56 ev to kcal
42 usd to dkk

"""
        exit()



    convert = False

    try:
        if args[2] == "in" or args[2] == "to":

            value = args[0]
            from_unit = args[1]
            to_unit = args[3]

            if from_unit.upper() in CURRENCY.keys():
                # http://www.linux-magazine.com/Online/Blogs/Productivity-Sauce/Simple-Bash-Currency-Converter
                google = shell('wget -qO- "http://www.google.com/finance/converter?a='+value+'&from='+from_unit+'&to='+to_unit+'" | sed "/res/!d;s/<[^>]*>//g";', shell=True)
                google = google.strip()
                if google == "": exit("Could not recognize currency: "+" ".join(args))
                print google


            elif from_unit.lower() in CONVERTDICT.keys():

                print convert_energy(value, from_unit.lower(), to_unit.lower()), to_unit.lower()

                exit()


            else:

                print args
                exit("Did not understand your conversion")

    except IndexError:
        pass

    # Evaluate argument as Python math
    print eval(" ".join(args))




#
#     import argparse
#     import sys
#
#     description = """
# Calculate Root-mean-square deviation (RMSD) between structure A and B, in XYZ
# or PDB format. The order of the atoms *must* be the same for both structures.
#
# citation:
#  - Kabsch algorithm:
#    Kabsch W., 1976, A solution for the best rotation to relate two sets of
#    vectors, Acta Crystallographica, A32:922-923, doi:10.1107/S0567739476001873
#
#  - Quaternion algorithm:
#    Michael W. Walker and Lejun Shao and Richard A. Volz, 1991, Estimating 3-D
#    location parameters using dual number quaternions, CVGIP: Image
#    Understanding, 54:358-367, doi: 10.1016/1049-9660(91)90036-o
#
#  - Implementation:
#    Calculate RMSD for two XYZ structures, GitHub,
#    http://github.com/charnley/rmsd
#
# """
#
#     epilog = """
# The script will return three RMSD values:
# Normal: The RMSD calculated the straight-forward way.
# Kabsch: RMSD after coordinates are translated and rotated using Kabsch.
# Quater: RMSD after coordinates are translated and rotated using quaternions.
# """
#
#     parser = argparse.ArgumentParser(
#                     description=description,
#                     formatter_class=argparse.RawDescriptionHelpFormatter,
#                     epilog=epilog)
#
#     parser.add_argument('structure_a', metavar='structure_a.xyz', type=str)
#     parser.add_argument('structure_b', metavar='structure_b.xyz', type=str)
#     parser.add_argument('-o', '--output', action='store_true', help='print out structure A, centered and rotated unto structure B\'s coordinates in XYZ format')
#     parser.add_argument('-n', '--no-hydrogen', action='store_true', help='ignore hydrogens when calculating RMSD')
#     parser.add_argument('-f', '--format', action='store', help='Format of input files. Supports xyz or pdb.')
#     parser.add_argument('-r', '--remove-idx', nargs='+', type=int, help='index list of atoms NOT to consider')
#     parser.add_argument('-a', '--add-idx', nargs='+', type=int, help='index list of atoms to consider')
#
#     if len(sys.argv) == 1:
#         parser.print_help()
#         sys.exit(1)
#

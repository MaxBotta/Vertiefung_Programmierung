from xbrl import *
import re
import xml.etree.ElementTree as ET

#file = open("./Novartis/Novartis-2002-11-15.xml", "r")
#file = open("./sweetsandtreats/data", "r")
#file = open("./test_data/HelloWOrld.xml", "r")


tree = ET.parse("sample-Instance-Proof.xml")
root = tree.getroot()




def set_spacing(string, x):
    i = len(string)
    spacing = ""
    while i <= x:
        space = " "
        spacing = spacing + space
        i = i + 1
    return spacing


gaap = "{http://xasb.org/gaap}"


def get_facts(topic):
    result = root.findall(gaap + topic)
    dict = {}
    for item in result:
        if item.get("contextRef") == "D-2006":
            dict["2006"] = item.text
        elif item.get("contextRef") == "D-2007":
            dict["2007"] = item.text

    return dict


revenue_gross = get_facts("RevenuesGross")
cost_of_sales = get_facts("CostOfSales")
returns_and_allowances = get_facts("ReturnsAndAllowances")
revenues_net = get_facts("RevenuesNet")
gross_profit_loss = get_facts("GrossProfitLoss")


def print_table():
    print("Topic" + set_spacing("Topic", 25) + "2006" + set_spacing("2006", 10) + "2007")
    print("--------------------------------------------------")
    print("Revenue Gross" + set_spacing("Revenue gross", 25) + str(revenue_gross["2006"]) + set_spacing(str(revenue_gross["2006"]), 10) + str(revenue_gross["2007"]))
    print("Cost of Sales" + set_spacing("Cost of Sales", 25) + str(cost_of_sales["2006"]) + set_spacing(str(cost_of_sales["2006"]), 10) + str(cost_of_sales["2007"]))
    print("Returns and Allowences" + set_spacing("Returns and Allowances", 25) + str(returns_and_allowances["2006"]) + set_spacing(str(returns_and_allowances["2006"]), 10) + str(returns_and_allowances["2007"]))
    print("Revenues Net" + set_spacing("Revenues Net", 25) + str(revenues_net["2006"]) + set_spacing(str(revenues_net["2006"]), 10) + str(revenues_net["2007"]))
    print("Gross Profit Loss" + set_spacing("Gross Profit Loss", 25) + str(gross_profit_loss["2006"]) + set_spacing(str(gross_profit_loss["2006"]), 10) + str(gross_profit_loss["2007"]))


print_table()














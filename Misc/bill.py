import random
import time
import datetime
import json


def getBillID():
    format1 = "%Y%m%d%H%M%S"
    return datetime.datetime.today().strftime(format1)


def getBillDate():
    start = "01/01/2008 00:00:00"
    end = "01/01/2009 23:59:59"
    time_format = "%m/%d/%Y %H:%M:%S"
    prop = random.random()
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))

def getStoreID():
    return random.randint(1, 4)

def getProductID():
    return random.randint(1, 25)

def getQty():
    return random.randint(1, 20)


#
#l_bills_path = "E:\\code\\PYTHON_TRAINING\\Assignments\\Billing\\bills\\"
l_bills_path = "//Users//arun//PycharmProjects//python//Misc//IP_FILE//"

run = True

while run:
    l_bill_id = getBillID()

    l_bill_json = {"BillID": l_bill_id
        , "BillDate": getBillDate()
        , "StoreID": getStoreID()
                   }

    print("print(l_bill_json):", l_bill_json)

    l_bill_details = {}

    print("print(l_bill_details):", l_bill_details)

    for c1 in range(random.randint(1, 25)):
        l_bill_details[getProductID()] = getQty()

    print("print(l_bill_details):", l_bill_details)

    l_bill_json["BillDetails"] = l_bill_details

    print("print(l_bill_json):", l_bill_json)

    new_file = open(l_bills_path + l_bill_id + "_sample_hema.json", "w")
    new_file.write(json.dumps(l_bill_json))
    new_file.close()

    run = False


    #time.sleep(2)
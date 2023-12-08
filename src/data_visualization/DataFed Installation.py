# Import packages

import os
import getpass
import subprocess
from platform import platform
import sys
from datafed.CommandLib import API
from datafed import version as df_ver

try:
    datapath = os.mkdir("./datapath")
except:
    datapath = "./datapath"
sys.version_info
platform()

df_api = API()

print("Success! You have DataFed: " + df_ver)
if df_api.getAuthUser():
    print(
        "Success! You have been authenticated into DataFed as: " + df_api.getAuthUser()
    )
else:
    print("You have not authenticated into DataFed Client")
    print(
        'Please follow instructions in the "Basic Configuration" section in the link below to authenticate yourself:'
    )
    print("https://ornl.github.io/DataFed/user/client/install.html#basic-configuration")
if not df_api.endpointDefaultGet():
    print("Please follow instructions in the link below to find your Globus Endpoint:")
    print(
        "https://ornl.github.io/DataFed/system/getting_started.html#install-identify-globus-endpoint"
    )
    endpoint = input(
        "\nPlease enter either the Endpoint UUID or Legacy Name for your Globus Endpoint: "
    )
    df_api.endpointDefaultSet(endpoint)

print("Your default Globus Endpoint in DataFed is:\n" + df_api.endpointDefaultGet())
# This is a dataGet Command
dget_resp = df_api.dataGet("d/49965349", os.path.abspath(datapath), wait=True)
dget_resp
if dget_resp[0].task[0].status == 3:
    print("Success! Downloaded a test file to your location. Removing the file now")
    os.remove(os.path.abspath(datapath) + "/49965349.ibw")
else:
    if dget_resp[0].task[0].msg == "globus connect offline":
        print(
            "You need to activate your Globus Endpoint and/or ensure Globus Connect Personal is running.\n"
            "Please visit https://globus.org to activate your Endpoint"
        )
    elif dget_resp[0].task[0].msg == "permission denied":
        print(
            "Globus does not have write access to this directory. \n"
            "If you are using Globus Connect Personal, ensure that this notebook runs within"
            "one of the directories where Globus has write access. You may consider moving this"
            "notebook to a valid directory or add this directory to the Globus Connect Personal settings"
        )
    else:
        NotImplementedError(
            "Get in touch with us or consider looking online to find a solution to this problem:\n"
            + dget_resp[0].task[0].msg
        )

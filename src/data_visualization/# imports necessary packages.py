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
    datapath = "C:/Users/24867/Data_Visualization/src/data_visualization/"
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
        "\nPlease enter either the Endpoint UUID or Legacy Name for your Globus Endpoint: e7d4c58a-8fc8-11ee-83c0-d5484943e99a"
    )
    df_api.endpointDefaultSet(endpoint)

print("Your default Globus Endpoint in DataFed is:\n" + df_api.endpointDefaultGet())

# This is a dataGet Command
dget_resp = df_api.dataGet("d/500652535", os.path.abspath(datapath), wait=True)
dget_resp


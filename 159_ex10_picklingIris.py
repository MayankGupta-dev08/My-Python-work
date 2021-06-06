from typing import ItemsView
import requests
import pickle

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# getting the response and data from url in str form
# resp = requests.get(url)
# resp_txt = resp.text # or
resp_txt = requests.get(url).text
# print(resp_txt)
print("Completed getting data!!")

with open("uci-ML-IrisData.txt", "w") as f:
    f.write(resp_txt) # Writing it to txt file, here its in string format
    print("Created a txt file with fetched data")

dataList = resp_txt.splitlines() # Creating a list of the recieved data which was in string format by spliting at new line character
# print(dataList) # List having many string elements
dataList2 = [item.split(",") for item in dataList if len(item)!=0] # Using list comprehension to directly creating a list out of another list
# print(dataList2) # List having many list elements

# Pickling the data from list to binary data
with open("uci-ML-IrisData.pkl", "wb") as f2:
    pickle.dump(dataList2, f2)
    print("Finished Pickling")

# Unpickling the data from binary to readable data
with open("uci-ML-IrisData.pkl", "rb") as f2:
    DList = pickle.load(f2)
    print("Finished Unpickling")
    print(DList)
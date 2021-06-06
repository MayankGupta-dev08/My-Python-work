import requests
import pickle

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# getting the response and data from url in str form
resp = requests.get(url)
resp_txt = resp.text
print("Completed getting data!!")
with open("uci-ML-IrisData.txt", "w") as f:
    f.write(resp_txt)
    # Writing it to txt file
    print("Created a txt file.")
dataList = resp_txt.splitlines()
# Creating a list of the recieved data

# Pickling the data from list to binary data
with open("uci-ML-IrisData.pkl", "wb") as f2:
    pickle.dump(dataList, f2)
    print("Finished Pickling")

# Unpickling the data from binary to readable data
with open("uci-ML-IrisData.pkl", "rb") as f2:
    DList = pickle.load(f2)
    print("Finished Unpickling")
for i, j in enumerate(DList):
    print(f"{j}")
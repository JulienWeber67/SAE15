open("U:/Documents/lora-energie-transmission/data/raw/energy-125-7-4_5.csv", "r")
desc =open("U:/Documents/lora-energie-transmission/data/raw/energy-125-7-4_5.csv", "r")
content = desc.readline()
for idx in content :
    print(idx)
desc.close()
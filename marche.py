desc1 = open("U:/Documents/lora-energie-transmission/data/raw/energy-125-7-4_5.csv","r")
desc2 = open("U:/Documents/lora-energie-transmission/data/raw/energy-125-7-4_6.csv","r")
desc3 = open("U:/Documents/lora-energie-transmission/data/raw/energy-125-7-4_7.csv","r")
desc4 = open("U:/Documents/lora-energie-transmission/data/raw/energy-125-7-4_8.csv","r")
desc5 = open("U:/Documents/lora-energie-transmission/data/raw/energy-125-12-4_5.csv","r")
desc6 = open("U:/Documents/lora-energie-transmission/data/raw/energy-125-12-4_6.csv","r")
desc7 = open("U:/Documents/lora-energie-transmission/data/raw/energy-125-12-4_7.csv","r")
desc8 = open("U:/Documents/lora-energie-transmission/data/raw/energy-125-12-4_8.csv","r")
content =desc1.readline()
for idx in content :
    desc1 = open("U:/Documents/lora-energie-transmission/data/processed/cleantest.csv","a")
    desc1.write(idx)
desc1.close()

desc1.close()
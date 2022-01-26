open("../lora-energie-transmission", "r")
desc =open("../lora-energie-transmission", "r")
content = desc.readline()
for idx in content :
    print(idx)
desc.close()
import json
with open("data.json", "r") as read_file:
    data = json.load(read_file)
print("Interface Status")
print('='*81)

print("""DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")

for j in range(3):
    for i, k in data["imdata"][j]['l1PhysIf']["attributes"].items():
        if i == 'dn':
            print(k, end="                               ")
            for i, k in data["imdata"][j]['l1PhysIf']["attributes"].items():
                if i == "speed":
                    print(k, end="  ")
                    for i, k in data["imdata"][j]['l1PhysIf']["attributes"].items():
                        if i == "mtu":
                            print(k, end=" "*51)

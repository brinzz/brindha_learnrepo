import json
with open('ex5.json','r') as f:
    ex5 = json.load(f)
    for data in ex5:
        if data['name'] == "Old Fashioned" and data['type'] == "donut":
            batter = data['batters']['batter']
            batter.append({"id":"2345","type":"coffee"})
            print(data)
with open("ex5.json","w") as f:
    json.dump(ex5,f)
    f.close()
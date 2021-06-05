import pandas as pd
import json
import matplotlib
import matplotlib.pyplot as plt

matplotlib.style.use('dark_background')

with open('c:\localapp\logs\speedtest.json') as f:
    content = [json.loads(line.rstrip('\n')) for line in f]

df_dict = []
for item in content:
    try:
        t_dict = {"timestamp": item["timestamp"],
            "jitter":    item["ping"]["jitter"],
            "latency":   item["ping"]["latency"],
            "download":  item["download"]["bandwidth"] / 1024 / 1024 * 8,
            "upload":    item["upload"]["bandwidth"] / 1024 / 1024 * 8,
            "packetLoss": item["packetLoss"]}
    except KeyError as e:
        print(item)
        print(e)
        continue
    df_dict.append(t_dict)

df = pd.DataFrame.from_dict(df_dict)

ax = df.plot(subplots=True, figsize=(8, 8))
plt.legend(loc='best')
plt.savefig('test_graph_2.jpg', bbox_inches='tight')

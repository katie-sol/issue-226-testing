import os
import yaml


os.makedirs("nested folder", exist_ok=True)
with open("nested folder/sample.txt", "w", encoding="utf-8") as f:
    f.write("expected content")


config_data = [
    {
        "nested folder/sample.txt": [
            {
                "check": "MatchFileFragment",
                "options": {
                    "fragment": "expected content",
                    "count": 1
                }
            }
        ]
    }
]


with open("gatorgrade.yml", "w", encoding="utf-8") as f:
    yaml.dump(config_data, f, default_flow_style=False)

print("gatorgrade.yml generated cleanly!")
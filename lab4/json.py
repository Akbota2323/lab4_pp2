import json

file_path = r"C:\Users\МММ\Downloads\sample-data.json"

with open(file_path, "r") as file:
    data = json.load(file)

header = f"{'Interface Status':^80}\n{'='*80}\n{'DN':<60}{'Description':<20}{'Speed':<10}{'MTU':<5}\n{'-'*80}"
output = [header]

for item in data.get("imdata", []):
    attributes = item.get("l1PhysIf", {}).get("attributes", {})
    dn = attributes.get("dn", "N/A")
    description = attributes.get("descr", "")  
    speed = attributes.get("speed", "N/A")
    mtu = attributes.get("mtu", "N/A")
    

    output.append(f"{dn:<60}{description:<20}{speed:<10}{mtu:<5}")


formatted_output = "\n".join(output)
print(formatted_output)


with open("output.txt", "w", encoding="utf-8") as output_file:
    output_file.write(formatted_output)

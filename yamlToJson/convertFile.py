## Python Script to convert YAML to JSON
import sys
import yaml
import json

# Handle files inputted by user on command line
filein = sys.argv[1]
fileout = sys.argv[2]

print ("You would like to convert ", filein)
print ("n", fileout)


# List to hold the data from file
data = {}

# Read the YAML file & load to data list
with open("c:\temp\operating-systems.yml") as infile:
    data = yaml.load(infile, Loader=yaml.FullLoader)     
    print(data)

#Open a file to write the JSON output. The 'w' makes the file writable
with open("c:\temp\python_operating-systems.json", 'w') as outfile:
    json.dump(data, outfile, indent=4) 
    print("JSON file written.")


## Python Program to convert YAML to JSON and JSON to YAML
import sys
import yaml
import json

# Handle files inputted by user on command line
filein = sys.argv[1]
fileout = sys.argv[2]

# List to hold the data from file
data = {}

# Function to convert JSON file to YAML file
def create_yaml():
    # Read the YAML file & load to data list
    with open(filein) as infile:
        data = yaml.load(infile, Loader=yaml.FullLoader)     
        print(data)

    #Open a file to write the JSON output. The 'w' makes the file writable
    with open(fileout, 'w') as outfile:
        json.dump(data, outfile, indent=4) 
        print("JSON file written.")


# YAML >> JSON
if( ( filein.endswith('.yml') ) or ( filein.endswith('.yaml') )):
    print ("\nYou would like to convert", filein, end=' ')
    print ("to", fileout, "\n\n")
    print ("YAML file to JSON file.\n\n")

# JSON >> YAML
if( ( filein.endswith('.jsn') ) or ( filein.endswith('.json') )):
    print ("\nYou would like to convert", filein, end=' ')
    print ("to", fileout)
    print ("JSON file to YAML file.\n\n")
    create_yaml()



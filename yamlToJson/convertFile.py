## Python Script to convert YAML to JSON
import sys
import yaml
import json

# Handle files inputted by user on command line
filein = sys.argv[1]
fileout = sys.argv[2]

if( ( filein.endswith('.yml') ) or ( filein.endswith('.yaml') )):
    print ("\nYou would like to convert", filein, end=' ')
    print ("to", fileout, "\n\n")
    print ("YAML file to JSON file.\n\n")

if( ( filein.endswith('.jsn') ) or ( filein.endswith('.json') )):
    print ("\nYou would like to convert", filein, end=' ')
    print ("to", fileout)
    print ("JSON file to YAML file.\n\n")


# List to hold the data from file
data = {}

def create_yaml():
    # Read the YAML file & load to data list
    with open(filein) as infile:
        data = yaml.safe_load(infile, Loader=yaml.FullLoader)     
        print(data)

    #Open a file to write the JSON output. The 'w' makes the file writable
    with open(fileout, 'w') as outfile:
        json.dump(data, outfile, indent=4) 
        print("JSON file written.")



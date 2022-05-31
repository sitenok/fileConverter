## Python Program to convert YAML to JSON and JSON to YAML
import sys
import yaml
import json

# Handle files inputted by user on command line
filein = sys.argv[1]
fileout = sys.argv[2]

if( argc != 3 ):
    print ("Usage: convertFile.py filein.ext fileout.ext\n")
    exit

# Function to convert YAML file to JSON file
def create_json():
    with open(filein, 'r') as yaml_in, open(fileout, "w") as json_out:
        yaml_data = yaml.safe_load(yaml_in)
        json.dump(yaml_data, json_out)
    print ("JSON file written.\n")
    
# Function to convert JSON file to YAML file
def create_yaml():
    with open(filein, 'r') as json_in, open(fileout, "w") as yaml_out:
        json_data = json.load(json_in)
        yaml.dump(json_data, yaml_out, sort_keys=False)
    print ("YAML file written.")
    

# YAML >> JSON
if( ( filein.endswith('.yml') ) or ( filein.endswith('.yaml') )):
    print ("\nYou would like to convert", filein, "to", fileout, "?\n")
    print ("YAML file to JSON file.\n")
    ans = input("Y or N: ")
    if( ans == ('y' or 'Y') ):
        create_json()
    else:
        print("Goodbye")
        exit

# JSON >> YAML
if( ( filein.endswith('.jsn') ) or ( filein.endswith('.json') )):
    print ("\nYou would like to convert", filein, end=' ')
    print ("to", fileout)
    print ("JSON file to YAML file.\n")
    ans = str(input("Y or N: "))
    print (ans)
    if( ans == ('y' or 'Y') ):
        create_yaml()
    else:
        print("Goodbye")
        exit



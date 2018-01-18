# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:38:57 2018

@author: Red VII
"""

import pandas as pd
import os
import configparser

def chk(**kwargs):
    if 'smt' in kwargs:
        print(kwargs['smt'])

def typecheck(val,**kwargs):
    if 'bypass' in kwargs and kwargs['bypass'] != '':
        dt = kwargs['bypass']
    else:
        dt = val.dtype
    if dt in ["int64","int","float"]:
        return val.astype(str)
    else:
        return "'" + val.astype(str) + "'"

#If you have just 1 column of data

def onecol(df,bypass_type):
    #bypass_type = 'float' #either str, int or float
    
    if bypass_type.lower() in ["","none"] or bypass_switch != "on":
        print("No bypass. Autodetecting types.")
        del bypass_type
    
    if modswitch == "on":
        try:
            commadel = df.apply(lambda x: ",".join(typecheck(x,bypass=bypass_type)),axis=1)
        except:
            commadel = df.apply(lambda x: ",".join(typecheck(x)),axis=1)
        return commadel.apply(lambda x: prefix + ' ' + x + ' ' + suffix)
    else:
        try:
            commadel = df.apply(lambda x: ",".join(typecheck(x,bypass=bypass_type)))
        except:
            commadel = df.apply(lambda x: ",".join(typecheck(x)))
        return commadel
    


#If you have multiple columns

def multcol(df,bypass_types):
    #bypass_types = ['','str'] #in order of all columns in dataframe. if you don't want a bypass, leave blank. Possible values: str, int, float
    
    if bypass_types.lower() in ["","none"] or bypass_switch != "on":
        print("No bypass. Autodetecting types.")
        del bypass_types
    
    try:
        multicols = df.apply(lambda x: typecheck(x,bypass=bypass_types[df.columns.get_loc(x.name)])).apply(lambda x:",".join(x),axis=1)
    except:
        multicols = df.apply(lambda x: typecheck(x)).apply(lambda x:",".join(x),axis=1)
        
    #multicols.to_clipboard(index=False)
    #multicols.apply(lambda x: "SELECT " + x + " FROM DUAL UNION ALL").to_clipboard(index=False)
    if modswitch == "on":
        return multicols.apply(lambda x: prefix + ' ' + x + ' ' + suffix)
    else:
        return multicols


def bypass_check(var):
    if "," in var:
        lst = var.split(",")
        out = [x.strip() for x in lst]
        return out
    else:
        return var.strip()

def filepath():
    try:
        path = os.path.dirname(os.path.realpath(__file__))
    except:
        path = input("Insert path of your directory:")
    return path

def read_config():
    global config
    global modswitch
    global prefix
    global suffix
    global readfrom
    global filesep
    global output
    global bypass
    global bypass_switch
    global headerflag
    #os.chdir(os.path.dirname(sys.argv[0]))
    try:
        os.chdir(filepath())
    except Exception as e:
        print("Error reading your script's current directory.")
        print(e)
    config = configparser.ConfigParser()
    config.read("config.py")
    modswitch = str(config["STRINGMODS"]["MODSWITCH"]).lower()
    prefix = str(config["STRINGMODS"]["PREFIX"])
    suffix = str(config["STRINGMODS"]["SUFFIX"])
    readfrom = str(config["DEFAULT"]["READFROM"])
    filesep = str(config["DEFAULT"]["FILESEP"]).encode("utf_8").decode("unicode_escape")
    output = str(config["DEFAULT"]["OUTPUT"])
    bypass = bypass_check(str(config["BYPASS"]["BYPASS"])).lower()
    bypass_switch = bypass_check(str(config["BYPASS"]["BYPASSSWITCH"])).lower()
    headerflag = True if str(config["DEFAULT"]["HEADER"]).lower() == "true" else False



def main():
    #READ CONFIG
    try:
        read_config()
    except Exception as e:
        print("Error with reading config file.")
        print(e)
        return
    
    #READ INPUT
    try:
        if readfrom == "CLIPBOARD":
            print("Reading from clipboard.")
            if headerflag == True:
                df = pd.read_clipboard(sep="\t")
            else:
                df = pd.read_clipboard(sep="\t",header=None)
        elif readfrom == "FILE":
            print("Reading from FILE: input.txt")
            
            if headerflag == True:
                df = pd.read_csv("input.txt",sep=filesep)
            else:
                df = pd.read_csv("input.txt",sep=filesep,header=None)
    except Exception as e:
        print("Error with reading from %s" %readfrom)
        print(e)
        return
    
    #PROCESS COLUMNS
    try:
        cols = len(df.columns)
        
        if cols == 1:
            print("One column detected.")
            outdf = onecol(df,bypass)
        elif cols > 1:
            print("Multiple coulmns detected.")
            outdf = multcol(df,bypass)
        else:
            print("Error")
            return
    except Exception as e:
        print("Input processed successfully, but error reading columns.")
        print(e)
        return
    
    #THROW OUTPUT
    try:
        if output == "CLIPBOARD":
            outdf.to_clipboard(index=False)
            print("Done. Outputted to clipboard.")
        elif output == "FILE":
            outdf.to_csv("output.txt",sep=filesep,index=False)
            print("Done. Outputted to FILE: output.txt")
    except Exception as e:
        print("Error outputting.")
        print(e)
        return

main()

input() #waits for user to prses enter before closing the console



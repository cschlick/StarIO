"""
Two simple functions for processing Relion .star files:

dataframe = read_star("path/to/file.star")

write_star(dataframe,"path/to/newfile.star)


Author: Christopher Schlicksup
License: MIT

"""


from pathlib import Path
import pandas as pd
import numpy as np
import shutil




def read_star(filepath):
    """
    Parameters
    ----------

    filepath : Either a string or a Path object, which points to the star file


    Returns:
    ---------

    dataframe_dict: A dictionary where keys are the names of the data blocks, and values are pandas dataframes

    """
    if not isinstance(filepath,Path):
        filepath = Path(filepath)



    class DataBlock:
        def __init__(self,title):
            self.title = title

            self.loops = []
            self.data_items = {}


    class Loop:
        def __init__(self):
            self.keys = []

    def iscomment(linestring):
        if linestring[0] == "#":
            return True
        else:
            return False        
    

    def isblank(linestring): 
        split = linestring.strip("\n").split()
        tests = ["\t","\n"]
        results = [bool(not s not in tests or s.isspace()) for s in split]
        return all(results)
    
    def isint(x):
        try:
            a = float(x)
            b = int(a)
        except ValueError:
            return False
        else:
            if "." in x:
                return False
            else:
                return a == b


    def isfloat(x):
        try:
            a = float(x)
        except ValueError:
            return False
        else:
            return True

    
    def process_looped_data_line(current_loop,line):
        data_items = line.split() # comments on data lines not implemented yet
        try:
            assert(len(data_items) == len(current_loop.keys))
            for i,key in enumerate(current_loop.keys):
                value = data_items[i].strip("\n")
                if isint(value):
                    value = int(value)
                elif isfloat(value):
                    value = float(value)

                current_loop.data_items[key].append(value)
            
        except AssertionError:
            print("Number of items in data loop line does not equal length of loop keys")
            print(current_loop.keys)
            print("\t",line)
    
    # at each line we can define a parsing state using flags
    parseflag_datablock = False
    parseflag_loop_keys = False 
    parseflag_loop_data = False

    # data for each block is stored in a datablock class
    datablocks = []
    current_datablock = None
    current_loop = None


    # by default we ignore commented lines "#" or lines with only whitespace. 
    # Data on each line is separated by whitespace
    with filepath.open("r") as fh:

        for line in fh:
            if (iscomment(line) == False) and (isblank(line) == False):
                line = line.lstrip()
                line = line.strip("\n")


                if line[:5] == "data_": # we are entering a new data block.

                    #Check if one is already open
                    if parseflag_datablock == True: # close previous block
                        if parseflag_loop_data == True:
                            current_datablock.loops.append(current_loop)
                            current_loop = None
                        datablocks.append(current_datablock)

                    # make new datablock
                    title = line.split("#")[0].replace("data_","")
                    if title == "":
                        title = "data"
                    current_datablock = DataBlock(title)
                    parseflag_datablock = True
                    parseflag_loop_data = False

                # make loop
                elif line[:5] == "loop_":
                    parseflag_loop_keys= True
                    if current_loop == None:
                        current_loop = Loop()
                    else:
                        current_datablock.loops.append(current_loop)
                        current_loop = Loop()

                # encountered data key
                elif line[0] == "_":
                    # key as part of a loop
                    if parseflag_loop_keys == True:
                        if "#" in line:
                            line = line.split("#")[0]
                        split = [s.strip()for s in line.split()]
                        key = split[0][1:]
                        current_loop.keys.append(key)

                    # or simple key,value data
                    else:
                        if "#" in line:
                            line = line.split("#")[0]
                        split = [s.strip()for s in line.split()]
                        key = split[0][1:]
                        value = split[1]

                        if isint(value):
                            value = int(value)
                        elif isfloat(value):
                            value = float(value)


                        current_datablock.data_items[key] = value

                # encountering looped data values, or error
                else:
                    if parseflag_loop_keys == True:
                        parseflag_loop_keys = False
                        parseflag_loop_data = True
                        current_loop.data_items = {key:[] for key in current_loop.keys}
                        process_looped_data_line(current_loop,line)


                    elif parseflag_loop_data == True:
                        process_looped_data_line(current_loop,line)


                    else:
                        print("Error Parsing line:")
                        print("\t",line)



    # finish
    if current_loop != None:
        current_datablock.loops.append(current_loop)

    if current_datablock != None:
        datablocks.append(current_datablock)


    # make into pandas dataframe
    df_dict = {}
    for block in datablocks:
        if bool(block.data_items) == False: # only has loop
            assert(len(block.loops) == 1)

            df = pd.DataFrame(block.loops[0].data_items)

        else:
            assert(len(block.loops)==0)
            df = pd.DataFrame(block.data_items,index=range(1))
        df.name = block.title
        df_dict[block.title] = df


    return df_dict
        


# write a df to star file
def write_star(filepath,df):
    """
    Parameters
    ----------

    filepath : Either a string or a Path object, where a new star file will be written
          df : A pandas dataframe.

    Returns:
    ---------
       None
    """
    if isinstance(filepath,pd.DataFrame):
        df_ = filepath
        filepath = df
        df = df_

    if not isinstance(filepath,Path):
        filepath = Path(filepath)
    with filepath.open("w") as fh:
        # title
        try:
            fh.write("data_"+df.name)
        except:
            fh.write("data_")
        fh.write("\n")
        if len(df) > 1: # need to do loop
            fh.write("loop_")
            fh.write("\n")
            for column in df.columns:
                fh.write("_"+column+"\n")
            for i,row in df.iterrows():
                rowstring = ""
                for val in row:
                    if type(val) == int:
                        entry = str(val).rjust(12)
                        entry = entry.rjust(12)
                    elif type(val) == float:
                        if val > 1.0e+5:
                            entry = "{:.6e}".format(val)
                        else:
                            entry = "{0:.6f}".format(val)
                        entry = entry.rjust(12)
                    else: # assume string
                        entry = val

                    rowstring= rowstring+" "+entry
                rowstring= rowstring+"\n"
                fh.write(rowstring)

    





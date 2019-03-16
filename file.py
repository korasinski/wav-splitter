# waverd_1.py
# When reading a binary file, Python converts values to strings.
# To decode the strings we need the struct module

import struct

def file_info(file_name, value):

    output = []

    #0
    output.append(file_name)

    # open(fname,mode) is the Python way of reading files
    file = open(file_name,"rb") # Read wav file, "r flag" - read, "b flag" - binary

    #print("\n")
    #print("New file loaded")
    #print("\n")

    #1
    ChunkID=file.read(4) # First four bytes are ChunkID which must be "RIFF" in ASCII
    #print("ChunkID",ChunkID)
    output.append(ChunkID)

    #2
    ChunkSizeString=file.read(4) # Total Size of File in Bytes - 8 Bytes
    ChunkSize=struct.unpack('I',ChunkSizeString) # 'I' Format is to to treat the 4 bytes as unsigned 32-bit inter
    TotalSize=ChunkSize[0]+8 # The subscript is used because struct unpack returns everything as tuple
    TotalSizeHuman = humansize(TotalSize)
    #print("TotalSize=",TotalSizeHuman)
    output.append(TotalSizeHuman)

    #3
    DataSize=TotalSize-44 # This is the number of bytes of data
    #print("DataSize=",DataSize)
    output.append(DataSize)

    #4
    Format=file.read(4) # "WAVE" in ASCII
    #print("Format=",Format)
    output.append(Format)

    #5
    SubChunk1ID=file.read(4) # "fmt " in ASCII
    #print("SubChunk1ID=",SubChunk1ID)
    output.append(SubChunk1ID)

    #6
    SubChunk1SizeString=file.read(4) # Should be 16 (PCM, Pulse Code Modulation)
    SubChunk1Size=struct.unpack("I",SubChunk1SizeString) # 'I' format to treat as unsigned 32-bit integer
    #print("SubChunk1Size=",SubChunk1Size[0])
    output.append(SubChunk1SizeString)

    #7
    AudioFormatString=file.read(2) # Should be 1 (PCM)
    AudioFormat=struct.unpack("H",AudioFormatString) # 'H' format to treat as unsigned 16-bit integer
    #print("AudioFormat=",AudioFormat[0])
    output.append(AudioFormat[0])

    #8
    NumChannelsString=file.read(2) # Should be 1 for mono, 2 for stereo
    NumChannels=struct.unpack("H",NumChannelsString) # 'H' unsigned 16-bit integer
    #print("NumChannels=",NumChannels[0])
    output.append(NumChannels)

    #9
    SampleRateString=file.read(4) # Should be 44100 (CD sampling rate)
    SampleRate=struct.unpack("I",SampleRateString)
    #print("SampleRate=",SampleRate[0])
    output.append(SampleRate)

    #10
    ByteRateString=file.read(4) # 44100*NumChan*2 (88200 - Mono, 176400 - Stereo)
    ByteRate=struct.unpack("I",ByteRateString) # 'I' unsigned 32 bit integer
    #print("ByteRate=",ByteRate[0])
    output.append(ByteRate)

    #11
    BlockAlignString=file.read(2) # NumChan*2 (2 - Mono, 4 - Stereo)
    BlockAlign=struct.unpack("H",BlockAlignString) # 'H' unsigned 16-bit integer
    #print("BlockAlign=",BlockAlign[0])
    output.append(BlockAlign)

    #12
    BitsPerSampleString=file.read(2) # 16 (CD has 16-bits per sample for each channel)
    BitsPerSample=struct.unpack("H",BitsPerSampleString) # 'H' unsigned 16-bit integer
    #print("BitsPerSample=",BitsPerSample[0])
    output.append(BitsPerSample)

    #13
    SubChunk2ID=file.read(4) # "data" in ASCII
    #print("SubChunk2ID=",SubChunk2ID)
    output.append(SubChunk2ID)

    #14
    SubChunk2SizeString=file.read(4) # Number of Data Bytes, Same as DataSize
    SubChunk2Size=struct.unpack("I",SubChunk2SizeString)
    #print("SubChunk2Size=",SubChunk2Size[0])
    output.append(SubChunk2Size)

    #15
    S1String=file.read(2) # Read first data, number between -32768 and 32767
    S1=struct.unpack("h",S1String)
    #print("S1=",S1[0])
    output.append(S1[0])

    #16
    S2String=file.read(2) # Read second data, number between -32768 and 32767
    S2=struct.unpack("h",S2String)
    #print("S2=",S2[0])
    output.append(S2[0])

    #17
    S3String=file.read(2) # Read second data, number between -32768 and 32767
    S3=struct.unpack("h",S3String)
    #print("S3=",S3[0])
    output.append(S3[0])

    #18
    S4String=file.read(2) # Read second data, number between -32768 and 32767
    S4=struct.unpack("h",S4String)
    #print("S4=",S4[0])
    output.append(S4[0])

    #19
    S5String=file.read(2) # Read second data, number between -32768 and 32767
    S5=struct.unpack("h",S5String)
    #print("S5=",S5[0])
    output.append(S5[0])

    file.close()

    print(output)

    return (output[value]);







suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']

def humansize(nbytes):
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])


import os
import zipfile


# Declare the function to return all file paths of the particular directory
def retrieve_file_paths(dirName):
    # setup file paths variable
    filePaths = []

    # Read all directory, subdirectories and file lists
    for root, directories, files in os.walk(dirName):
        for filename in files:
            # Create the full filepath by using os module.
            filePath = os.path.join(root, filename)
            filePaths.append(filePath)

    # return all paths
    return filePaths


# Declare the main function
def create_zip():
    # Assign the name of the directory to zip
    os.remove('export.zip')
    dir_name = 'export'

    # Call the function to retrieve all files and folders of the assigned directory
    filePaths = retrieve_file_paths(dir_name)

    # printing the list of all files to be zipped
    print('The following list of files will be zipped:')
    for fileName in filePaths:
        print(fileName)

    # writing files to a zipfile
    zip_file = zipfile.ZipFile(dir_name + '.zip', 'w')
    with zip_file:
        # writing each file one by one
        for file in filePaths:
            zip_file.write(file)

    print(dir_name + '.zip file is created successfully!')

    for f in filePaths:
        os.remove(f)




from scipy.io import wavfile


def multichannel(file_name,channel_amount):

    fs, data = wavfile.read(file_name)  # reading the file

    p_channel = channel_amount[0]
    #print(p_channel)

    for ch in range(p_channel):
        p_name = "export/channel_{0}.wav".format(ch)
        wavfile.write(p_name, fs, data[:, ch])  # saving x column which corresponds to channel x
        #print(p_name)


    create_zip()

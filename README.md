# wav-splitter
### A lightweight WebApp for WAV files processing
This is a web aplication that allow to split every channel on WAV audio file into separate files. You are able to download them as a ZIP file. There is also a function that returns a lot of data hidden in header of .wav files (RIFF tables).

------------------------------

![Screenshoot](https://i.imgur.com/EUpJNo2.png)

------------------------------
### Usage

When loading WAV file the output of console will be:

```
['/wav-splitter/upload/6ch.wav', b'RIFF', '2.95 MB', 3089016, b'WAVE', b'fmt ', b'(\x00\x00\x00', 65534, (6,), (44100,), (529200,), (12,), (16,), b'\x16\x00\x10\x00', (63,), 1, 0, 0, 16, 128]
The following list of files will be zipped:
export/channel_0.wav
export/channel_1.wav
export/channel_2.wav
export/channel_3.wav
export/channel_4.wav
export/channel_5.wav
export.zip file is created successfully!
```

-------------------------------

### Options

ID | key | type / notes
---|----|---------
1 |`filename` | path to uploaded file 
2 |`ChunkID` | First four bytes are ChunkID which must be "RIFF" in ASCII
3 |`ChunkSizeString` | Total Size of File in Bytes - 8 Bytes
4 |`Format` | "WAVE" in ASCII
5 |`SubChunk1ID` | "fmt " in ASCII
6 |`SubChunk1SizeString` | Should be 16 (PCM, Pulse Code Modulation)
7 |`AudioFormatString` | Should be 1 -> (PCM)
8 |`NumChannelsString` | Should be 1 for mono, 2 for stereo... 
9 |`SampleRateString` | Should be 44100 (CD sampling rate)
10|`ByteRateString` | SampleRateString * NumChanString * NumChannelsString
11|`BlockAlignString` | NumChan * 2
12|`BitsPerSampleString` | 16 (CD has 16-bits per sample for each channel)
13|`SubChunk2ID=file` | "data" in ASCII
14|`SubChunk2SizeString` | Number of Data Bytes, Same as DataSize
15|`S1String` | Read first sample data, number between -32768 and 32767
16|`S2String` | Read second saple data
17|`S3String` | Read third sample data
18|`S4String` | Read fourth sample data
19|`S5String` | Read fifth sample data
-------------------------------

Source: http://pythonaudio.blogspot.com/2014/04/3-reading-wave-file.html

-------------------------------

### Libraries

* Bootstrap -  https://github.com/twbs/bootstrap 
* particles.js - https://github.com/VincentGarreau/particles.js
* bootstrap-filestyle.js - https://github.com/markusslima/bootstrap-filestyle

-------------------------------

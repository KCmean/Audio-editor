from pydub import AudioSegment
from playsound import playsound 

def cut(Start, End, sound):
    slice = sound[Start:End]
    return slice

def merge(slice1,slice2):
    merge = slice1+ slice2
    return merge
slices = ["1.mp3", "2.mp3"]

start_min, start_sec=  map(int , input("\n Enter the starting point as (1(mins) 30(secs)) : ").split(' '))
end_min, end_sec = map(int, input("\n Enter the ending point as (1(mins) 30(secs)) : ").split(' ') )
start = start_min*60000 + start_sec*1000
end = end_min*60000 + end_sec*1000
sound= AudioSegment.from_mp3("E:/sem 2/python programming/python ptoject/audio/1.mp3")
slice = cut(start, end , sound)
slices.append(slice)
slice.export("3.mp3" , format = "mp3")

import os
import subprocess
f = os.listdir(os.path.dirname("H:/o/"))
def gvlen(file_path):
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", file_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return float(result.stdout.strip())
# print(f)
for i in f:
    vlen=gvlen("H:/o/"+i)
    os.system("ffmpeg -f lavfi -i color=c=black:s=360x240:d={} -c:v h264 -crf 35 -preset slow -an H:/p/{}".format(vlen,i))

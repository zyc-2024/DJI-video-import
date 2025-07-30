# DJI Video Import
## Tips：文件名在filelist.xlsx里

### 首先，下载仓库

可以用`git clone`或者下载压缩包。

文件格式
```
|
\-MISC
  \-IDX
  \-THM
  \-AC002.db
```


### 然后把你的视频拷过来

可以用整合视频.bat合并视频，其中第15行是视频路径，第20行是几个视频合成一个

### 然后用生成空壳视频.py生成空mp4

你要的视频后缀LRF，空mp4后缀mp4。

### 之后放在DCIM/DJI_002里

*******
*******

ffmpeg记得加进PATH里哦！
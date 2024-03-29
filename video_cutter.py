from moviepy.editor import VideoFileClip, concatenate_videoclips
start=True
#Insert video name and clips time
import_videoname="palabrotas.mp4"
export_videoname="final_video.mp4"
#format ==> [[initial_clip_time,final_clip_time],[initial_clip_time,final_clip_time],...] IN SECONDS
#No matter how many intervals you insert, it works
t_clips=[[2,6],[10,15],[20,25]]

#Code
for i,f in t_clips:
  clip1 = VideoFileClip(import_videoname).subclip(i,f)
  if start:
    final_clip = clip1
    start=False
  else:
    final_clip = concatenate_videoclips([final_clip,clip1])

final_clip.write_videofile(export_videoname)
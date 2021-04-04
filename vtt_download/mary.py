from __future__ import unicode_literals
import youtube_dlc
import argparse
import os

from converter import toTxt

parser = argparse.ArgumentParser(
    description='Interfaz de línea de comandos para descargar guiones de videos',
    prog="MARY")    

parser.add_argument('link', metavar='[link]',
                    help='El link del video a convertir')

parser.add_argument('-s','--sub', action="store_true",
help='Colocar si el video viene con subtítulos manuales',
)

args = parser.parse_args()

#         'writesubtitles': ---
#         'writeautomaticsub': ---
#         'subtitleslangs': --- 
#         'skip_download': --- 
#         'outtmpl': ---

ydl_opts = {
'skip_download': True,
'forcetitle': True,
'writesubtitles': args.sub,
'writeautomaticsub': (not args.sub),
'subtitleslangs': ["es"],
# 'outtmpl': '%(title)s.%(ext)s' , 
}

with youtube_dlc.YoutubeDL(ydl_opts) as ydl:
    ydl.download([args.link])
    info_dict = ydl.extract_info(args.link, download=False)
    video_id = info_dict.get('id', None)

# Looking for the video file by ID 
subtitles = os.listdir('.')
res = list(filter(lambda x: video_id in x, subtitles))

# When we found it, we only have to convert it to text
toTxt(res[0])

# Now it only converts  automatically generated .vtt files, we need to tweak
# the algorith to convert default subtitle .vtt files properly 



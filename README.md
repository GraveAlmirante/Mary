
# DESCRIPTION

**Mary** is a command line application for downloading youtube video's scripts or, for being more precise, their subtitles.
It is entirely made in python, using the [youtube-dl](https://github.com/ytdl-org/youtube-dl#readme) proyect.

    mary https://www.youtube.com/watch?v=oyeaQtn_svI&t=19s 
    
# CLI USAGE
<ol>
<li>Move the `mary.exe` file on your desired directory. </li>

<em>(remember that in said directory our <strong>.txt transcript</strong> will be saved)</em>

<li>Open a Command Line Terminal on said directory</li>
<li>Type the  <strong> mary </strong> keyword followed by the desired youtube link video to download, as shown: </li>
   
    mary https://www.youtube.com/watch?v=oyeaQtn_svI&t=19s

<li>You'll be left with two files the <strong>.txt</strong> file it's the one you'll be more insterested in.</li>
</ol>

# ERRORS

At the moment, you need to specify if the video that you'll transcript, only has Spanish generated subtitles as shown below:

    mary https://www.youtube.com/watch?v=wOuM8girLuY -s  

<em> You also could use the `--sub` option in this case. </em>


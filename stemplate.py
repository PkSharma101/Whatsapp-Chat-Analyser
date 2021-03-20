header = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<style>
    h1{
         text-align:center;
       }
        h3{
         text-align:center;
       }
     
     
    img{
        height: 500px;
        display: block;
        margin-left: auto;
        margin-right: auto;
       
    }
</style>
<body>
    
            <h1>WHATSAPP CHAT ANALYSIS REPORT</h1>
        <br>
"""

rmt = """
<h3>Rate of messages in an year </h3>
        <br>
        <img src="Output/rtime.png">
        <br>
"""

rmd = """
<h3>Rate of messages in a typcal day </h3>
        <br>
        <img src="Output/rdate.png">
        <br>
"""

up_start = """
<h3>List of unique people in chat</h3>
        <br>
        <ul>
"""
up_end = """
</ul>
<br>
"""

emoji_start = """
<h3>Rate of emojis</h3>
<br>
<img src="Output/remoji.png">
<br>
"""

url_start = """
<h3>List of URLs</h3>
<br>
<ul>
"""

phn_start= """
<h3>Phone Numbers in Chat< and all Alphanumeric words/h3>
<br>
<ul>
"""

media = """
<h3>Media count</h3>
<br>
<img src ="Output/icount.png">
<br>
"""
wc_start = """
<h3>Word Clouds</h3>
<br>
"""


footer = """ 
</body>
</html>

"""

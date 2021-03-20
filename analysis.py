import re
import matplotlib.pyplot as plt
from collections import defaultdict
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import emoji as pemoji
from wordcloud import WordCloud
from datetime import datetime



Output = "Output/"


def load_data(file_name):
    with open(file_name) as file:
        data = [line.strip() for line in file.readlines()]
    i = 2
    j = 0
    sdata = []
    while i<len(data):
        ap = data[i].split(" ")
        try :
            if ap[2] == "AM" or ap[2] == "PM":
                sdata.append(data[i])
                j+=1
                i+=1
            else:
                sdata[j-1] = sdata[j-1] +" "+ data[i]
                i+=1
        except:
            sdata[j-1] = sdata[j-1] +" "+ data[i]
            i+=1
    data = sdata

    data  = [ re.sub("\u200e", "", line) for line in data]
    return data

def rate_emoji(file_name):
    data = load_data(file_name)
    emoji_pattern = re.compile("["
                                u"\U0001F600-\U0001F64F"  
                                u"\U0001F300-\U0001F5FF"  
                                u"\U0001F680-\U0001F6FF"  
                                u"\U0001F1E0-\U0001F1FF" 
                                u"\U00002500-\U00002BEF"  
                                u"\U00002702-\U000027B0"
                                u"\U00002702-\U000027B0"
                                u"\U000024C2-\U0001F251"
                                u"\U0001f926-\U0001f937"
                                u"\U00010000-\U0010ffff"
                                u"\u2640-\u2642"
                                u"\u2600-\u2B55"
                                u"\u200d"
                                u"\u23cf"
                                u"\u23e9"
                                u"\u231a"
                                u"\ufe0f"  
                                u"\u3030"
                                "]+", flags=re.UNICODE)

    emodata = []
    for line in data:
        emojis = re.findall(emoji_pattern,line)
        if emojis:
            try:
                temp = line.split(" - ")[1].strip()
                name = temp.split(":")[0].strip()
            except:
                pass
            emodata.append([name,emojis])
    
    grp_emodata = []
    for line,emojis in emodata:
        cond = re.findall("You were added | removed | changed the subject",line)
        if cond:
            grp_emodata.append([line,emojis])

    emodata = [x for x in emodata if x not in grp_emodata]
    return emodata



# %% [markdown]
# Remove Devnagri words


def remove_dev(file_name):
    data = load_data(file_name)
    edata =[]
    for line in data:
        exp = "([A-Za-z]|[0-9]| |/|:|<|>|-)"
        line = re.findall(exp, line)
        line = "".join(alpha for alpha in line)
        line = line.strip()
        edata.append(line)
    return edata

lname = {}
def image_count(file_name):
    edata = remove_dev(file_name)
    textdata = []
   
    for line in edata:
        image = re.findall("<image omitted>|<video omitted>|<GIF omitted>| <Media omitted>",line)
        if line:
            if image:
                try:
                    temp = line.split(" - ")[1].strip()
                    name = temp.split(":")[0].strip()
                    try:
                        lname[name]+=1
                    except:
                        lname[name]=1
                except:
                    print(line)
            else:
                textdata.append(line)
    
    fig = plt.figure(figsize=(7, 5))
    plt.ylabel("Numbers")
    fig.suptitle('Media Exchanged')
    plt.bar(range(len(lname)), list(lname.values()), align='center',color=["#e76f51", '#e9c46a'])
    plt.xticks(range(len(lname)), list(lname.keys()))
    plt.savefig(Output+"icount.png")
    return textdata

def get_url(file_name):
    textdata = image_count(file_name)
    url_regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    lurl = []
    murldata =[] 
    for line in textdata:
        url = re.findall(url_regex,line)
        if url:
            try:
                name = line.split(" - ")[1].split(":")[0]
                lurl.append([name,url[0][0]])
            except:
                pass
        else:
            murldata.append(line)
    textdata = murldata
    return textdata,lurl


def unq_people(file_name):
    textdata,_ = get_url(file_name)
    uname = []
    for line in textdata:
        name = line.split(" - ")[1].split(":")[0]
        uname.append(name)
    uname = set(uname)
    fname = []
    for name in uname:
        if not re.findall("changed|encryption|removed|no longer an admin|added|left|now an admin",name):
            fname.append(name)
    return textdata,fname


def make_text_corpous(file_name):
    textdata,fname = unq_people(file_name)
    corpous = {}
    for line in textdata:
        name = line.split(" - ")[1].split(":")[0]
        
      
    
        if name in fname:
            try:
                temp = corpous[name]
                t = line.split(" - ")[1].strip()
                temp = temp + " "+t.split(":")[1].strip()
                corpous[name] = temp
            except:
                t = line.split(" - ")[1].strip()
                temp = t.split(":")[1].strip()
            
                corpous[name] = temp
    textcorpous = corpous
  
    return textcorpous,textdata,fname

def rate_date(file_name):
    textdata,fname = unq_people(file_name)
    corpous = {}
    for line in textdata:
        name = line.split(" - ")[1].split(":")[0]
        
        if name in fname:
            try:
                temp = corpous[name]
                temp = temp + " "+line.split(" ")[0].split("/")[0].strip()
                corpous[name] = temp
            except:
                temp =  line.split(" ")[0].split("/")[0].strip()
                corpous[name] = temp
    date = corpous
    for key in date.keys():
        dstr = date[key]
        date[key] = dstr.split(" ")
    return date

def rate_time(file_name):
    textdata,fname = unq_people(file_name)
    corpous = {}
    for line in textdata:
        
        name = line.split(" - ")[1].split(":")[0]
        if name in fname:
            try:
                temp = corpous[name]
                temp = temp + ","+line.split(" ")[1] +" "+line.split(" ")[2].split(" - ")[0]
                corpous[name] = temp
            except:
                temp =  line.split(" ")[1] +" "+line.split(" ")[2].split(" - ")[0]
                corpous[name] = temp
    time = corpous
    for key in fname:
        try:
            dstr = time[key]
            time[key] = dstr.split(",")
        except:
            pass
    return time


def get_number(file_name):
    textcorpous,_,_ = make_text_corpous(file_name)
    numberdb ={}
    for key in textcorpous.keys():
        data = textcorpous[key]
        tokens = word_tokenize(data)
        numbers = [word.lower() for word in tokens if not word == "" and not word.isalpha() and len(word)>3]
        tokens = [word.lower() for word in tokens if not word == "" and word.isalpha()]
        lemmas = [lemmatizer.lemmatize(token) for token in tokens]
        ftokens = [word for word in lemmas if not word in stopwords.words('english')]
        textcorpous[key] = ftokens
        if numbers:
            numberdb[key] = numbers
    return numberdb,textcorpous

def plot_rate_date(file_name):
    date = rate_date(file_name)
    date_list = []
    for name in date.keys():
        date_list.extend(date[name])
    
    date_list.sort(key = int)

    date_fdict = defaultdict( int )
    for x in date_list:
        date_fdict[x] += 1

    fig = plt.figure(figsize=(20, 7))
    fig.suptitle('Proportion of Messages over the year')
    plt.xlabel("Month Number")
    plt.ylabel("Numbers")
    plt.bar(range(len(date_fdict)), list(date_fdict.values()), align='center', color= "#7209B7")
    plt.xticks(range(len(date_fdict)), list(date_fdict.keys()))
    dpath = Output+"rdate.png"
    plt.savefig(dpath)
    return dpath

def plot_rate_time(file_name):
    time = rate_time(file_name)
    time_list = []
    for name in time.keys():
        time_list.extend(time[name])

    hh_list = []
    for tz in time_list:    
        ap = tz.split(":")[1].split(" ")[1]
        hh = tz.split(":")[0]
        hh_list.append(hh+" "+ap)
    
    hh_list.sort(key = lambda date: datetime.strptime(date, '%I %p')) 

    time_fdict = defaultdict( int )
    for x in hh_list:
        time_fdict[x] += 1

    fig = plt.figure(figsize=(20, 7))
    fig.suptitle('Rate of messages in a typical day')
    plt.bar(range(len(time_fdict)), list(time_fdict.values()), align='center', color=["#EA5455", "#DF5560", "#D5566C", "#CA5778",  "#C05884", "#B55990", "#AB5B9C",  "#A15CA7",  "#965DB3",  "#8C5EBF",  "#815FCB",  "#7760D7"])
    plt.xlabel("Time")
    plt.ylabel("Numbers")
    plt.xticks(range(len(time_fdict)), list(time_fdict.keys()))
    tpath = Output+"rtime.png"
    plt.savefig(tpath)
    return tpath

def plot_emoji(file_name):
    emodata = rate_emoji(file_name)
    emo_list = []
    for _,emojis in emodata:
        if len(emojis)>1:
            lemoji = []
            for x in emojis:
                lemoji.extend(list(x))
        else:
            lemoji = list(emojis[0])
        emo_list.extend(lemoji)
    emo_freq_dict = defaultdict( int )
    for emoji in emo_list:
        emo_freq_dict[emoji] += 1

    emo_freq_dict_wrd = {}
    for key in emo_freq_dict.keys():
        name = pemoji.demojize(key).strip(":")
        emo_freq_dict_wrd[name] = emo_freq_dict[key]

    emo_freq_dict_wrd = {k: v for k, v in sorted(emo_freq_dict_wrd.items(), key=lambda item: item[1])}
    keys = list(emo_freq_dict_wrd.keys())
    keys[-10:]

    emo_freq_dict_final = {}
    for key in keys[-10:]:
        emo_freq_dict_final[key] = emo_freq_dict_wrd[key]

    femoji = []
    for key in keys[-10:]:
        emo = pemoji.emojize(":"+key+":")
        femoji.append(emo)
    femoji[::-1]


    fig = plt.figure(figsize=(20, 7))
    fig.suptitle('Top 10 Emoji Used')
    plt.bar(range(len(emo_freq_dict_final)), list(emo_freq_dict_final.values()), align='center', color="black")
    plt.xticks(range(len(emo_freq_dict_final)), list(emo_freq_dict_final.keys()))
    tpath = Output+"remoji.png"
    plt.savefig(tpath)
    return tpath

def get_cloud(file_name):
    _,textcorpous = get_number(file_name)
    cfiles =[]
    i=1
    for key in textcorpous.keys():
        data = textcorpous[key]
        cloud_vec =  " ".join(x for x in data)   
        wordcloud = WordCloud(width = 800, height = 800,background_color ='white', min_font_size = 10).generate(cloud_vec) 
        
        # plot the WordCloud image                        
        plt.figure(figsize = (8, 8), facecolor = None) 
        plt.imshow(wordcloud) 
        plt.axis("off") 
        plt.tight_layout(pad = 0) 
        
        tpath = Output+"wtime"+str(i)+".png"
        i+=1
        plt.savefig(tpath)
        cfiles.append(tpath)

    return cfiles, textcorpous.keys()

def pie_media(file_name):
    _,textcorpous = get_number(file_name)
    labels = ['Word Count', 'Media Count']
    cf = []
    i = 1
    for key in textcorpous.keys():
    
        data = textcorpous[key]
        img = lname[key]
        sizes = [len(data), img]


        fig, ax = plt.subplots()
        ax.pie(sizes, labels= labels, autopct="%1.1f%%")
        ax.axis('equal')
        fig.suptitle(key)

        tpath = Output+"pmed"+str(i)+".png"
        i+=1
        plt.savefig(tpath)
        cf.append(tpath)

    return cf

    

  

    


if __name__ == "__main__":
    file_name = "data/temp.txt"
    get_cloud(file_name)
    plot_emoji(file_name)
    plot_rate_time(file_name)
    plot_rate_date(file_name)
    unq_people(file_name)
    get_url(file_name)
    image_count(file_name)
    get_number(file_name)
    pie_media(file_name)



# %%

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import glob

#Speaker Level Metadata
def read_speakermaps(speakermap_file):
    desc_df = pd.read_csv(speakermap_file, sep="|")
    return desc_df
    
#Speech Files
def read_speech(speech_file):
    final_df = []
    with open(speech_file, 'rb') as f:
        for line in f:
            final_df.append(line.decode(errors='ignore').split("|"))
    
    final_df = pd.DataFrame(final_df)
    final_df = final_df.iloc[:, 0:2]
    final_df = final_df[1:]
    final_df.columns = ["speech_id", "speech"]
    final_df["speech_id"] = final_df["speech_id"].astype(int)
    return final_df
     
#Description of Speech
def read_descr(descr_file):
    desc_df = pd.read_csv(descr_file, sep="|")
    desc_df["date"] = desc_df["date"].astype(str).str.slice(stop=4)
    return desc_df

speeches = glob.glob("speeches_*.txt")
descr_files = glob.glob("descr_*.txt")
speakermap_files = glob.glob("*_SpeakerMap.txt")
speeches = sorted(speeches)
descr_files = sorted(descr_files)
speakermap_files = sorted(speakermap_files)


# In[ ]:


master_data = pd.DataFrame()
for speech, descr, speakermap in zip(speeches, descr_files, speakermap_files):
    speech_df = read_speech(speech)      
    spmap = read_speakermaps(speakermap)
    spmap.drop(columns="district", inplace=True)
    descr_df = read_descr(descr)
    speech_desc = pd.merge(speech_df, descr_df[["speech_id", "date", "speaker", "word_count"]], on="speech_id", how="inner")
    speech_desc_speakermap = pd.merge(speech_desc, spmap,  on="speech_id", how="inner")
    master_data = master_data.append(speech_desc_speakermap)
    


# In[ ]:


#Filtering based on word count
long_speeches = master_data[(master_data["word_count"] > 250) & (master_data["word_count"]<500)]
long_speeches.to_csv("long_speeches.csv", index=False)

#Filtering based on party
df = pd.read_csv("long_speeches.csv")
party_specific = df[df["party"].isin(["D","R"])]

#Filtering based on time/year
party_specific = party_specific[party_specific["date"]>2000]
party_specific.to_csv("filtered.csv", index=None)


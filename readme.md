# Controlled text generation for Political Speeches using PPLM. 

## Group Members
Haritha Anannthakrishnan, Madhumitha Mohan, Madhu Samhitha Vangara, Somya Goel

## Dataset 
Get the dataset from [STANFORD_SPEECH](https://data.stanford.edu/congress_text)

Preprocess and filter the data using 
```bash
python3 Data_Preprocessing.py
```
from the hein bound folder
## Baseline Model

We are training GPT-2 on our speech dataset which can be seen in `Baseline_FineTuned_on_GPT2.ipynb`

## Party Discriminator
In order to classify the partisanship of speeches (D/R), we create a party discriminator script which is a classifier built on a Language Model.

For `Approach 1` we build the classifier on `GPT-2` and for `Approach 2` we build the classifier on `Fine Tuned GPT-2 with Political Speech`

Code can be seen in `Party_Discriminator.ipynb`

For our prompts, use [Prompts](https://drive.google.com/file/d/1hkFTmYzrX6dZiEZfvYw5O7hw2egJRc1U/view?usp=sharing)

## Approach 1 - PPLM
In approach 1, we use three attribute models, first to choose the main
topic as politics, second to choose the sub-topic
within politics (like Business, Healthcare, etc.)
and the third to control the political affiliation
of the speaker (Democratic / Republican).

Code can be seen in `Approach_1.ipynb`

## Approach 2 - PPLM
For our model checkpoint, use [Checkpoint](https://drive.google.com/file/d/1-0v29_O_c2pFa0jTiaR9eVSALVQWBfvB/view?usp=sharing)

We used another approach combining  the advantages of fine-tuning and PPLM, where  GPT-2 was first fine-tuned with the Congressional speeches. We then control this text with Plug and Play architecture, by adding two attribute models on top of the fine-tuned model, one for subtopic BoW, and the other to control political affiliation. 

Code can be seen in `Approach_2.ipynb`

## Metrics Used
We had annotators evaluate our results from Approach 1 & 2.
To get our plots, we use `MetricsCalculation.ipynb`
- Relevance
- Non Redundancy
- Coherence
- Consistency
- Correctness

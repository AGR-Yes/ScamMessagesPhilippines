# **Sino 'To?! _(Who is this?!)_**
### **Taking a Look at Spam Texts in the Philippines**

### 👨‍💻 Author/s: [Anton Reyes](https://www.github.com/AGR-yes)

#### **--** Project Status: **In Progress** **--**

<!--- ![Alt text](image link here) --->

---

## 🗒️ Project Objective
Sino ‘To?! (Who is this?!) is a project that aims to collate and visualize spam texts in the Philippines through datasets made available online. 

### 📓 Files/Folders
| File | Description | Status |
|-------------|-------------|:-------------:|
| `Phase_1.ipynb` |  Contains an EDA, Preprocessing, and Cleaning of the `raw datasets`. | **Complete** |
| `Phase_2.ipynb` |  Cleaned up the `proof.csv` dataset to using NLP and predicted the labels for the unclassified texts. | **Complete** |
| `Phase_3.ipynb` |  Created preliminary visuals and charts to put into the dashboard. Also includes the other information to put for the dashboard's content | **Complete** |
| `app.py` |  The main file that connects all the other pages and files together to complete the dashboard | **In progress** |



### 🧬 Methods Used
* Exploratory Data Analysis (EDA)
* Data preprocessing
* Data cleaning
* Natural Language Processing
* Model training


### 💽 Technologies
* Python
* jupyter
* VSCode
* Google Sheets
* Google Docs


---

## 📁 Project Description
### 📃 Project Overview
This project aims to collate, dig deeper, and visualize datasets of Spam Texts in the Philippines. Backed up by research, the end goal of this project is to create a dashboard that shows data but also tells a story of how data privacy and hacking became a concern during the pandemic.

However, before the creation of the dashboard, data mining and natural language processing techniques were done to clean and extract text data.

### 📃 In Collaboration with *KakakompyuterMoYan!*
KakaKompyuter Mo Yan! Is under the Philippine Internet Archive of Developph. The project aims to explore the Philippine internet and culture while digitally preserving what is seen, heard and put online. 

The Philippine Internet Archive, a newly founded research institute, aims to preserve the idea that the history of the Philippine Internet is the history of the Filipino people. 


### 🗄️ Datasets
***No Webscraping was done***

#### **Scam SMS Report**
> An open-to-all Google Sheet for users to input the numbers of scammers and the type of message that was received (lotto, casino, etc.) The file also contained the number of networks, text message itself and if it contains the name of the receiver. *The link of this dataset will not be shared as it contains a sheet with personal data of other people.*

#### [**Spam SMS**](https://www.kaggle.com/datasets/bwandowando/philippine-spam-sms-messages)
> According to the creator of the dataset, *Bwandowando*, the rise of spam SMS messages increased since the beginning of the COVID-19 pandemic. This dataset consisted of texts that *Bwandowando* received from November 12, 2022, to May 30, 2023. 

#### [**Networks**](https://www.prefix.ph/prefixes/2023-complete-list-of-philippine-mobile-network-prefixes/)
> Contains the available numbers/indicators for a number associated with a network. This was used to help clean up the Google Sheet dataset.

#### [**Tagalog Stopwords**](https://github.com/stopwords-iso/stopwords-tl/blob/master/raw/genediazjr-tagalog.txt)
> A `.txt` file that contains Tagalog stopwords to add and extend the stopwords from the built-in stopwords from the `nltk` library.


### 📝 Problems Faced
* Availability of Philippine-specific datasets
* Handling massive amounts of unclean data
    * One of the datasets was taken from a Google Sheet that was open-to-edit by anyone (Can be edited by those without being logged in to Google). There were standard categories to categorize these reports and there were rules and guidelines on how to use the file. Because it was publicly available, some rules were not followed and it messed with some of the formulas in the file.  
* Categorizing data
    * Due to one of the datasets being unclean, most of the cleaning time was dedicated to re-identifying the phone numbers and re-categorizing the type of spam message, and the column indicating if the text message included the recipient's name.
* Identification of one dataset
    * Since the dataset from Google Sheets was the main dataset for the project, another dataset was found with similar features. However, it lacked a column indicating the type of spam.
* Low accuracy scores

<!---
---

## 🖼️ Project Screenshots (if applicable)
![Alt text](image link)


## 📋 Needs of this project
- insert needs
--->
---

## 🤲🏽 Contributing

First off, thanks for considering to contribute to this project! Contributions are what makes the open-source community such an amazing place to learn, inspire, and create. Any contributions you make will benefit everybody else and are greatly appreciated.

**You can contribute by:**

- Improving documentation
- Implementing a new feature
- Discuss potential ways to improve project
- Adding another graph/plot
- Adding more datasets or Philippine-based data for the model

**Just make sure that your contributions or reports are:**

- *Reproducible*. Include steps to reproduce the problem.
- *Specific*. Include as much detail as possible: which version, what environment, etc.
- *Unique*. Do not duplicate existing opened issues.

---

## 📬 Contact Anton
### [Email](AntonReyes.work@gmail.com) | [LinkedIn](www.linkedin.com/in/anton-r-501b12136/)

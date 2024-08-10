# AI-for-pharmacology
##### The pre-processing of ChEMBL database for molecules was done, where we refine and filter the database for SARS coronavirus 3C-like proteinase, we get to know the different drugs that inhibit the sars coronavirus 3C-like proteinase and make a database out of it

##### I also did exploratory data analysis and converted the data on the basis of the Lipinski's rule, which tells the druglikeness of a compound, we then plotted several plots comparing the active and inactive compounds to all the 4 Lipinski descriptors, and proved statistically using mann-whitney test that the inactive and active types are significantly different.

##### I then took Acetylcholinesterase whose primary job is to break down acetylcholine, a major neurotransmitter, into acetic acid and choline. We then used Padel to calculate the compounds descriptors.

##### I then made a Randon Forest Regresssor fit to the previous data given here as final_3_df.csv and predicted the pIC50 value of the compound which was one of the four Lipnksi Descriptors.

##### There is a streamlit app where you can give your compunds with canonical smiles the app will predict it.

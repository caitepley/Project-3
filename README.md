# Project-3

## Overview
For our project, we are using data from the Dataset of World Digital Library available on the Library of Congress’ website (loc.gov).  The data is available in a .csv format, so our goal was to extract, transform, and load the data into a relational database that can be used to access and analyze the data more readily than its current format. In a relational database format, the item records available in this dataset are more easily updated and are less likely to produce inconsistencies and errors when updating.
	
We chose this topic for our project because we thought it would be a good real world application of a relational database. Libraries often need to go in and update records to add, edit, and delete items, so having the data available in a relational database, rather than an Excel file or .csv file makes these tasks more efficient and accurate. 

## Database Choice
We chose to use a relational database because the data from our source file had some structure to it already. Each item had very similar characteristics and shared most of the features from the dataset, so it made more sense to use a relational database with a rigid structure rather than a non-relational database like NoSQL. To implement the relational database we used Postgres in the form of pgAdmin4 because everyone in the group had already used it before in class and there was no cost associated with it. 

##  Instructions on how to use and interact with the project
The 'Resources' folder contains all of the final .csv files, as well as the source file, and the final tables uploaded into a SLQite database.
#### Source file
- wdl_data_reduced.csv
Note: this is not the complete dataset from the loc.gov website. We had to remove items from the file to make it small enough to upload to GitHub. We also chose to remove some of the columns that we decided were less important to include due to time constraints.
- main_item.csv
Note: this file was used as reference during the project, but does not appear in any code

#### Final .csv files
- Dewey.csv
- col_mapping_new.csv
- creator_id.csv
- creator_type_id.csv
- creator_type_item.csv
- ins_mapping_new.csv
- item_codes.csv
- items.csv (Note: this file has '|' as the delimiter, rather than ',')
- items_csv (this is the same as the items.csv, except that this file has ',' as the delimiter)
- lang_item.csv
- languages_id.csv
- place_id.csv
- place_item.csv
- pub_mapping_new.csv
- subject_id.csv
- subject_item.csv

#### SQLite database
- project_3.sqlite

Outside of the Resources folder (in the main part of the repository) there are the files that contain the ETL workflows to create the final .csv files
#### ETL files
- LOC_new.ipynb
- creator_processing.ipynb
- dewey.ipynb
- items_processing.ipynb
- lang_id_processing.ipynb
- place_id_processing
- subject_processing.ipynb



There is also a processing file that was used to create the SQLite database
#### Code to create SQLite database
- sqlite_processing.ipynb



## Ethical Considerations
The dataset we used for our project did not contain any personally identifiable information (PII) other than the names of the creators of the items included in the dataset. However, since there wasn't any other PII (like contact information, addresses, or social security numbers) we did not to take any special measures to protect the creator's information. Had there been other PII, we would have either had to remove it from the dataset (if it wasn't necessary) or add some security measure(s) to make sure that only authorized individuals would be able to access the information.

## Resources
### Data Source
https://www.loc.gov/item/2020446966/ 
We downloaded the zipped file for [ English language ].

### Outside code

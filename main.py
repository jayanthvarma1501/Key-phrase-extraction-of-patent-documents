import glob
import xml.etree.ElementTree    as ET
import re
from rake_nltk import Rake
import nltk

#!pip install rake-nltk
#python -c "import nltk; nltk.download('stopwords')"
nltk.download('stopwords')
nltk.download('punkt')


# This will connect our main.py to the MySQL Database
import mysql.connector

db = mysql.connector.connect(host = "patentsdb", user = "root", passwd = "1234") #Please insert userID and pwd which you  
                                                                                 #created while pulling the MySQL image 
                                                                                 #from the dockerhub
create_db = "CREATE DATABASE patents" #Please check if the database exists

with db.cursor() as mycursor:       #Queries can be executed using cursor object
    mycursor.execute(create_db)

    
db = mysql.connector.connect(host = "patentsdb", user = "root", passwd = "1234", database="patents")


create_table_query = """
CREATE TABLE patents(
    doc_id VARCHAR(50) PRIMARY KEY,
    key_phrase VARCHAR(10000)
)
"""
with db.cursor() as mycursor:
    mycursor.execute(create_table_query)
    db.commit()


#Please specific the path to the dataset accordingly
dataset = glob.glob(r"dataset/ongoing_100001_120000/*.xml")


def main():
    
    for i in range(len(dataset)):
        
        r = Rake()
        
        #Parsing the XML file
        tree = ET.parse(dataset[i])
        data = tree.getroot()
        doc_id = data.get('file')
        paragraph = data.findall('.//abstract/p')
        total_string = ""
        
        for p in paragraph:
            para = ET.tostring(p)
            decodedpara = para.decode('utf-8')
            modifiedpara = decodedpara.replace("<br />","")
            remodifiedpara = modifiedpara.replace("</p>","")
            remodifiedp = remodifiedpara.replace(re.findall(r'<.+>',remodifiedpara)[0],"").strip()
            total_string = total_string + remodifiedp
            
        total_string= total_string.replace("\n", "")
        total_string = total_string.replace("  ", "")
        
        #Key phrase extraction using Rake object
        r.extract_keywords_from_text(total_string)
        key_phrases_list = r.get_ranked_phrases()[0:10] #Extracting top 10 Key phrases which is user-defined
        key_phrases_string = ", ".join(key_phrases_list)
    # =============================================================================
    #     print('Key phrases')
    #     print(r.get_ranked_phrases()[0:10])
    # =============================================================================
        insert_query = """
        INSERT INTO patents
        (doc_id, key_phrase)
        VALUES ( %s, %s )
        """
        records = [
            (doc_id, key_phrases_string),
        ]
        
        with db.cursor() as mycursor:
            mycursor.executemany(insert_query, records)
            db.commit()
           
        
         #checking for 50 samples
    # =============================================================================
    #     if i == 50:
    #         break
    # =============================================================================
      
    
    #Displaying records from the database table.
      
    select_query = "SELECT * FROM patents LIMIT 3;"
    print('select query')
    with db.cursor() as mycursor:
            mycursor.execute(select_query)
            result = mycursor.fetchall()
            for row in result:
                print(row)
    
    #Terminating the database connection
    mycursor.close()
    db.close()


if __name__ == '__main__':
    main()

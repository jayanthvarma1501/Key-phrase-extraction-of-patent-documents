# Key-phrase-extraction-of-patent-documents


## <div align="center">Description</div>

This repository contains source code for parsing and extracting the Key phrases of the in-house collection of patent documents:

1. The patents stored in the XML documents are parsed, and the abstract of each patent is processed.
2. The RAKE NLTK algorithm extracts the key phrases from the text and stores them in a MySQL database. Each row consists of a document identifier and the extracted Key phrases of a patent.
3. The entire application is wrapped in a docker container. 



## <div align="center">Running in Local computer</div>


<details open>
<summary>Install</summary>

[**Python>=3.6.0**](https://www.python.org/) is required with all
[requirements.txt](https://github.com/jayanthvarma1501/Key-phrase-extraction-of-patent-documents/blob/main/requirements.txt) installed.
<!-- $ sudo apt update && apt install -y libgl1-mesa-glx libsm6 libxext6 libxrender-dev -->

```bash
$ git clone https://github.com/jayanthvarma1501/Key-phrase-extraction-of-patent-documents.git
$ cd Key-phrase-extraction-of-patent-documents
$ pip install -r requirements.txt
```

</details>

<details open>
<summary>Execute</summary>

Replace the database host name to "localhost", and provide your MySQL userID and password in [main.py](https://github.com/jayanthvarma1501/Key-phrase-extraction-of-patent-documents/blob/main/main.py).

</details>

## <div align="center">Running in a Docker Container</div>

1. Install Docker in your local computer.

2. Create volumes for data and configuration of MySQL

```bash
$ docker volume create mysql
$ docker volume create mysql_config
```

3. Create a network that can be used to connect MySQL to Python application

```bash
$ docker network create mysqlnet
```

4. Pull the MySQL image from Dockerhub, and provide a name and password for your database.

```bash
$ docker run --rm -d -v mysql:/var/lib/mysql \
>>   -v mysql_config:/etc/mysql -p 3306:3306 \
>>   --network mysqlnet \
>>   --name patentsdb \
>>   -e MYSQL_ROOT_PASSWORD=1234 \
>>   mysql
```

5. Connect to the MySQL database inside the container and make sure it is running. Type your password created in the previous step.
 
```bash
$ docker exec -ti patentsdb mysql -u root -p
Enter password:
```

6. Build a docker image for your python application.

```bash
$ docker build -t patent .
```

7. Run the docker container and make a connection to the MySQL database.

```bash
$ docker run --network mysqlnet --name rest-server patent
```

In this step, main.py gets executed, and all the key phrases along with document identifiers will be stored in your container's MySQL database. 

</details>

## <div align="center">Further Improvements</div>

The Rake-NLTK algorithm used for Key Phrase extraction comes with some drawbacks. 

1. Firstly, RAKE is domain-independent, and the algorithm works purely on statistical measures. So there is a possibility that some essential Key phrases of a particular domain might not get a higher score than they deserved. Semantic information will not be considered for the ranking.
2. In addition, if there are no stopwords in between a long continuous text, then the whole text is treated as a phrase.
3. Lastly, multi-words with stop words included will be missed. For example, "not trustworthy" phrase will be missed because of "not".

To overcome some of the problems, sophisticated algorithms based on Linguistic Approaches, Graph-based approaches, and Machine Learning approaches can be used. It is mentioned in some sources that "YAKE" algorithm perform better than Rake-NLTK. Replacing MySQL database with a cloud database will be more efficient while processing millions of data. 







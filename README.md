# Key-phrase-extraction-of-patent-documents


## <div align="center">Description</div>

This repository contains source code for parsing and extracting the Key phrases of the in-house collection of patent documents. Firstly, the patents stored in the XML documents are parsed, and the abstract of each patent is extracted. Furthermore, the RAKE NLTK algorithm is used to extract the key phrases from the text and stored them in a MySQL database. Each row consists of a document identifier and the extracted Key phrases of a patent. Lastly, the entire application is wrapped in a docker container.  


## <div align="center">Dataset</div>
 
Download the Dataset Here. [Patents Dataset](https://databricksexternal.blob.core.windows.net/hiring/patents.zip?sp=r&st=2021-10-07T23:09:03Z&se=2021-10-31T08:09:03Z&spr=https&sv=2020-08-04&sr=b&sig=uR36HP3kCEDY9aPc0mvZFzLnblodA9adxQRTYTc6O6M%3D). 


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

Replace the database host name to localhost, and provide your MySQL userID and password in [main.py](https://github.com/jayanthvarma1501/Key-phrase-extraction-of-patent-documents/blob/main/main.py).

</details>

## <div align="center">Running in Docker Container</div>

1. Install Docker in your local computer.

2. Create volumes for data and configuration of mysql 

```bash
$ docker volume create mysql
$ docker volume create mysql_config
```

3. Create a network that can be used to connection MySQL to Python application

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

5. Connect to the running MySQL database inside the container and make sure it is running.
 
```bash
$ docker exec -ti patentsdb mysql -u root -p
```

6. Build a docker image for you python application.

```bash
$ docker build -t patent .
```

7. Run the docker container and make a connection to the MySQL database.

```bash
$ docker run --network mysqlnet --name rest-server patent
```

After this step all the keyphrases along with document identifiers will the stored in the MySQL database of your container.

</details>

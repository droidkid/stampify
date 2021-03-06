# Stampify

Project to automatically convert news / entertainment websites into STAMP
(Stories on AMP) pages.

This is an internship project for Summer 2020.

## Project Requirements

### Set Environment Variables
To get the project working, you will need to set the below mentioned API keys as environment 
variables:

- `GOOGLE_CLOUD_API_KEY` and the value as the base64 encoded string of the API key obtained from the console. For more information on creating and setting API keys, check [Using API Keys](https://cloud.google.com/docs/authentication/api-keys). To get the API key used for this project contact the owner of this repository.

- `FLASK_APP_SECRET_KEY` and the value could be any random generated string. For more information on the usage of this secret key, check official [Flask documentation.](https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions)

### Install Dependencies
- Run the following command to install all the dependencies:

    `$ pip install -r requirements.txt`

    **Note:** You need pip installed in your system for running above command . To install pip, refer [official documentation](https://pip.pypa.io/en/stable/installing/).

- Run the below commands after installing the dependencies

    - Run this command in terminal:
    
        `$ python3 -m spacy download en_core_web_sm`
  
    - Run these commands in the python shell:

        ```
        >>> import nltk
        >>> nltk.download('punkt')
        ```

## How To Run

### Command Line Interface
  
#### Input: 
  
- **url**: Url of the website to be stampified.
- **page_count**: Maximum number of stamp pages to generate.
  
#### Output:
  
  Generated stamp amp-html file will saved in `stampify/output/` directory.
  
#### Command to run:
  
  `$ python main.py 'url' page_count(optional)`
  
  Example:
  
    
    $ python main.py 'https://www.scoopwhoop.com/entertainment/memes-from-dd-ramayan/' 5
    
    $ python main.py 'https://www.scoopwhoop.com/entertainment/memes-from-dd-ramayan/'
    
  
  **For more help, use command:** `python3 main.py -h`

### Flask Server
    
`$ python run_server.py`

The server will be hosted at http://127.0.0.1:5000/

#### API Endpoints:

- `GET /` to see home page for STAMPIFY
- `POST /submit` to provide the details required for stampification.
- `GET /result` to see the output options available.
- `GET /generated_stamp` to show the preview of generated stamp page.

  **Note:** Stamp must be generated by passing stampification details first on `/submit`
  to see generated stamp at this endpoint.

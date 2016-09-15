# nlp-task
This library performs certain NLP tasks, namely coreference resolution of texts, as part of my internship project

## Requirements

* A machine running Linux
* [Python 3](https://www.python.org/downloads/)
* [Java SDK 8](http://www.webupd8.org/2012/09/install-oracle-java-8-in-ubuntu-via-ppa.html)
* [Stanford CoreNLP](http://stanfordnlp.github.io/CoreNLP/index.html#download)

This library was developed using Python 3.5.2, Java SDK 1.8.0_102 and Stanford CoreNLP 3.6.0 running on Lubuntu 16.04.1 LTS.

## Setup

1. Clone the project
1. Install Python dependencies: `$ sudo pip3 install -r requirements.txt`
1. Run the Stanford CoreNLP local server: `$ ./coref/corenlp.sh </path/to/corenlp>`
1. Run the demo program: `$ python3 ./demo.py`

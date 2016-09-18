# nlp-task
This library performs certain natural language processing (NLP) tasks, namely coreference resolution of texts, as part of my internship project.

## Table of Contents

* [Overview](#overview)
* [Requirements](#requirements)
* [Setup](#setup)

## <a name="overview" style="color: #000;"> Overview </a>

In normal contexts, texts contain ambiguous mentions that are of little value to processing and machine learning. An example would be "He was sick." - such a standalone sentence has little meaning; putting it in some form of context such as "John was not at work yesterday. He was sick." allows us to interpret "he" as "John", and the aim of coreference resolution is to resolve "he" into "John" so that meaningful properties can be attributed to "John".

The state of the art in coreference resolution is [Stanford Deterministic Coreference Resolution System](http://nlp.stanford.edu/software/dcoref.shtml). It is integrated with other Stanford NLP tools in [Stanford CoreNLP](http://stanfordnlp.github.io/CoreNLP/) which would be used in this library.

The project involves processing of domain-specific text in the domain of Digital Signal Processing (DSP). To test the approach, some DSP textbooks would be used; the data is available on a server, and the library would include integration with the [server](https://github.com/nathanielove/pdf-server) through the [Python client](https://github.com/nathanielove/pdf-client).

## <a name="requirements" style="color: #000;"> Requirements </a>

* A machine running Linux
* [Python 3](https://www.python.org/downloads/)
* [JDK 8](http://www.webupd8.org/2012/09/install-oracle-java-8-in-ubuntu-via-ppa.html)
* [Stanford CoreNLP](http://stanfordnlp.github.io/CoreNLP/index.html#download)

This library was developed using Python 3.5.2, JDK 1.8.0_102 and Stanford CoreNLP 3.6.0 running on Lubuntu 16.04.1 LTS.

## <a name="setup" style="color: #000;"> Setup </a>

1. Clone the project
1. Install Python dependencies: `$ sudo pip3 install -r requirements.txt`
1. (Optional) Run the Stanford CoreNLP local server: `$ ./coref/corenlp.sh /path/to/corenlp`
1. Run the demo program: `$ python3 ./demo.py`

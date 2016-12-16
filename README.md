# nlp_coref
This library performs certain natural language processing (NLP) tasks, namely coreference resolution of texts, as part of my internship project.

## Table of Contents

* [Overview](#overview)
* [Requirements](#requirements)
* [Setup](#setup)
* [Documentation](#documentation)

## Overview

In normal contexts, texts contain ambiguous mentions that are of little value to processing and machine learning. An example would be "He was sick." - such a standalone sentence has little meaning; putting it in some form of context such as "John was not at work yesterday. He was sick." allows us to interpret "he" as "John", and the aim of coreference resolution is to resolve "he" into "John" so that meaningful properties can be attributed to "John".

The state of the art in coreference resolution is [Stanford Deterministic Coreference Resolution System](http://nlp.stanford.edu/software/dcoref.shtml). It is integrated with other Stanford NLP tools in [Stanford CoreNLP](http://stanfordnlp.github.io/CoreNLP/) which would be used in this library.

The project involves processing of domain-specific text in the domain of Digital Signal Processing (DSP). To test the approach, some DSP textbooks would be used; the data is available on a server, and the library would include integration with the [server](https://github.com/nathanielove/pdf-server) through the [Python client](https://github.com/nathanielove/pdf-client).

## Requirements

* Linux
* [Python 3](https://www.python.org/downloads/)
* [JDK 8](http://www.webupd8.org/2012/09/install-oracle-java-8-in-ubuntu-via-ppa.html)
* [Stanford CoreNLP](http://stanfordnlp.github.io/CoreNLP/index.html#download)

This library was developed using Python 3.5.2, JDK 1.8.0_101 and Stanford CoreNLP 3.6.0 running on Lubuntu 16.04.1 LTS.

## Setup

1. Clone the project
1. Install Python dependencies: `$ sudo pip3 install -r requirements.txt`
1. Edit [config files](#config-files) (`coref/process_config.json` and optionally, `optionals/crawler_config.json`)
1. (Optional, if using the default `coref/process_config.json`) Run the Stanford CoreNLP local server: `$ ./corenlp.sh /path/to/corenlp`
1. Run the demo program: `$ python3 ./demo.py`

## Documentation

### Table of Contents

* [Library structure](#library-structure)
* [Config Files](#config-files)
* [API](#api)

### Library structure

```
coref/
    process.py                  # coref process
    process_config.json         # config file for coref process
    corpus.py                   # corpus operations
optionals/
    clean.py                    # cleaning library
    clean_dsp_terms.txt         # DSP term dictionary, optional for coref process
    clean_english_words.txt     # list of English words, for cleaning library
    svm.py                      # SVM evaluation of corpus
    crawler.py                  # PDF server operations
    crawler_config.json         # config file for PDF server operations
data/                           # misc data
results/
    results.terms               # results file for replace_terms
    results.json                # results file for annotate_txt
    results.corefs              # results file for coref_print
    results.normalized          # results file for normalize
corenlp.sh                      # script to start local CoreNLP server
api.py                          # API wrappers
demo.py                         # demo script
```

### Config Files

#### `coref/process_config.json`

This is the config file to set up Stanford CoreNLP and (optionally) the term model. Default:

```json
{
    "url": "http://localhost:9000",
    "props": {
        "annotators": "tokenize,ssplit,pos,ner,lemma,parse,dcoref",
        "outputFormat": "json"
    },
    "term_model": ""
}
```

Attributes:

| Attribute | Value type | Description 
| --- | --- | ---
| `url` | `string` | URL of the CoreNLP server. Default is the local server.
| `props` | `json` | Properties to be passed into the server. Default is CoreNLP defaults.
| `term_model` | `string` | Text file containing the term model (abbreviation - normalized form pairs). Default is none. 

#### `optionals/crawler_config.json`

This is the (optional) config file to set up pdf-client. More info can be found [here](https://github.com/nathanielove/pdf-client). Default:

```json
{
    "base_url": "http://pdf.bretty.io/api/v1/",
    "auth_class": "HTTPBasicAuth",
    "auth_args": ["user", "password"]
}
```

Attributes:

| Attribute | Value type | Description 
| --- | --- | ---
| `base_url` | `string` | Base URL of API requests. Default is pdf-client default.
| `auth_class` | `string` | Authentication class for all requests. Default is pdf-client default.
| `auth_args` | `list` | Authentication details. Two-element list, first element is username, second is password.

### API

The wrapper for the various functions in this library is provided in `api.py`. These wrappers are called in `demo.py` with `import api`.

| Wrapper | Argument | Function | Return type | Description
| --- | --- | --- | --- | ---
| `annotate(txt, file_out)` | Text to be annotated | `coref.process.Process().annotate_txt` | `json` | Annotate text using CoreNLP
| `coref(txt, file_out)` | Text to be coreferenced | `coref.process.Process().coref_print` | `None` | Print out coreferences
| `normalize(txt, replace_terms, file_out)` | Text to be normalized | `coref.process.Process().normalize` | `string` | Normalize text
| `process(txt)` | Text to be processed | `coref.process.Process().process` | `string` | Process text (coref and normalize) 
| `corpus_clean(path_in, path_out)` | Input and output path for corpus | `coref.corpus.Corpus().corpus_clean` | `None` | Clean a corpus
| `corpus_normalize(path_in, path_out)` | Input and output path for corpus | `coref.corpus.Corpus().corpus_normalize` | `None` | Normalize a corpus
| `clean(txt, debug)` | Text to be cleaned | `optionals.clean.Clean().clean` | `string` | Clean text
| `clean_non_ascii(txt, debug)` | Text to be cleaned | `optionals.clean.Clean([...]).clean` | `string` | Clean only non-ASCII characters from text
| `svm(path)` | Input path for corpus | `optionals.svm.svm_eval` | `None` | SVM to support topic classification of a corpus
| `download_all()` | None | `optionals.crawler.book_download_raw_all` | `None` | Download all raw sections of all books

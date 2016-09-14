# argument of script is path to CoreNLP library
# e.g. ./server.sh /home/nhanh/stanford-corenlp-full-2015-12-09

cd $1
java -Xmx2g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -timeout 3600000 -threads 4
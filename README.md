# Information Retrieval System

This repository contains the implementation of a small and rudimentary information retrieval system.

<b>Information retrieval</b> refers to the process of being able to provide specific information from a large 
amount of unsorted data. Search engines like Google, for example, use the principle of information retrieval, 
which is part of computer science, information science and computational linguistics. This is for example done
by indexing all relevant documents of a collection into an inverted and non-inverted data structure. <b>Vector space
model</b> then is used in which documents and search queries are represented as n-dimensional vectors in an orthogonal
vector space. 

To apply your own search, populate the <b>documents</b> directory with files containing texts which should be 
made searchable. Afterwards, add files containing your search queries into the <b>queries</b> folder. Last but not
least execute the script with <b>python app.py</b>. The program will give you the ten best search results in 
descending order for each search query.
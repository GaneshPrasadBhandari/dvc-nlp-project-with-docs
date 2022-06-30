# Data Prepration Stage

- Convert my data into train and test.tsv in 70:30 ratio

```
data.xml
    |-train.tsv
    |-test.tsv
```
- We are chosing only 3 tags in  the xml data - 1. row ID, 2. title and body 3. Tags 
(stagoverflow tags specific to python)

|Tags|feature names|
|row ID|row ID|
|title and body|test|
|stagoverflow tags|Label - Python|

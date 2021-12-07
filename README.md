# Long Parameter List

---

**Long Parameter List** is a code smell consisting of a method that exceeds the threshold of number of parameters. It's recommended to avoid methods that have more than 3-4 parameters. A solution to overcome this issue is to split the method in submethods or to group all the parameters in an Object that will be passed as argument. 

We propose an approach that uses **Association Rule Learning** to group together parameters that can be associated based on a certain criteria.  
The algorithm used is **Apriori**, under the Unsupervised learning category of Association Rule Learning.  

### Goal

The aim of this project is to scan a source code repository (we used Django for the purpose of testing) and extract all the methods that have more than 3 parameters. Furthermore, we create a DataFrame with all the extracted data and apply **apriori** algorithm to find a association between parameters. This will lead to refactoring the code by creating new objects that will contain the parameters that are more likely to be associated.

### How to use
The project can perform data extraction and processing. Before getting started, you have to define an environment variable:  
```
DIRECTORY_PATH
``` 
which represent the path of source code from where the methods will be extracted.
This work only on Python files, and the parameters we don't take into account are:  
```
- self 
- cls
- *args
- **kwargs
- *
```
Run main.py in order to find the associated rules.

Check the [juputer notebook](notebook/association_rule_learning.ipynb) for **apriori** algorithm explanation.

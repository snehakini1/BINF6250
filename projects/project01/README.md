# Introduction
This repository contains the deliverables for Northeastern University BINF6250 Project 1. The python file contains a script which takes a VCF file and counts the number of occurences of diseases for entries representing rare alleles according to the frequencies from the EXAC database. 
# Pseudocode
Put pseudocode in this box:

```

Initialize an empty dictionary where the keys are strings and the values are integers, to store disease counts.

Open and read the file with UTF-8 encoding. If this fails, exit and raise error.

For each line:

  If the line is empty or begins with '#', return a blank list.

  Remove trailing whitespace, then split the line by '\t' and store elements as a list of fields.
    If the fields list has less than 8 elements, return a blank list.
    Otherwise, extract the 8th element in the list, which is INFO.
  
  Store the elements in fields as a dictionary where the keys are strings and the values are either string or none.
    If the element contains '=', then the key is the string before '=' and the value is the string after '='
    If the element does not contain '=', then the key is the element and the value is none.
  
  From the dictionary of fields, pull the value for the key AF_EXAC. 
    If this value is a placeholder or none, return an empty list.
    If the value cannot be converted to a float, return an empty list. 
    Otherwise, convert the value to float.
  
  If the converted value is above 0.0001, then return an empty list.
  
  Pull the value for the key CLNDN from the dictionary of fields.
    If this value is a placeholder or none, return an empty list.
    Otherwise, split this value by '|' and store it as a list.

  For each element of the CLNDN list, if it is either not_specified or not_provided, do not count it.
  
  Otherwise, append it to a list of diseases.
  
  Return the disease list.

For each disease list (either a list of strings or an empty list), elements that appear are either entered into the dictionary as a key with an initial value of 1 if it is the first time it appears or gets 1 added to its tally for each new occurence.


```

# Successes
We learned how to use GitHub to collaborate with others. We learned how to create pull requests and fork repositories. We became familiar with VCF format and how to parse a file line by line. We also learned how to use the pprint Python module to display a dictionary.

# Struggles
In the beginning, we struggled with using GitHub and had to learn how to fork a repository and ensure that the correct branch was being used. 

# Personal Reflections
## Group Leader
Sneha Kini- Ngoc Linh Nguyen and Thu Thu Han were both great partners. When briefly meeting after class, we all shared our strengths and weaknesses in terms of Python coding and GitHub. We were all a bit unfamiliar with GitHub, but we were quickly able to figure out together how to collaborate using pull requests and merges. Everyone was willing to meet outside of class time to get the project done efficiently, and the work load was shared evenly. When coding the actual project, I was a little slow at first since I had never worked with VCF files before, so figuring out how to parse the file with its unique format was a little tricky at first. We did not face any significant challenges and all steps of the project went relatively smoothly. As the team leader, I tried to set up meeting times to make sure the assignment got done in a timely manner.

## Other member
Ngoc Linh Nguyen - My groupmates were great partners and we were able to coordinate times to collaborate and discuss as well as work separately while keeping each other posted through Teams chat. This project helped me better understand the internal structure of git as well as the collaboration layer of pull requests.

Thu Thu Han - I believe I had great teammates for this project as we were able to communicate really well during our collaborative assignment through the teams meeting and chat. I struggled a little bit with GitHub repositories but my teammates really helped me out with figuring out how to fork a repository of my own. While writing out the test cases, I also learned from my teammate's code such as the type hint indicators in which I have not used them before. I believe that after this project I have gained a deeper understanding of functional file parsing and how to collaboratively work on a Github platform.  

# Generative AI Appendix
We asked the Perplexity-based Course Assistant to clarify assignment instructions as following.
- Could you clarify what "lexer implementation" means in the instructions?

- For test cases, do we do unit tests with fake lines (since the input is hardcoded), and does this imply we should make no assumptions that the file or data is valid?

- May we at least assume that the VCF format is respected, for example that the INFO field's position (8th column), or do we have to validate the structure of the file beyond the file extension and "##fileformat=VCFv4.1"?
 
- Could you clarify what "lexer implementation" means in the instructions?

- For test cases, do we do unit tests with fake data (since the input is hardcoded), and does this imply we should make no assumptions that the file or data is valid, and have built-in checks to potentially return error messages?

- May we at least assume that the VCF format is respected, for example that the INFO field's position (8th column), or do we have to validate the structure of the file beyond the file extension and "##fileformat=VCFv4.1"?


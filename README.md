# Source code of Random Permutation Set
# Introduction
This is the source code for the reproduction of the paper Random Permutation Set^[https://univagora.ro/jour/index.php/ijccc/article/view/4542] with Python. Random Permutation Set was proposed by Deng and is a generalization of the Dempster-Shafer evidence theory. 
# Usage
To successfully run the code, you need to install the Python extension library 'orderdset'. When you are using it, simply run main.py and modify the relevant variables in it.
# Example
The code uses Table 4 in the paper as an example for demonstration

```python
from function import multi_set_fusion
Theta = {'A', 'B', 'C'}
RPS1 = {'A': 0.12, 'B': 0.10, 'AB': 0.15, 'BA': 0.15, 'AC': 0.03, 'ABC': 0.10, 'ACB': 0.25, 'BAC': 0.08, 'CAB': 0.02}
RPS2 = {'A': 0.10, 'B': 0.15, 'AB': 0.07, 'BA': 0.23, 'AC': 0.10, 'ABC': 0.10, 'ACB': 0.05, 'BAC': 0.12, 'CAB': 0.08}
RPS3 = {'A': 0.18, 'B': 0.05, 'AB': 0.15, 'BA': 0.05, 'AC': 0.00, 'ABC': 0.12, 'ACB': 0.30, 'BAC': 0.10, 'CAB': 0.05}
list_RPS = [RPS3, RPS1, RPS2]
result = multi_set_fusion(Theta, 'left', list_RPS)
for item in result:
    print(item)
```
# Citation
@article{ WOS:000754790600003,
Author = {Deng, Yong},
Title = {Random Permutation Set},
Journal = {INTERNATIONAL JOURNAL OF COMPUTERS COMMUNICATIONS \& CONTROL},
Year = {2022},
Volume = {17},
Number = {1},
pages = {},
}



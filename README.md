<div style="text-align:center">
	<img src="images/ji_logo.png" alt="Jilogo" style="zoom:60%;" />
</div>
<center>
	<h2>
		VE444 Networks
	</h2>
</center> 
<center>
	<h3>
		Pure Python Implementation of Classical Network Algos
	</h3>
</center>
<center>
   <h4>
       FA 2020
    </h4> 
</center>

### Abstract

This project is inspired by the coding assignment of course `VE444` to implement some classical networks algos using pure-python effectively and efficiently. Once we open source code of this project and if you want to refer to our work, please follow the Joint Institute’s honor code and don’t plagiarize these codes directly.

### Dependency

Actually, in this project, we only use the pure-python but also two efficient computation package in python called `pandas` and `numpy`, you can run the following instruction to install both two packages in your python environments.

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Algorithms

#### PageRank

To run the algo, here is an example:

```bash
python ./pagerank/pagerank.py --edges ./pagerank/edgelists.txt --max_itr 500 --epsilon 0.001 --beta 0.85
```

For more detailed usage, you can check it with

```bash
python ./pagerank/pagerank.py --help
```

#### Influence Maximization Problem

To run this program, here is an example"

```bash
python ./influence-maximization/hill-climbing.py --edges ./influence-maximization/Employee_Movie_Choices.txt
```

For more detailed usage, you can check it with

```bash
python ./influence-maximization/hill-climbing.py --help
```

### Reference

[1] Zhu, Y., 2020. *Ve444 Networks Hw3.pdf*.

---------------------------------------------------------------

<center>
    UM-SJTU Joint Institute 交大密西根学院
</center>

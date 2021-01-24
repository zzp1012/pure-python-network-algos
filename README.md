<div style="text-align:center">
	<img src="images/ji_logo.png" alt="Jilogo" style="zoom:60%;" />
</div> 
<center>
	<h1>
		Pure Python Implementation of Classical Network Algos
	</h1>
</center>
<center>
   <h2>
       FA 2020
    </h2> 
</center>

### Abstract

This project is inspired by the coding assignment of course network to implement some classical networks algos using pure-python effectively and efficiently. Once we open source code of this project and if you want to refer to our work, please follow the Joint Institute’s honor code and don’t plagiarize these codes directly.

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

To run hill-climbing algo, here is an example:

```bash
python ./influence-maximization/hill-climbing.py --edges ./influence-maximization/Employee_Movie_Choices.txt
```

For more detailed usage, you can check it with

```bash
python ./influence-maximization/hill-climbing.py --help
```

#### Epidemic Model

To simulate SIR model, here is an example:

```bash
python ./epidemic-model/SIR-model.py --beta 0.2 --delta 0.1 --total 1000 --recovery 0 --infected 1 --path ./
```

For more detailed usage, you can check it with

```bash
python ./epidemic-model/SIR-model.py --help
```

---------------------------------------------------------------

<center>
    UM-SJTU Joint Institute 交大密西根学院
</center>

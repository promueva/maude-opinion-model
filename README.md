# Unified Opinion Formation Analysis in Rewriting Logic

Social media platforms have played a key role in weaponizing the polarization
of social, political, and democratic processes. This is, mainly, because they
are a medium for opinion formation. Opinion dynamic models are a tool for
understanding the role of specific social factors on the acceptance/rejection
of opinions because they can be used to analyze certain assumptions on human
behaviors. This [paper](./paper.pdf) presents a framework that uses concurrent
set relations as the formal basis to specify, simulate, and analyze social
interaction systems with dynamic opinion models. Standard models for social
learning are obtained as particular instances of the proposed framework. This
repository contains the implementation in
[Maude](https://maude.cs.illinois.edu/w/index.php/The_Maude_System) of this
framework, that can be used to better understand how opinions of a system of
agents can be shaped. The executable rewrite theory allows for performing 
reachability analysis and, with the aid of
[umaudemc](https://github.com/fadoss/umaudemc), it also possible to perform
probabilistic simulation, and statistical model checking.


## Getting started

The project was tested in [Maude 3.5](https://maude.cs.illinois.edu/wiki/The_Maude_System).
and with [umaudemc](https://github.com/fadoss/umaudemc). 

### Maude files

Next we describe the main Maude files of the implementation. 
See the headers of each file for further information.

- `data`: Sorts and operators for defining a network of agents. 
- `semantics`: Implementation of the non-executable `atomic` rewrite rule
  and the executable rewrite rule `step`. 
- `ex-vaccines`: Example of the social system in [this paper](./paper.pdf)
- `ex-vacc-dgroot`, `ex-vacc-hybrid` and `ex-vacc-gossip`: Instantiation of the
  framework with the DeGroot, Hybrid and Gossip models. Some results of the
  analyses can be found in the end of these files. 
- `formula.quates`: The QuaTEx formulas used for stochastic analysis. 
- `ex-vacc-dgroot-ext-paper` and `ex-vacc-dgroot-ext.maude`:  Analysis with
  DeGroot model extended with different cognitive biases
- `ex-vacc-silence-spi-mem.maude` and `ex-vacc-silence-spi.maude` case studies
  using the  Silence Spiral model (memoryless and history-dependent versions). 

The directory `./exp-gossip` contains the needed files to reproduce the
experiments on the gossip model reported in the paper. 

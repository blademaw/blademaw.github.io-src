Title: Problem Representation in Python, and N-Queens, Revisited
Date: 2021-09-20 12:00
Tags: python, brute-force, simulated-annealing, stochastic
<!-- Summary:  -->

In this first-ever blog post, I want to take the opportunity to talk a little bit about **representing problems** — a process any CS student must first fully internalize before advancing to complex problem solving. To seasoned problem-solvers, the process of problem representation is so natural that us onlookers are quick to take it for granted. In this blog post, I'd like to look at three case studies — two are puzzles from the mathematical gold mine _[The PuzzlOR](http://puzzlor.com/)_, and the third is the infamous N-Queens problem.

## Enumeration and Exhaustion
### Problem 1 — Toy Builder

Imagine you are a [toy builder](http://puzzlor.com/2016-02_ToyBuilder.html) who can build three different toys — **airplanes, helicopters, or cars**. Each of these toys requires resources to make, namely **blue blocks, green rods,** or **red wheels**. Below is a table that summarizes the cost for each toy:

$$ \begin{array} {r|| r r r}
 \textbf{Toy} & \textbf{Blue Blocks} & \textbf{Green Rods} & \textbf{Red Wheels} \\
  \hline \text{Airplane} & 3 & 2 & 1 \\ 
   \text{Helicopter} & 2 & 4 & 1 \\
    \text{Car} & 1 & 2 & 4 \\
     \end{array} $$

Once each toy is crafted, they can be sold (presumably on the luxury toy market) netting the following profits:

$$ \begin{array} {r|| r }
 \textbf{Toy} & \textbf{Profit}  \\
  \hline \text{Airplane} & \$7 \\ 
   \text{Helicopter} & \$8  \\
    \text{Car} & \$5 \\
     \end{array} $$

You begin with **25 blue blocks, 29 green rods,** and **30 red wheels**. The question is, of course,
> What is the maximum profit you can achieve?

You do not have to exhaust your resources. At this point if you have an itch to try your hand at solving the puzzle, feel free to come back and compare approaches.

As the sample space for this problem is quite small, one approach is to just enumerate over all possibilities, i.e., brute force. This cut-and-dried approach is expensive, but is less costly on humans in favor of implementing something like a backtracking algorithm.

When implementing brute-force, there are generally three steps: **(1)** defining the representation of a candidate solution, **(2)** generating all possibilities, and **(3)** finding the candidate that solves our problem.

#### Representation
This problem is relatively easy to represent — we can define a $1\times3$ vector to hold the number of airplanes, helicopters, and cars made, respectively. I.e.,
$$ \text{solution} = (airplanes, \space helicopters, \space cars) $$
is our representation of a candidate solution. 
#### Generating possibilities
First, we need to limit each toy produced in a given solution by the maximum number we can make of that toy. This will be given by the floor of the minimum amount of toys you can make with **any** of the resources available, or
$$ \left \lfloor{\min\left(\frac{c^{(i)}_b}{25}, \frac{c_g^{(i)}}{29}, \frac{c^{(i)}_r}{30} \right)}\right \rfloor $$
where $c^{(i)}_{b,g,r}$ is the cost in blue/green/red resources of toy $i$. We can query these results

{% notebook representing-problems.ipynb cells[2:3] %}

to discover we can create a maximum of $8$ airplanes, $7$ helicopters, and $7$ cars. To enumerate all possibilities, we can use a nested `for` loop to create each vector solution with the maximums in place. We can also cut down on the number of solutions to sift through in the future by axing solutions we know are wrong (if they use excess resources). To do this we can write the following function:

{% notebook representing-problems.ipynb cells[3:4] %}

which ensures after spending all required resources, we didn't over-use any.

#### Identifying the maximum
Next, we can enumerate the solutions and accumulate the *'correct'* ones:

{% notebook representing-problems.ipynb cells[4:5] %}

Let's check how many *'correct'* solutions there are:
{% notebook representing-problems.ipynb cells[5:6] %}
which is next to nothing, so we can more than feasibly solve this problem by checking each solution. To do so, we'll define a cost function and then iterate over all our candidates, bearing in mind that we're *maximizing* cost:

{% notebook representing-problems.ipynb cells[6:7] %}

Revealing our profit-maximizing toy distribution to be **5 airplanes, 2 helicopters**, and **5 cars**, generating **$76** profit in total.


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

Once each toy is crafted, they can be sold (presumably on the luxury toy market) to net the following profits:

$$ \begin{array} {r|| r }
 \textbf{Toy} & \textbf{Profit}  \\
  \hline \text{Airplane} & \$7 \\ 
   \text{Helicopter} & \$8  \\
    \text{Car} & \$5 \\
     \end{array} $$

You begin with **25 blue blocks, 29 green rods,** and **30 red wheels**. The question is, of course,
> What is the maximum profit you can achieve?

You do not have to exhaust your resources. At this point if you have an itch to try your hand at solving the puzzle, feel free to come back and compare approaches.

As the search space for this problem is quite restricted, one approach is to just enumerate over all possibilities, i.e., brute force. This cut-and-dried approach is (potentially very) expensive, but is less costly on us humans to implement in favor of something like a convoluted backtracking algorithm.

When implementing brute-force, there are generally three steps: **(1)** defining the representation of a candidate solution, **(2)** generating all possibilities, and **(3)** finding the candidate that solves our problem. "Solving the problem" means fitting a criteria, in this case the maximum cost-generating combination of toys to build.

#### Representation
This problem is relatively easy to represent — we can define a $1\times3$ vector to hold the number of airplanes, helicopters, and cars made, respectively. I.e.,
$$ \text{solution} \leftarrow (airplanes, \space helicopters, \space cars) $$
is our representation of a candidate solution. 
#### Generating possibilities
First, we need to limit each toy produced in a given solution by the maximum number we can make of that toy. This will be given by the floor of the minimum amount of toys you can make with **any** of the resources available, or
$$ \left \lfloor{\min\left(\frac{c^{(i)}_b}{25}, \frac{c_g^{(i)}}{29}, \frac{c^{(i)}_r}{30} \right)}\right \rfloor $$
where $c^{(i)}_{b,g,r}$ is the cost in blue/green/red resources of toy $i$. We can query these results

{% notebook representing-problems.ipynb cells[2:3] %}

to discover we can create a maximum of $8$ airplanes, $7$ helicopters, and $7$ cars. To enumerate all possibilities, we can use a nested `for` loop to create each vector solution with the maximums in place. We can also cut down on the number of solutions to sift through in the future by axing solutions we know are wrong (if they use excess resources). We can write a function:

{% notebook representing-problems.ipynb cells[3:4] %}

that ensures after spending all required resources, we didn't over-use any.

#### Identifying the solution
Next, we can enumerate the solutions and accumulate the *'correct'* ones with the $O(n^3)$ `for` loop:

{% notebook representing-problems.ipynb cells[4:5] %}

Let's check how many *'correct'* solutions there are:
{% notebook representing-problems.ipynb cells[5:6] %}
which is next to nothing, so we can more than feasibly solve this problem by checking each solution. To do so, we'll define a cost function and then iterate over all our candidates, bearing in mind that we're *maximizing* cost:

{% notebook representing-problems.ipynb cells[6:7] %}

Revealing our profit-maximizing toy distribution to be **5 airplanes, 2 helicopters**, and **5 cars**, generating **$76** profit in total.

Remember, this deterministic approach was only really used because we knew the number of solutions to check was low. If we increased the amount of starting resources, we'd increase the search space combinatorially (possibly leading to a *[combinatorial explosion](https://en.wikipedia.org/wiki/Combinatorial_explosion)*, which, like most kinds of explosions, aren't fun).

### Problem 2 — Port in a Storm
This is the (sadly apparent) [last published puzzle](http://puzzlor.com/2017-02_PortInAStorm.html) from the great *PuzzlOR*, where it is your job to direct **20 boats** at sea to their nearest dock (with a total of **20 dock spaces**) in the midst of a storm.

{% img styled /images/portinastorm_desc.png 450 315 "Twenty boats at sea to be assigned docks" "" "https://puzzlor.com/2017-02_PortInAStorm.html" %}

There are three distinct clusters of boats (labelled above), and we can summarize them as follows:

$$ 
\begin{array} {r r r}
 \quad\quad\quad\quad & \textbf{Distance} & \quad\quad\\
\end{array} \\
\begin{array} {r|| r r r |r}
 \textbf{Cluster} & \text{Dock 1} & \text{Dock 2} & \text{Dock 3} & \textbf{Boats}\\
  \hline 1 & 1 & 3 & 2 & 8\\ 
   2 & 2 & 2 & 1 & 5\\
    3 & 3 & 2 & 1 & 7\\
\end{array}
$$

And the dock spaces are:

$$ 
\begin{array} {r|| r r r}
 \textbf{Dock} & \textbf{Spaces Available} \\
  \hline 1 & 4   \\ 
   2 & 7 \\
    3 & 9  \\
\end{array}
$$

Given the data, the question this time is:
> What is the minimum total distance travelled by all boats?

#### Representation
With this puzzle, it is harder to see how we would go about abstracting a solution to a data structure. Several ideas are possible, some more efficient than others. Take for instance each boat represented by a list with relevant attributes:

$$ 
\text{boat}_i \leftarrow \left[ \left(\text{dist}_1, \text{dist}_2, \text{dist}_3 \right), \space \text{current_dock} \right] 
$$

where $\text{dist}_i$ is the distance of the boat to the $i$-th dock.

This representation is clear and allows querying of the boat's *travelled distance,* or *cost* via $\verb|boat|_i\verb|[0][1]|$. However, we must consider that twenty boats in an array means $20\cdot4=100$ total elements in memory, and it's easy to see that many boats are essentially the same array, with the `current_dock` being the only altered attribute.

Okay, what about a different data structure? Since `current_dock` is the only variable attribute, can we encode that data without constantly altering it in some fashion? One possible representation is to transform `current_dock` a position in an array:

$$ \text{docks} \leftarrow \left[ \left[ \text{boats}\right], \space \left[\dots\right],\space \left[\dots\right] 
    \right] 
$$

where $\text{docks}[i]$ stores all boats docked at the $i$-th dock. In this representation, boats would change destinations via array swapping, which is possibly even more costly given the nature of array concatenation and slicing.

As explicit as this representation is, it still suffers from the redundancy issues of the boat representation, and its practical implementation must constantly ensure $\text{len}(\text{docks}[i])\le\text{dock_spaces}_i$, which is at least three comparisons per iteration.

Let's move on from this nested array approach. In a *single array,* can we somehow encode the assigned dock of a boat and identify its cluster at the same time? Unsurprisingly, the answer is yes — probably in many ways.

Let's move forward with a representation that makes use of the position in the array to signify dock number, and integers 1–3 to signify boat cluster. Here is a sample solution that assigns boats to each dock in sorted order:
{% img /images/portinastorm_rep.png 500 78 "" "Problem representation for Problem 2" %}

Functionally, in this array there are three 'hidden' sets — dock one, two, and three. Within these sets, order does not matter (this will *drastically* cut down on the search space later), and while we do have repeated elements, we can use these to index cost-distance arrays when evaluating a solution.

#### Generating possibilities
We can think of our representation as a result of *choosing* different individual boats from a pool of available boats, one dock at a time. We can define the algorithm for generating a given solution as

> 1. Define a pool of available boats, $S$
> 2. Choose $4$ boats from $S$, let this be the set $D_1$
> 3. Choose $7$ boats from $\{S-D_1\}$, let this be the set $D_2$
> 4. The remaining $9$ boats in dock three will be $D_3=\{S-D_1-D_2\}$

Of course, the real algorithm must enumerate all choices of `(2)` and then `(3)`.

In Python, we can define our pool and algorithm as such:

{% notebook representing-problems.ipynb cells[8:10] %}

Let's check how many solutions we have in total:

{% notebook representing-problems.ipynb cells[10:11] %}

Which is, again, not that many.

#### Identifying the solution
A cost function for the problem given our representation is easy — we simply iterate over each boat in each dock slice, applying the appropriate costs as distances:

{% notebook representing-problems.ipynb cells[11:12] %}

We can then iterate over all solutions and look for the minimum cost/distance travelled by a configuration of boats in docks:

{% notebook representing-problems.ipynb cells[12:13] %}

And we find the minimum distance to be **31**, and it just so happened to be that the minimum distance yielding configuration was our default case!

## Exhaustion due to Enumeration
Of course, we should note **the only reason we could feasibly solve the previous problems** with **brute-force** was because of the small number of solutions to verify, and the guarantee our parameters/arguments were fixed.

But what happens when our problem is more general, or simply has too many possibilities to check?

### Problem 3 — The N-Queens Problem


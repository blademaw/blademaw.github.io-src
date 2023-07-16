Title: Solving Logic Puzzles in Prolog
Date: 2023-07-01 00:00
Tags: prolog, programming, logic
slug: prolog-puzzles

<!-- PELICAN_BEGIN_SUMMARY -->

<figure class="styled"><img class="styled" src="/images/futoshiki_splash.png" width="250" height="250" title="A solved 7x7 Futoshiki board." alt="A solved 7x7 Futoshiki board."><figcaption>A solved 7x7 futoshiki board.</figcaption></figure>

Recently, I came across this fun brainteaser on <a href="https://mathematicaloddsandends.wordpress.com/2022/01/01/a-brainteaser-involving-prime-sums-and-differences/" target="_blank">Kenneth Tay's blog</a>. The problem was:

> Write the numbers 1 to 14 around a circle so that the sum and difference of every pair of adjacent numbers is prime.

This puzzle is a classic constraint satisfaction problem, in which given a set of objects (numbers, in this case), a domain of values (here, positions), and a set of constraints (the fact that sums/differences of neighbors must be prime), we want to find a *complete* and *consistent* evaluation of the variables and values that satisfy the constraints.

<!-- PELICAN_END_SUMMARY -->

{% notebook prolog-puzzles.ipynb cells[0:] %}

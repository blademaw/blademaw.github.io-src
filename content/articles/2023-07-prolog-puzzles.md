Title: Solving Logic Puzzles in Prolog
Date: 2023-07-01 00:00
Tags: prolog, programming, logic
slug: prolog-puzzles

<!-- PELICAN_BEGIN_SUMMARY -->

<figure class="styled"><img class="styled" src="/images/futoshiki_splash.png" width="250" height="250" title="A solved 7x7 Futoshiki board." alt="A solved 7x7 Futoshiki board."><figcaption>A solved 7x7 Futoshiki board.</figcaption></figure>

Recently, I came across this fun brainteaser on <a href="https://mathematicaloddsandends.wordpress.com/2022/01/01/a-brainteaser-involving-prime-sums-and-differences/" target="_blank">Kenneth Tay's blog</a>:

> Write the numbers 1 to 14 around a circle so that the sum and difference of every pair of adjacent numbers is prime.

In this blog post, I want to use this riddle as an example to show how _easy_ it can be to solve logic puzzles out-of-the-box with Prolog: a constraint logic programming language. Alongside this riddle, I'll cover two additional games that aren't as easy, and showcase how Prolog can allow for intuitive, declarative solutions to nontrivial problems.

<!-- PELICAN_END_SUMMARY -->

{% notebook prolog-puzzles.ipynb cells[0:] %}

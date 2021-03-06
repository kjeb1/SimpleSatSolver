
## satSolver.py
This very simple <a href="https://en.wikipedia.org/wiki/SAT_solver">SAT solver</a> is based on one-sided <a href="https://en.wikipedia.org/wiki/Sequent_calculus">sequent calculus</a>. It is made for my own educational purpose, and I hope the logic are correct. This is "pure" sequent calculus, no optimization whatsoever.

We use "proof by contradiction". The axiom is then A and ¬A. We know that if all leaf sequents 
are axioms, then the formula is valid; otherwise, it is invalid. That means A is satisfiable 
iff ¬A is invalid. By using refutation calculus we can say:
- If at least one branch leaf is an axiom: the formula is satisifiable
- If all branch leafs are non-axioms: the formula is unsatisifiable

Since we start with a formula in conjunctive normal form (CNF), we only need to deal with the ∨-rule and the ∧-rule.
We will need to split branches for the ∨, but for ∧ we will only iterate through them.

For interpretation, we know that at least one non-axiom leaf branch will satisfy the formula.
So a interpretation that satisfy that leaf branch will be enough. The interpretation of
the rest leaf branches doesn’t matter.

In the Python program the literals will be strings in lowercase or uppercase characters (a silly idea, actually).
Lowercase is non negated, and uppercase is negated. This may not be memory efficient, but
easy to debug. The clause set will be a list of lists.<br>
Example<br>
Formula: p∧(¬p∨r)∧q<br>
CNF: {{p,{¬p, r},{¬q},{q}}<br>
Python: [[′p′],[′P′,′r′],[′Q′],[′q′]]<br>

The interpretation will be a dictonary with T for true and F for false.<br>
Print out eksample:<br>
I(p) = True and I(r) = False<br>
Python: {′p′:′T′,′r′:′F′}<br>

The literals are restricted to a-z/A-Z.

To solve ¬p∧(¬p∨ ¬q∨r)∧q, run satSolver([[’P’], [’P’,’Q’,’r’], [’q’]])<br>
See tests in tester.py


## resolutionSatSolver.py
I decided to make a satsolver based on <a href="https://en.wikipedia.org/wiki/Resolution_(logic)">resolution calculus</a> as well. It turns out to be a little 
more simplier to implement (fewer lines with code). But without any optimization, it uses a ridiculous 
amount of memory if we have more than a few clauses.<br>
See tests in resolutionTester.py

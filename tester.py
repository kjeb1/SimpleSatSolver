
from satSolver import satSolver

# Tester program
# First print the formula with an indication if it is satisfiable or not
# literals in lower case are non negated.
# Literals in upper case are negated.
# The clause set is a list of lists (not sets)
#
# Eks: satSolver([['p','q','r'],['p','q','R'],['P']])

print()
print("¬p : sat")
satSolver([['P']])

print()
print("p : sat")
satSolver([['p']])

print()
print("¬p ∨ p : sat")
satSolver([['P', 'p']])

print()
print("¬p ∧ p : unsat")
satSolver([['P'],['p']])

print()
print("p ∧ q ∧ r : sat")
satSolver([['p'], ['q'], ['r']])

print()
print("¬p ∨ -q ∨ ¬r : sat")
satSolver([['P','Q','R']])

print()
print("r ∧ (p ∨ ¬r) ∧ q : sat")
satSolver([['r'], ['p','R'], ['q']])

print()
print("p ∧ (¬p ∨ ¬q) ∧ q : unsat")
satSolver([['p'], ['P','Q'], ['q']])

print()
print("¬p ∧ (¬p ∨ ¬q ∨ r) ∧ q : sat")
satSolver([['P'], ['P','Q','r'], ['q']])

print()
print("(p ∨ q ∨ r) ∧ (p ∨ q ∨ ¬r) : sat")
satSolver([['p','q','r'],['p','q','R']])

print()
print("(p ∨ q ∨ r) ∧ (p ∨ q ∨ ¬r) ∧ ¬p ∧ ¬q : unsat")
satSolver([['p','q','r'],['p','q','R'],['P'],['Q']])

print()
print("(¬p ∨ q) ∧ (p ∨ q) ∧ (¬p ∨ ¬q) ∧ (p ∨ ¬q) : unsat")
satSolver([['P','q'],['p','q'],['P','Q'],['p','Q']])

print()
print("(¬p ∨ q ∨ r) ∧ (p ∨ ¬q ∨ r ) ∧ (¬p ∨ ¬q ∨ ¬r) : sat")
satSolver([['P','q','r'],['p','Q','r'],['P','Q','R']])

print()
print("(p ∨ q ∨ r) ∧ (p ∨ q ∨ ¬r) ∧ (p ∨ ¬q ∨ r) ∧ (¬p ∨ q ∨ r) ∧ (p ∨ ¬q ∨ ¬r) ∧ (¬p ∨ ¬q ∨ r) ∧ (¬p ∨ ¬q ∨ ¬r) : sat")
satSolver([['p','q','r'],['p','q','R'],['p','Q','r'],['P','q','r'],['p','Q','R'],['P','Q','r'],['P','Q','R']])

print()
print("(p ∨ q ∨ r ∨ s) ∧ (p ∨ q ∨ r ∨ ¬s) ∧ (p ∨ q ∨ ¬r ∨ s) ∧ (p ∨ ¬q ∨ r ∨ s) ∧ (¬p ∨ q ∨ r ∨ s) ∧ (p ∨ q ∨ ¬r ∨ ¬s) ∧ (p ∨ ¬q ∨ ¬r ∨ ¬s) ∧ (¬p ∨ ¬q ∨ ¬r ∨ ¬s) : sat")
satSolver([['p','q','r','s'],['p','q','r','S'],['p','q','R','s'],['p','Q','r','s'],['P','q','r','s'],['p','q','R','S'],['p','Q','R','S'],['P','Q','R','S'],])

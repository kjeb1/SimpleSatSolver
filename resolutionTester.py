
from resolutionSatSolver import resolutionSatSolver

# Tester program for resolutionSatSolver
# First print the formula with an indication of satisfiable or not
# literals in lower case are non negated.
# Literals in upper case are negated.
# The clause set is a list of lists (not sets)
#
# Eks: resolutionSatSolver([['p','q','r'],['p','q','R'],['P']])

print()
print("¬p : sat")
resolutionSatSolver([['P']])

print()
print("p : sat")
resolutionSatSolver([['p']])

print()
print("¬p ∨ p : sat")
resolutionSatSolver([['P', 'p']])

print()
print("¬p ∧ p : unsat")
resolutionSatSolver([['P'],['p']])

print()
print("p ∧ q ∧ r : sat")
resolutionSatSolver([['p'], ['q'], ['r']])

print()
print("¬p ∨ -q ∨ ¬r : sat")
resolutionSatSolver([['P','Q','R']])

print()
print("r ∧ (p ∨ ¬r) ∧ q : sat")
resolutionSatSolver([['r'], ['p','R'], ['q']])

print()
print("p ∧ (¬p ∨ ¬q) ∧ q : unsat")
resolutionSatSolver([['p'], ['P','Q'], ['q']])

print()
print("¬p ∧ (¬p ∨ ¬q ∨ r) ∧ q : sat")
resolutionSatSolver([['P'], ['P','Q','r'], ['q']])

print()
print("(p ∨ q ∨ r) ∧ (p ∨ q ∨ ¬r) : sat")
resolutionSatSolver([['p','q','r'],['p','q','R']])

print()
print("(p ∨ q ∨ r) ∧ (p ∨ q ∨ ¬r) ∧ ¬p ∧ ¬q : unsat")
resolutionSatSolver([['p','q','r'],['p','q','R'],['P'],['Q']])

# Below will use a ridiculous amount of memory...
"""
print()
print("(¬p ∨ q) ∧ (p ∨ q) ∧ (¬p ∨ ¬q) ∧ (p ∨ ¬q) : unsat")
resolutionSatSolver([['P','q'],['p','q'],['P','Q'],['p','Q']])

print()
print("(¬p ∨ q ∨ r) ∧ (p ∨ ¬q ∨ r ) ∧ (¬p ∨ ¬q ∨ ¬r) : sat")
resolutionSatSolver([['P','q','r'],['p','Q','r'],['P','Q','R']])

print()
print("(p ∨ q ∨ r) ∧ (p ∨ q ∨ ¬r) ∧ (p ∨ ¬q ∨ r) ∧ (¬p ∨ q ∨ r) ∧ (p ∨ ¬q ∨ ¬r) ∧ (¬p ∨ ¬q ∨ r) ∧ (¬p ∨ ¬q ∨ ¬r) : sat")
resolutionSatSolver([['p','q','r'],['p','q','R'],['p','Q','r'],['P','q','r'],['p','Q','R'],['P','Q','r'],['P','Q','R']])

print()
print("(p ∨ q ∨ r ∨ s) ∧ (p ∨ q ∨ r ∨ ¬s) ∧ (p ∨ q ∨ ¬r ∨ s) ∧ (p ∨ ¬q ∨ r ∨ s) ∧ (¬p ∨ q ∨ r ∨ s) ∧ (p ∨ q ∨ ¬r ∨ ¬s) ∧ (p ∨ ¬q ∨ ¬r ∨ ¬s) ∧ (¬p ∨ ¬q ∨ ¬r ∨ ¬s) : sat")
resolutionSatSolver([['p','q','r','s'],['p','q','r','S'],['p','q','R','s'],['p','Q','r','s'],['P','q','r','s'],['p','q','R','S'],['p','Q','R','S'],['P','Q','R','S'],])
"""

# -*- coding: utf-8 -*-

# Simple SAT solver based on (one-sided) sequent calculus
#
# literals in lower case are non negated.
# Literals in upper case are negated.
# The clause set is a list of lists (not sets)
#
# Eks: satSolver([['p','q','r'],['p','q','R'],['P']])
#

## Detailed description:
# The function sequentCalculus() takes one parameter witch is a list of branches (named
# branches). The first iteration it will only contain one branch - the root. The main loop will go
# through all the branches, and work up to the leaf for each branch at a time. For each time we
# do a split of a clause, the new branch will be added to the list of branches and taken care of in
# a later iteration. For each branch we loop through each clause. One at a time, each clause will
# be splited, and the clause will be deleted. If the clause has more than two literals, it will
# split into one literal and one new clause. The new clause or literal will be added together with the
# rest of the clauses as a new branch. For each clause split it checks if the branch has become a
# leaf. If so, it checks if the leaf is not an axiom. Then it will stop the branch loop and return the
# branch containing the leaf literals. To check for axioms, it checks if the difference in ASCII
# value is 32.
#
# The function interpretation() will loop through the given list of clauses containing the
# leaf literals. If a literal is in uppercase, it needs to be interpretered as false, and true for low-
# ercase. The rest of the literals can be either true or false. So it goes through the original given
# root branch and add in missing literals with interpretation as true.


# Main function
def satSolver(clauseSet):
    baseclauseSet = clauseSet.copy() # Take a copy for nice printing at the end
    leafBranch = sequentCalculus([clauseSet])
    if leafBranch is None:
        print("%s is unsatisfiable" % baseclauseSet)
    else:
        print("%s is satisfiable" % baseclauseSet)
        interpretation(leafBranch, baseclauseSet)


# A satisfying interpretation will be a interpretation that satisfy a leaf that is not an axiom 
# The rest of the literals doesn't matter
def interpretation(leafBranch,baseclauseSet):
        interpretation = {}
        for leaf in leafBranch:
            for literal in leaf:
                if literal.isupper():
                    interpretation[literal.lower()] = 'F'
                else:
                    interpretation[literal] = 'T'
        # At this point we have interpretered enough literals to conclude.
        # But if there are more literals, we nead to give them a value, F or T (it doesn't matter)
        # So, we then just loop through the base clause set and pick up missing literals and set them to T
        for branch in baseclauseSet:
            for clause in branch:
                for literal in clause:
                    if literal.lower() not in interpretation:
                        interpretation[literal.lower()] = 'T' # Just set the rest to True
        print("Interpretation ", interpretation)


# Check if a clause set/branch is an axiom
# Loop through the clauses looking for clauses with only one literal
# If we find clauses with only one literal, try to find another literal witch is the same with negation
def isAxiom(clauseSet):
    for clause in clauseSet:
        if len(clause) == 1: # This clause is one literal
            for clauseAx in clauseSet:
                if len(clauseAx) == 1: # Here is another clause witch is only one literal
                    if abs(ord(clause[0]) - ord(clauseAx[0])) == 32: # If the ASCII distance is 32 we have a sibling
                        return True
    return False


# Check if all clauses is one literal
def isLeaf(clauseSet):
    for clause in clauseSet:
        if len(clause) > 1:
            return False
    return True


# The function takes a list of branches. One branch is one clause set
# The first iteration it will only have one branch. The list will grow when splitting
def sequentCalculus(branches):

    # Loop through all branches. Will grow in the loop
    for branch in branches:

        # Loop through each clause in the branch and split one by one clause
        for clause in branch:

            # Split the clause with the V-rule
            branch.remove(clause) # Remove the clause before splitting it
            newBranch = branch.copy() # Copy the clauseSet for the new branch
            branch.insert(0,[clause[0]]) # Add back the one literal from the splited clause

            # Make the new branch with the rest (if any) of the splitted clause
            if len(clause) > 1: # If it isn't anything left in the clause, we have a leaf
                newClause = clause.copy() # Copy the clause for the new branch
                newClause.remove(clause[0]) # Remove the literal that we have in the other branch
                newBranch.insert(0,newClause) # Add the rest if the splitted clause to the new branch
                branches.append(newBranch) # Add the new branch back to the list of branches

            # Check if the branch is a leaf branch that is not an Axiom, then it is satisfiable
            if isLeaf(branch):
                if not isAxiom(branch):
                    return branch

    # No leafs was Axioms, then it is unsatisfiable
    return None

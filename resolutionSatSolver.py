# -*- coding: utf-8 -*-

# Simple SAT solver based on resolution caluclus

# Litterals in lower case are non negated.
# Literals in upper case are negated.
# The clauseset is a list of lists (not sets)
#
# Eksample:
# Clause set: {{¬p, q}, {¬q, r}, {p}, {¬r}}
# resolutionSatSolver([[P, q], [Q, r], [p], [R]])

def resolutionSatSolver(clauseset):
    clauseNumber = 0
    clauseResolveNumber = 0
    baseClauseset = clauseset.copy()

    # Main loop:
    # Loop through the clauseset
    for clause in clauseset:
        clauseNumber += 1 # Keep track of wich clause we are working on

        # Loop through all litterals in current clause
        for litteral in clause: 
            clauseResolveNumber = 0

            # Resolve loop:
            # For each litteral, look for a resolution in all other clauses. 
            for clauseResolve in clauseset:
                clauseResolveNumber += 1 # Keep track of wich clause we are resolving against
                if clauseResolveNumber != clauseNumber: # Dont check against the clause it selves

                    # Now, loop through the litterals in the resolving clause
                    for litteralResolve in clauseResolve:

                        # Compare litterals. If the ASCII space between two litterals is 32 then it is a lower/upper pair 
                        if abs(ord(litteral) - ord(litteralResolve)) == 32: 

                            # Take out the resolvent
                            resolvent = clause.copy()
                            resolvent.remove(litteral)
                            resolventResolve = clauseResolve.copy()
                            resolventResolve.remove(litteralResolve)

                            # If both clauses are empty, then we are finnished!
                            if len(resolvent) == 0 and len(resolventResolve) == 0:
                                print("%s is unsatisfialble" % (baseClauseset))
                                return

                            # Add back the new resolvents
                            clauseset.append(resolvent + resolventResolve)

    print("%s is satisfiable" %(baseClauseset))


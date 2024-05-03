class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables  # list of variables
        self.domains = domains  # dict of domains for each variable
        self.constraints = constraints  # list of constraints (functions)

    def is_consistent(self, variable, assignment):
        """Check if the current assignment is consistent."""
        for constraint in self.constraints:
            if not constraint(assignment):
                return False
        return True

    def backtrack(self, assignment):
        """Backtrack search to find a solution."""
        if len(assignment) == len(self.variables):
            return assignment

        unassigned = [v for v in self.variables if v not in assignment]
        first = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            if self.is_consistent(first, local_assignment):
                result = self.backtrack(local_assignment)
                if result is not None:
                    return result
        return None

    def solve(self):
        """Solve the CSP."""
        return self.backtrack({})

# Example CSP: Sudoku
def sudoku_constraints(assignment):
    """Define constraints for Sudoku."""
    for i in range(9):
        row = [assignment.get((i, j)) for j in range(9) if (i, j) in assignment]
        col = [assignment.get((j, i)) for j in range(9) if (j, i) in assignment]
        if len(set(row)) != len(row) or len(set(col)) != len(col):
            return False
    return True

# Variables and domains for a simple 4x4 Sudoku
variables = [(i, j) for i in range(4) for j in range(4)]
domains = {var: list(range(1, 5)) for var in variables}
constraints = [sudoku_constraints]

# Creating CSP instance
sudoku_csp = CSP(variables, domains, constraints)
solution = sudoku_csp.solve()
print("Sudoku Solution:", solution)
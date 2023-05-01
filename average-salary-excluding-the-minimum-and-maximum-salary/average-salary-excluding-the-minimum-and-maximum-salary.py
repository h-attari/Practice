class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(min(salary))
        salary.remove(max(salary))
        avg_salary = sum(salary) / len(salary)
        return avg_salary
from airflow.sdk import dag, task

@dag
def branch():
    @task
    def a():
        return 1
    
    @task.branch
    def b(val:int):
        if val ==1:
            return "equal_1"
        else:
            return "different_1"

    @task
    def equal_1(val: int):
        print("Value is equal to {val}")

    @task
    def different_1(val: int):
        print("Value is different from {val}")

    val = a()
    b(val) >> [equal_1(val), different_1(val)]

    

branch()
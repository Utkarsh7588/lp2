n = int(input("Enter the number of jobs: "))
profit = []
jobs = []
deadline = []

for i in range(n):
    p, j, d = input("Enter job {}: ".format(i+1)).split()
    profit.append(int(p))
    jobs.append(j)
    deadline.append(int(d))

profitNJobs = list(zip(profit, jobs, deadline))
profitNJobs = sorted(profitNJobs, key=lambda x: x[0], reverse=True)

max_deadline = max(deadline)  # Find the maximum deadline

slot = [0] * (max_deadline + 1)  # Initialize the slot list with enough elements
profit = 0
ans = ['null'] * (max_deadline + 1)  # Initialize ans list with enough elements

for i in range(len(jobs)):
    job = profitNJobs[i]
    # check if slot is occupied
    for j in range(job[2], 0, -1):
        if slot[j] == 0:
            ans[j] = job[1]
            profit += job[0]
            slot[j] = 1
            break

print("Jobs scheduled buddy:", ans[1:])
print("Total profit:", profit)

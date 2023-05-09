def job_scheduling(n, jobs):
    # sort jobs in decreasing order of profit
    jobs.sort(key=lambda x: x[2], reverse=True)

    # initialize variables
    result = [-1] * n
    slots = [False] * n

    # iterate over jobs
    for i in range(n):
        # find the maximum available slot for the current job
        for j in range(min(n, jobs[i][1]) - 1, -1, -1):
            if not slots[j]:
                result[j] = jobs[i][0]
                slots[j] = True
                break

    return result

# take input from user
n = int(input("Enter the number of jobs: "))
jobs = []
for i in range(n):
    profit, deadline = map(int, input("Enter job {}: ".format(i+1)).split())
    jobs.append((i+1, deadline, profit))

# find job sequence
sequence = job_scheduling(n, jobs)

# print job sequence
print("Job sequence: ", sequence)

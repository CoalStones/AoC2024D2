# Constants
INCREASING = 1
DECREASING = 2
NEITHER = 3

if __name__ == "__main__":
    
    # gathering the input data
    data = []
    with open("input.txt") as file:
        while line := file.readline().strip():
            line = line.split(" ")
            report = []
            for datum in line:
                report.append(int(datum))
            data.append(report)
    # for report in data:
    #     print(report)
    
    safeReports = 0
    for report in data:
        # put an incrementer to count how many fails there were per report, if more than one fail it, if there are 0 or 1 fails it is a safe report
        failsPerLevel = 0
        pattern = 0
        # print(len(report))
        for i in range(len(report) - 1): # -1 here because there's nothing after the last level
            # compare each level in the report to see if they are increasing or decreasing
            # print("comparing " + str(report[i]) + " to " + str(report[i+1]) + " in report " + str(report))
            if i == 0:
                if report[i] < report[i+1] and abs(report[i] - report[i+1]) <= 3:
                    pattern = INCREASING
                elif report[i] > report[i+1] and abs(report[i] - report[i+1]) <= 3:
                    pattern = DECREASING
                else:
                    pattern = NEITHER
                    failsPerLevel += 1
                    # print("Fail number " + str(failsPerLevel) + " at level " + str(i) + " in report " + str(report))
                    if failsPerLevel > 1:
                        break
            else:
                if report[i] < report[i+1] and abs(report[i] - report[i+1]) <= 3 and pattern != DECREASING and pattern != NEITHER:
                    pattern = INCREASING
                elif report[i] > report[i+1] and abs(report[i] - report[i+1]) <= 3 and pattern != INCREASING and pattern != NEITHER:
                    pattern = DECREASING
                else:
                    pattern = NEITHER
                    failsPerLevel += 1
                    # print("Fail number " + str(failsPerLevel) + " at level " + str(i) + " in report " + str(report))
                    if failsPerLevel > 1:
                        break
        
        if failsPerLevel <= 1:
            print("Safe report: " + str(report) + " with " + str(failsPerLevel) + " fails")
            safeReports += 1
            # print("Safe report: " + str(report))
    
    print(safeReports)
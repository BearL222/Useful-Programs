report = open("report.txt", "r")

outputLines = []
for line in report.readlines():
    tmp = line.strip().strip("* ")
    if tmp.startswith("https") or tmp.startswith("http") and len(outputLines) != 0:
        outputLines[-1] = outputLines[-1][:len(outputLines[-1]) - 1] + " " + tmp + "\n"
    else:
        outputLines.append(tmp + "\n")
report.close()

output = open("output.txt", "w")
output.writelines(outputLines)
output.close()
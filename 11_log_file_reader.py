
# Log File Reader Program

filename = input("Enter log file name: ")

try:

    with open(filename, "r") as file:

        lines = file.readlines()

    info_count = 0
    warning_count = 0
    error_count = 0

    print("\n===== LOG FILE CONTENT =====")

    for line in lines:

        print(line, end="")

        if "INFO" in line.upper():
            info_count += 1

        elif "WARNING" in line.upper():
            warning_count += 1

        elif "ERROR" in line.upper():
            error_count += 1

    print("\n\n===== LOG SUMMARY =====")

    print("Total Lines:", len(lines))
    print("INFO Count:", info_count)
    print("WARNING Count:", warning_count)
    print("ERROR Count:", error_count)

except FileNotFoundError:

    print("File not found.")


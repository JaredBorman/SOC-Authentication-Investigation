failed_attempts = {}

with open("authentication_logs.txt", "r") as file:
    for line in file:
        if "FAILED" in line:
            parts = line.split("|")
            user = parts[2].strip().replace("User: ", "")
            ip = parts[3].strip().replace("Source IP: ", "")

            key = (user, ip)

            if key not in failed_attempts:
                failed_attempts[key] = 0

            failed_attempts[key] += 1

print("Failed Login Summary")
print("--------------------")

for (user, ip), count in failed_attempts.items():
    print(f"User: {user} | IP: {ip} | Failed Attempts: {count}")

    if count >= 5:
        print("ALERT: Multiple failed login attempts detected.")

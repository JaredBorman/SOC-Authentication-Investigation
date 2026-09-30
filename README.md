# SOC Authentication Investigation

## Overview

This project is a simulated Security Operations Center (SOC) investigation into suspicious authentication activity involving an administrator account.

The investigation focuses on identifying unusual login behavior, analyzing activity after authentication, identifying indicators of interest, and determining whether the activity may represent unauthorized access and potential data exfiltration.

## Investigation Scenario

The investigation began after multiple failed authentication attempts were observed against the administrator account.

Five consecutive failed login attempts were followed by a successful authentication from the same external IP address, `185.44.72.19`.

Following the successful authentication, the account:

* Executed system commands
* Accessed sensitive Finance and HR files
* Executed PowerShell and account-related commands
* Established network connections
* Transferred approximately 225 MB of data to the same external IP address

## Key Findings

The investigation identified several suspicious behaviors:

* Five consecutive failed authentication attempts
* Successful administrator authentication shortly after the failed attempts
* Authentication originating from an external IP address
* Execution of `whoami`, `ipconfig`, and `net user`
* Execution of `cmd.exe` and `powershell.exe`
* Access to sensitive Finance and HR files
* Network communication with the external IP address
* Approximately 225 MB of outbound data transfer

The observed activity is consistent with a potential account compromise followed by system reconnaissance, access to sensitive information, and possible data exfiltration.

However, the available logs do not independently prove who performed the activity, how the credentials were obtained, or exactly what information was transferred.

## Indicators of Interest

| Indicator        | Value                            |
| ---------------- | -------------------------------- |
| Account          | `administrator`                  |
| External IP      | `185.44.72.19`                   |
| Internal Host    | `10.0.0.50`                      |
| Port             | `445`                            |
| Port             | `443`                            |
| Processes        | `cmd.exe`, `powershell.exe`      |
| Commands         | `whoami`, `ipconfig`, `net user` |
| Data Transferred | Approximately 225 MB             |

## Investigation Timeline

The investigation timeline and detailed analysis can be found in `investigation.txt`.

## Files

* `authentication_logs.txt` - Authentication events and login attempts
* `system_activity.txt` - Commands, processes, and file access
* `network_activity.txt` - Network connections and data transfers
* `investigation.txt` - Full investigation, timeline, analysis, and indicators of interest

## Skills Demonstrated

This project demonstrates practical introductory SOC skills, including:

* Log analysis
* Authentication monitoring
* Timeline reconstruction
* Identification of suspicious behavior
* Basic network analysis
* Identification of indicators of interest
* Incident documentation
* Security investigation and reasoning

## Tools

* Text-based log analysis
* GitHub
* Windows security concepts
* Basic networking concepts

## Disclaimer

This is a simulated cybersecurity investigation created for educational and portfolio purposes. The logs and events used in this project are fictional.

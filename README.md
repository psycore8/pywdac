# pywdac

> Kills EDR with Windows Defender Application Control

Windows Defender Application Control (WDAC) is a policy-based application control system. Programs and directories can be allowed or blocked.

However, specially configured policies can be used to disable EDRs. Even the built-in Windows Defender can be bypassed this way.

With sufficient administrative privileges, attackers can exploit this to move laterally within the network.

## pywdac features

pywdac checks for write permission in the CodeIntegrity directory. If granted, a copy of the file SiPolicy.p7b is created there.

Additionally, the tool supports the following:

- Conversion of an XML template into the binary policy format
- Restarting the Computer
- Deleting the policy file from the directory

## usage

```shell
usage: pywdac.py [-h] [-d DIRECTORY] [-r] [-u] [-x XML_TEMPLATE]

options:
 -h, --help             show this help message and exit
 -d, --directory        DIRECTORY
                        Path to CodeIntegrity folder, where SiPolicy.p7b should be deployed
 -r, --reboot           Optional reboot after deployment, delayed for 60 seconds
 -u, --undo             Deletes SiPolicy.p7b from CodeIntegrity folder
 -x, --xml-template     XML_TEMPLATE
                        This will convert an XML policy template into SiPolicy.p7b
```
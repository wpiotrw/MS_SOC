---
layout: Conceptual
title: Reference - CIS Security Benchmarks for AKS Optimized Azure Linux via Machine Configuration - Azure Policy | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/policy/samples/cis-linux/azure-linux-ado
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/228/azure-policy
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/675ae472-f324-ec11-b6e6-000d3a4f0da0
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
adobe-target: true
author: pallakatos
learn_banner_products:
- azure
ms.author: pallakatos
ms.service: azure-policy
description: Reference - CIS Security Benchmarks for AKS Optimized Azure Linux via Machine Configuration
ms.date: 2026-11-04T00:00:00.0000000Z
ms.topic: reference
ms.custom: generated
locale: en-us
document_id: f163e267-032b-e33d-48b0-1b6dfb40a148
document_version_independent_id: 81ff8ea4-19cf-d930-c963-f6a6c85da9fa
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/policy/samples/cis-linux/azure-linux-ado.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/policy/samples/cis-linux/azure-linux-ado
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/policy/samples/cis-linux/azure-linux-ado.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/d44a5346-5de4-439c-b804-7b2a536cbb55
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/da41a22b-b7a0-42d3-9c35-50da1c2b7b87
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 037eeb19-270d-6c47-e0df-21c6e1c15f98
---

# Reference - CIS Security Benchmarks for AKS Optimized Azure Linux via Machine Configuration - Azure Policy | Microsoft Learn

This article provides detailed information about the CIS Security Benchmarks for AKS Optimized Azure Linux, including supported benchmarks, mismatched rules, remediation support, and configurable parameters across all supported versions.

## Supported benchmarks

| AKS Optimized Azure Linux Version | Benchmark Title |
| --- | --- |
| AKS Optimized Azure Linux 3 | CIS AKS Optimized Azure Linux 3 Benchmark 1.0.0 Level 1 + Level 2 - Server |

Note

Auto-remediation is in **[Public Preview]**. Remediation must be enabled separately and is available only for rules marked **Yes** in the **Remediation** column. It uses configured parameter values, or the defaults shown when no overrides are provided. Other rules remain audit-only. Review and test changes before enabling remediation broadly.

Supported parameters and remediations will expand over time. To request additional support, [open an issue in the kompli repository](https://github.com/microsoft/kompli/issues).

## CIS AKS Optimized Azure Linux 3 Benchmark 1.0.0 Level 1 + Level 2 - Server

### Rules

| Rule | Parameters | Default values | Remediation |
| --- | --- | --- | --- |
| 1.1.1.1 Ensure cramfs kernel module is not available | None | - | Yes |
| 1.1.1.2 Ensure freevxfs kernel module is not available | None | - | Yes |
| 1.1.1.3 Ensure hfs kernel module is not available | None | - | Yes |
| 1.1.1.4 Ensure hfsplus kernel module is not available | None | - | Yes |
| 1.1.1.5 Ensure jffs2 kernel module is not available | None | - | Yes |
| 1.1.1.6 Ensure unused filesystems kernel modules are not available | None | - | No |
| 1.1.2.1.1 Ensure /tmp is a separate partition | `mountPoint` | `/tmp` | No |
| 1.1.2.1.2 Ensure nodev option set on /tmp partition | `mountPoint``requiredMountOptions` | `/tmp``nodev` | No |
| 1.1.2.1.3 Ensure nosuid option set on /tmp partition | `mountPoint``requiredMountOptions` | `/tmp``nosuid` | No |
| 1.1.2.2.1 Ensure /dev/shm is a separate partition | `mountPoint` | `/dev/shm` | No |
| 1.1.2.2.2 Ensure nodev option set on /dev/shm partition | `mountPoint``requiredMountOptions` | `/dev/shm``nodev` | No |
| 1.1.2.2.3 Ensure nosuid option set on /dev/shm partition | `mountPoint``requiredMountOptions` | `/dev/shm``nosuid` | No |
| 1.2.1.1 Ensure GPG keys are configured | None | - | No |
| 1.2.1.2 Ensure gpgcheck is configured | None | - | No |
| 1.2.1.3 Ensure TDNF gpgcheck is globally activated | None | - | No |
| 1.2.1.4 Ensure package manager repositories are configured | None | - | No |
| 1.3.1 Ensure address space layout randomization is enabled | None | - | No |
| 1.3.2 Ensure ptrace\_scope is restricted | None | - | No |
| 1.3.3 Ensure core dump backtraces are disabled | `processSizeMaxRegex` | `0` | No |
| 1.3.4 Ensure core dump storage is disabled | `storageRegex` | `none` | No |
| 1.4.1 Ensure local login warning banner is configured properly | None | - | No |
| 1.4.2 Ensure remote login warning banner is configured properly | None | - | No |
| 1.4.3 Ensure access to /etc/motd is configured | `mask``owner``group` | `0133``root``root` | Yes |
| 1.4.4 Ensure access to /etc/issue is configured | `filename``mask``owner``group` | `/etc/issue``0133``root``root` | Yes |
| 1.4.5 Ensure access to /etc/issue.net is configured | None | - | Yes |
| 2.1.1 Ensure time synchronization is in use | `packageName` | `chrony` | No |
| 2.1.2 Ensure chrony is configured | None | - | No |
| 2.2.1 Ensure xinetd is not installed | None | - | No |
| 2.2.2 Ensure xorg-x11-server-common is not installed | None | - | No |
| 2.2.3 Ensure avahi is not installed | None | - | No |
| 2.2.4 Ensure a print server is not installed | None | - | No |
| 2.2.5 Ensure a dhcp server is not installed | None | - | No |
| 2.2.6 Ensure a dns server is not installed | None | - | No |
| 2.2.7 Ensure FTP client is not installed | None | - | No |
| 2.2.8 Ensure an ftp server is not installed | None | - | No |
| 2.2.9 Ensure a tftp server is not installed | None | - | No |
| 2.2.10 Ensure a web server is not installed | None | - | No |
| 2.2.11 Ensure IMAP and POP3 server is not installed | None | - | No |
| 2.2.12 Ensure Samba is not installed | None | - | No |
| 2.2.13 Ensure HTTP Proxy Server is not installed | None | - | No |
| 2.2.14 Ensure net-snmp is not installed or the snmpd service is not enabled | None | - | No |
| 2.2.15 Ensure NIS server is not installed | None | - | No |
| 2.2.16 Ensure telnet-server is not installed | None | - | No |
| 2.2.17 Ensure mail transfer agent is configured for local-only mode | None | - | No |
| 2.2.18 Ensure nfs-utils is not installed or the nfs-server service is masked | None | - | No |
| 2.2.19 Ensure rsync-daemon is not installed or the rsyncd service is masked | None | - | No |
| 2.3.1 Ensure NIS Client is not installed | None | - | No |
| 2.3.2 Ensure rsh client is not installed | None | - | No |
| 2.3.3 Ensure talk client is not installed | None | - | No |
| 2.3.4 Ensure telnet client is not installed | `packageName` | `telnet` | No |
| 2.3.5 Ensure LDAP client is not installed | None | - | No |
| 2.3.6 Ensure TFTP client is not installed | None | - | No |
| 3.1.1 Ensure packet redirect sending is disabled | None | - | No |
| 3.1.2 Ensure bogus icmp responses are ignored | None | - | No |
| 3.1.3 Ensure broadcast icmp requests are ignored | None | - | No |
| 3.1.4 Ensure icmp redirects are not accepted | None | - | No |
| 3.1.5 Ensure secure icmp redirects are not accepted | None | - | No |
| 3.1.6 Ensure reverse path filtering is enabled | None | - | No |
| 3.1.7 Ensure source routed packets are not accepted | None | - | No |
| 3.1.8 Ensure suspicious packets are logged | None | - | No |
| 3.1.9 Ensure tcp syn cookies is enabled | None | - | No |
| 3.1.10 Ensure ipv6 router advertisements are not accepted | None | - | No |
| 4.1.1 Ensure iptables is installed | None | - | No |
| 4.1.2 Ensure nftables is not in use | None | - | No |
| 4.1.3 Ensure firewalld is not in use | None | - | No |
| 5.1.1 Ensure cron daemon is enabled | None | - | No |
| 5.1.2 Ensure permissions on /etc/crontab are configured | `mask``owner``group` | `0077``root``root` | Yes |
| 5.1.3 Ensure permissions on /etc/cron.hourly are configured | `mask``owner``group` | `0077``root``root` | Yes |
| 5.1.4 Ensure permissions on /etc/cron.daily are configured | `mask``owner``group` | `0077``root``root` | Yes |
| 5.1.5 Ensure permissions on /etc/cron.weekly are configured | `mask``owner``group` | `0077``root``root` | Yes |
| 5.1.6 Ensure permissions on /etc/cron.monthly are configured | `mask``owner``group` | `0077``root``root` | Yes |
| 5.1.7 Ensure permissions on /etc/cron.d are configured | `mask``owner``group` | `0077``root``root` | Yes |
| 5.1.8 Ensure cron is restricted to authorized users | `filenameEtcCronDeny``owner``group``mask``filenameEtcCronAllow` | `/etc/cron.deny``root``root``0137``/etc/cron.allow` | Yes |
| 5.1.9 Ensure at is restricted to authorized users | `owner``group``mask` | `root``root``0177` | Yes |
| 5.2.1 Ensure access to /etc/ssh/sshd\_config is configured | `mask``owner``group` | `0177``root``root` | Yes |
| 5.2.2 Ensure access to SSH private host key files is configured | None | - | No |
| 5.2.3 Ensure access to SSH public host key files is configured | None | - | No |
| 5.2.4 Ensure sshd Ciphers are configured | `ciphersDisallowedValues` | `3des-cbc,aes128-cbc,aes192-cbc,aes256-cbc,arcfour,arcfour128,arcfour256,blowfish-cbc,cast128-cbc,rijndael-cbc@lysator\.liu\.se` | No |
| 5.2.5 Ensure sshd KexAlgorithms is configured | `kexalgorithmsDisallowedValues` | `diffie-hellman-group1-sha1,diffie-hellman-group14-sha1,diffie-hellman-group-exchange-sha1` | No |
| 5.2.6 Ensure sshd MACs are configured | `macsDisallowedValues` | `hmac-md5,hmac-md5-96,hmac-ripemd160,hmac-sha1-96,umac-64@openssh\.com,hmac-md5-etm@openssh\.com,hmac-md5-96-etm@openssh\.com,hmac-ripemd160-etm@openssh\.com,hmac-sha1-96-etm@openssh\.com,umac-64-etm@openssh\.com` | No |
| 5.2.7 Ensure sshd access is configured | `allowUsersValuePattern``allowGroupsValuePattern``denyUsersValuePattern``denyGroupsValuePattern` | `[^ \t]+``[^ \t]+``[^ \t]+``[^ \t]+` | No |
| 5.2.8 Ensure sshd Banner is configured | `bannerExpectedValueT``bannerDisallowedValuesNone` | `\/[^ \t]+``none` | No |
| 5.2.9 Ensure sshd ClientAliveInterval and ClientAliveCountMax are configured | `clientalivecountmaxThreshold``clientaliveintervalThreshold` | `0``0` | No |
| 5.2.10 Ensure sshd HostbasedAuthentication is disabled | None | - | No |
| 5.2.11 Ensure sshd IgnoreRhosts is enabled | None | - | No |
| 5.2.12 Ensure sshd LoginGraceTime is configured | `logingracetimeThresholdValue60``logingracetimeThresholdValue0` | `60``0` | No |
| 5.2.13 Ensure sshd LogLevel is configured | `loglevelExpectedValue` | `verbose,info` | No |
| 5.2.14 Ensure sshd MaxAuthTries is configured | `maxauthtriesThreshold` | `4` | No |
| 5.2.15 Ensure sshd MaxStartups is configured | `maxstartupsExpectedValue` | `10:30:100` | No |
| 5.2.16 Ensure sshd MaxSessions is configured | `maxsessionsThreshold` | `10` | No |
| 5.2.17 Ensure sshd PermitEmptyPasswords is disabled | None | - | No |
| 5.2.18 Ensure sshd PermitRootLogin is disabled | None | - | No |
| 5.2.19 Ensure sshd PermitUserEnvironment is disabled | None | - | No |
| 5.2.20 Ensure sshd UsePAM is enabled | None | - | No |
| 5.3.1 Ensure sudo is installed | None | - | No |
| 5.3.2 Ensure re-authentication for privilege escalation is not disabled globally | None | - | No |
| 5.3.3 Ensure sudo authentication timeout is configured correctly | None | - | No |
| 5.4.1 Ensure password creation requirements are configured | None | - | No |
| 5.4.2 Ensure lockout for failed password attempts is configured | None | - | No |
| 5.4.3 Ensure password hashing algorithm is SHA-512 | None | - | No |
| 5.4.4 Ensure password reuse is limited | None | - | No |
| 5.5.1.1 Ensure password expiration is 365 days or less | `maxDays` | `365` | Yes |
| 5.5.1.2 Ensure minimum days between password changes is configured | `minDays` | `1` | Yes |
| 5.5.1.3 Ensure password expiration warning days is 7 or more | `warnDays` | `7` | Yes |
| 5.5.1.4 Ensure inactive password lock is 30 days or less | None | - | No |
| 5.5.1.5 Ensure all users last password change date is in the past | None | - | No |
| 5.5.2 Ensure system accounts are secured | None | - | No |
| 5.5.3 Ensure default group for the root account is GID 0 | None | - | No |
| 5.5.4 Ensure default user umask is 027 or more restrictive | None | - | No |
| 6.1.1.1.1 Ensure journald service is active | None | - | No |
| 6.1.1.1.2 Ensure journald log file access is configured | None | - | No |
| 6.1.1.1.3 Ensure journald ForwardToSyslog is configured | None | - | No |
| 6.1.1.1.4 Ensure systemd-journal-remote service is not in use | None | - | No |
| 6.1.1.1.5 Ensure journald Storage is configured | `storageValue` | `persistent` | No |
| 6.1.1.1.6 Ensure journald Compress is configured | `compressValue` | `yes` | No |
| 6.1.2.1 Ensure rsyslog service is enabled and active | None | - | No |
| 6.1.2.2 Ensure rsyslog log file creation mode is configured | None | - | No |
| 6.1.2.3 Ensure rsyslog is not configured to receive logs from a remote client | None | - | No |
| 6.1.3.1 Ensure access to all logfiles has been configured | None | - | No |
| 6.2 Ensure logrotate is configured | None | - | No |
| 7.1.1 Ensure access to /etc/passwd is configured | None | - | Yes |
| 7.1.2 Ensure access to /etc/passwd- is configured | None | - | Yes |
| 7.1.3 Ensure access to /etc/group is configured | None | - | Yes |
| 7.1.4 Ensure access to /etc/group- is configured | None | - | Yes |
| 7.1.5 Ensure access to /etc/shadow is configured | None | - | Yes |
| 7.1.6 Ensure access to /etc/shadow- is configured | None | - | Yes |
| 7.1.7 Ensure access to /etc/gshadow is configured | None | - | Yes |
| 7.1.8 Ensure access to /etc/gshadow- is configured | None | - | Yes |
| 7.1.9 Ensure access to /etc/shells is configured | None | - | Yes |
| 7.1.10 Ensure access to /etc/security/opasswd is configured | `mask``owner``group` | `0177``root``root` | Yes |
| 7.1.11 Ensure world writable files and directories are secured | None | - | No |
| 7.1.12 Ensure no files or directories without an owner and a group exist | None | - | No |
| 7.2.1 Ensure accounts in /etc/passwd use shadowed passwords | None | - | No |
| 7.2.2 Ensure /etc/shadow password fields are not empty | None | - | No |
| 7.2.3 Ensure all groups in /etc/passwd exist in /etc/group | None | - | No |
| 7.2.4 Ensure no duplicate UIDs exist | None | - | No |
| 7.2.5 Ensure no duplicate GIDs exist | None | - | No |
| 7.2.6 Ensure no duplicate user names exist | None | - | No |
| 7.2.7 Ensure no duplicate group names exist | None | - | No |
| 7.2.8 Ensure local interactive user home directories are configured | None | - | No |
| 7.2.9 Ensure local interactive user dot files access is configured | None | - | No |

### Known assessment discrepancies

Note

These rules may produce assessment results that differ from CIS-CAT® Pro Assessor; our implementation may enforce stricter criteria. A rule is listed once if a discrepancy was observed in any tested scenario.

No discrepancies found among compared rules.
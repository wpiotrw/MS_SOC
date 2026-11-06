---
layout: Conceptual
title: Reference - CIS Security Benchmarks for Debian Linux via Machine Configuration - Azure Policy | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/policy/samples/cis-linux/debian-ado
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
description: Reference - CIS Security Benchmarks for Debian Linux via Machine Configuration
ms.date: 2026-11-04T00:00:00.0000000Z
ms.topic: reference
ms.custom: generated
locale: en-us
document_id: f5af4e80-98cc-fee0-c720-31db84a6ab6b
document_version_independent_id: eed5e056-0bd6-72a7-3f8f-704b15411211
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/policy/samples/cis-linux/debian-ado.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/policy/samples/cis-linux/debian-ado
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/policy/samples/cis-linux/debian-ado.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 019b0ecd-2b74-7bc6-c73b-ce8b84f897de
---

# Reference - CIS Security Benchmarks for Debian Linux via Machine Configuration - Azure Policy | Microsoft Learn

This article provides detailed information about the CIS Security Benchmarks for Debian Linux, including supported benchmarks, mismatched rules, remediation support, and configurable parameters across all supported versions.

## Supported benchmarks

| Debian Linux Version | Benchmark Title |
| --- | --- |
| Debian Linux 11 | CIS Debian Linux 11 Benchmark 2.0.0 Level 1 + Level 2 - Server |
| Debian Linux 12 | CIS Debian Linux 12 Benchmark 1.1.0 Level 1 + Level 2 - Server |

Note

Auto-remediation is in **[Public Preview]**. Remediation must be enabled separately and is available only for rules marked **Yes** in the **Remediation** column. It uses configured parameter values, or the defaults shown when no overrides are provided. Other rules remain audit-only. Review and test changes before enabling remediation broadly.

Supported parameters and remediations will expand over time. To request additional support, [open an issue in the kompli repository](https://github.com/microsoft/kompli/issues).

## CIS Debian Linux 11 Benchmark 2.0.0 Level 1 + Level 2 - Server

### Rules

| Rule | Parameters | Default values | Remediation |
| --- | --- | --- | --- |
| 1.1.1.1 Ensure cramfs kernel module is not available | None | - | Yes |
| 1.1.1.2 Ensure freevxfs kernel module is not available | None | - | Yes |
| 1.1.1.3 Ensure hfs kernel module is not available | None | - | Yes |
| 1.1.1.4 Ensure hfsplus kernel module is not available | None | - | Yes |
| 1.1.1.5 Ensure jffs2 kernel module is not available | None | - | Yes |
| 1.1.1.6 Ensure squashfs kernel module is not available | None | - | Yes |
| 1.1.1.7 Ensure udf kernel module is not available | None | - | Yes |
| 1.1.1.8 Ensure usb-storage kernel module is not available | None | - | Yes |
| 1.1.2.1.1 Ensure /tmp is a separate partition | `mountPoint` | `/tmp` | No |
| 1.1.2.1.2 Ensure nodev option set on /tmp partition | `mountPoint``requiredMountOptions` | `/tmp``nodev` | No |
| 1.1.2.1.3 Ensure nosuid option set on /tmp partition | `mountPoint``requiredMountOptions` | `/tmp``nosuid` | No |
| 1.1.2.1.4 Ensure noexec option set on /tmp partition | `mountPoint``requiredMountOptions` | `/tmp``noexec` | No |
| 1.1.2.2.1 Ensure /dev/shm is a separate partition | `mountPoint` | `/dev/shm` | No |
| 1.1.2.2.2 Ensure nodev option set on /dev/shm partition | `mountPoint``requiredMountOptions` | `/dev/shm``nodev` | No |
| 1.1.2.2.3 Ensure nosuid option set on /dev/shm partition | `mountPoint``requiredMountOptions` | `/dev/shm``nosuid` | No |
| 1.1.2.2.4 Ensure noexec option set on /dev/shm partition | `mountPoint``requiredMountOptions` | `/dev/shm``noexec` | No |
| 1.1.2.3.1 Ensure separate partition exists for /home | `mountPoint` | `/home` | No |
| 1.1.2.3.2 Ensure nodev option set on /home partition | `mountPoint``requiredMountOptions` | `/home``nodev` | No |
| 1.1.2.3.3 Ensure nosuid option set on /home partition | `mountPoint``requiredMountOptions` | `/home``nosuid` | No |
| 1.1.2.4.1 Ensure separate partition exists for /var | `mountPoint` | `/var` | No |
| 1.1.2.4.2 Ensure nodev option set on /var partition | `mountPoint``requiredMountOptions` | `/var``nodev` | No |
| 1.1.2.4.3 Ensure nosuid option set on /var partition | `mountPoint``requiredMountOptions` | `/var``nosuid` | No |
| 1.1.2.5.1 Ensure separate partition exists for /var/tmp | `mountPoint` | `/var/tmp` | No |
| 1.1.2.5.2 Ensure nodev option set on /var/tmp partition | `mountPoint``requiredMountOptions` | `/var/tmp``nodev` | No |
| 1.1.2.5.3 Ensure nosuid option set on /var/tmp partition | `mountPoint``requiredMountOptions` | `/var/tmp``nosuid` | No |
| 1.1.2.5.4 Ensure noexec option set on /var/tmp partition | `mountPoint``requiredMountOptions` | `/var/tmp``noexec` | No |
| 1.1.2.6.1 Ensure separate partition exists for /var/log | `mountPoint` | `/var/log` | No |
| 1.1.2.6.2 Ensure nodev option set on /var/log partition | `mountPoint``requiredMountOptions` | `/var/log``nodev` | No |
| 1.1.2.6.3 Ensure nosuid option set on /var/log partition | `mountPoint``requiredMountOptions` | `/var/log``nosuid` | No |
| 1.1.2.6.4 Ensure noexec option set on /var/log partition | `mountPoint``requiredMountOptions` | `/var/log``noexec` | No |
| 1.1.2.7.1 Ensure separate partition exists for /var/log/audit | `mountPoint` | `/var/log/audit` | No |
| 1.1.2.7.2 Ensure nodev option set on /var/log/audit partition | `mountPoint``requiredMountOptions` | `/var/log/audit``nodev` | No |
| 1.1.2.7.3 Ensure nosuid option set on /var/log/audit partition | `mountPoint``requiredMountOptions` | `/var/log/audit``nosuid` | No |
| 1.1.2.7.4 Ensure noexec option set on /var/log/audit partition | `mountPoint``requiredMountOptions` | `/var/log/audit``noexec` | No |
| 1.2.1.1 Ensure GPG keys are configured | None | - | No |
| 1.2.1.2 Ensure package manager repositories are configured | None | - | No |
| 1.2.2.1 Ensure updates, patches, and additional security software are installed | None | - | No |
| 1.3.1.1 Ensure AppArmor is installed | None | - | No |
| 1.3.1.2 Ensure AppArmor is enabled in the bootloader configuration | None | - | No |
| 1.3.1.3 Ensure all AppArmor Profiles are in enforce or complain mode | None | - | No |
| 1.3.1.4 Ensure all AppArmor Profiles are enforcing | None | - | No |
| 1.4.1 Ensure bootloader password is set | None | - | No |
| 1.4.2 Ensure access to bootloader config is configured | `filename``mask``owner``group` | `/boot/grub/grub.cfg``0177``root``root` | Yes |
| 1.5.1 Ensure address space layout randomization is enabled | None | - | No |
| 1.5.2 Ensure ptrace\_scope is restricted | None | - | No |
| 1.5.3 Ensure core dumps are restricted | None | - | No |
| 1.5.4 Ensure prelink is not installed | None | - | No |
| 1.5.5 Ensure Automatic Error Reporting is not enabled | None | - | No |
| 1.6.1 Ensure message of the day is configured properly | None | - | No |
| 1.6.2 Ensure local login warning banner is configured properly | None | - | No |
| 1.6.3 Ensure remote login warning banner is configured properly | None | - | No |
| 1.6.4 Ensure access to /etc/motd is configured | None | - | Yes |
| 1.6.5 Ensure access to /etc/issue is configured | `filename``mask``owner``group` | `/etc/issue``0133``root``root` | Yes |
| 1.6.6 Ensure access to /etc/issue.net is configured | None | - | Yes |
| 1.7.1 Ensure GDM is removed | None | - | No |
| 1.7.2 Ensure GDM login banner is configured | None | - | Yes |
| 1.7.3 Ensure GDM disable-user-list option is enabled | None | - | Yes |
| 1.7.4 Ensure GDM screen locks when the user is idle | None | - | No |
| 1.7.5 Ensure GDM screen locks cannot be overridden | None | - | No |
| 1.7.6 Ensure GDM automatic mounting of removable media is disabled | None | - | Yes |
| 1.7.7 Ensure GDM disabling automatic mounting of removable media is not overridden | None | - | No |
| 1.7.8 Ensure GDM autorun-never is enabled | None | - | Yes |
| 1.7.9 Ensure GDM autorun-never is not overridden | None | - | No |
| 1.7.10 Ensure XDCMP is not enabled | None | - | Yes |
| 2.1.1 Ensure autofs services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `autofs.service``enabled``active``autofs` | No |
| 2.1.2 Ensure avahi daemon services are not in use | `unitNameAvahiDaemonService``expectedUnitFileState``expectedActiveState``unitNameAvahiDaemonSocket``packageName` | `avahi-daemon.service``enabled``active``avahi-daemon.socket``avahi-daemon` | No |
| 2.1.3 Ensure dhcp server services are not in use | `unitNameIscDhcpServerService``expectedUnitFileState``expectedActiveState``unitNameIscDhcpServer6Service``packageName` | `isc-dhcp-server.service``enabled``active``isc-dhcp-server6.service``isc-dhcp-server` | No |
| 2.1.4 Ensure dns server services are not in use | `serviceName``expectedUnitFileState``expectedActiveState``packageName` | `bind9.service``enabled``active``bind9` | No |
| 2.1.5 Ensure dnsmasq services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `dnsmasq.service``enabled``active``dnsmasq` | No |
| 2.1.6 Ensure ftp server services are not in use | `serviceName``expectedUnitFileState``expectedActiveState``packageName` | `vsftpd.service``enabled``active``vsftpd` | No |
| 2.1.7 Ensure ldap server services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `slapd.service``enabled``active``slapd` | No |
| 2.1.8 Ensure message access server services are not in use | `packageNameDovecotImapd``packageNameDovecotPop3d``unitNameDovecotService``expectedUnitFileState``expectedActiveState``unitNameDovecotSocket` | `dovecot-imapd``dovecot-pop3d``dovecot.service``enabled``active``dovecot.socket` | No |
| 2.1.9 Ensure network file system services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `nfs-server.service``enabled``active``nfs-kernel-server` | No |
| 2.1.10 Ensure nis server services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `ypserv.service``enabled``active``ypserv` | No |
| 2.1.11 Ensure print server services are not in use | `unitNameCupsService``expectedUnitFileState``expectedActiveState``unitNameCupsSocket``packageName` | `cups.service``enabled``active``cups.socket``cups` | No |
| 2.1.12 Ensure rpcbind services are not in use | `unitNameRpcbindService``expectedUnitFileState``expectedActiveState``unitNameRpcbindSocket``packageName` | `rpcbind.service``enabled``active``rpcbind.socket``rpcbind` | No |
| 2.1.13 Ensure rsync services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `rsync.service``enabled``active``rsync` | No |
| 2.1.14 Ensure samba file server services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `smbd.service``enabled``active``samba` | No |
| 2.1.15 Ensure snmp services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `snmpd.service``enabled``active``snmpd` | No |
| 2.1.16 Ensure tftp server services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `tftpd-hpa.service``enabled``active``tftpd-hpa` | No |
| 2.1.17 Ensure web proxy server services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `squid.service``enabled``active``squid` | No |
| 2.1.18 Ensure web server services are not in use | `unitNameApache2Service``expectedUnitFileState``expectedActiveState``unitNameApache2Socket``packageNameApache2``unitNameNginxService``packageNameNginx` | `apache2.service``enabled``active``apache2.socket``apache2``nginx.service``nginx` | No |
| 2.1.19 Ensure xinetd services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `xinetd.service``enabled``active``xinetd` | No |
| 2.1.20 Ensure X window server services are not in use | None | - | No |
| 2.1.21 Ensure mail transfer agent is configured for local-only mode | None | - | No |
| 2.1.22 Ensure only approved services are listening on a network interface | None | - | No |
| 2.2.1 Ensure NIS Client is not installed | None | - | No |
| 2.2.2 Ensure rsh client is not installed | None | - | No |
| 2.2.3 Ensure talk client is not installed | None | - | No |
| 2.2.4 Ensure telnet client is not installed | `packageName` | `telnet` | No |
| 2.2.5 Ensure ldap client is not installed | None | - | No |
| 2.2.6 Ensure ftp client is not installed | None | - | No |
| 2.3.1.1 Ensure a single time synchronization daemon is in use | None | - | No |
| 2.3.2.1 Ensure systemd-timesyncd configured with authorized timeserver | None | - | No |
| 2.3.2.2 Ensure systemd-timesyncd is enabled and running | None | - | No |
| 2.3.3.1 Ensure chrony is configured with authorized timeserver | None | - | No |
| 2.3.3.2 Ensure chrony is running as user \_chrony | None | - | No |
| 2.3.3.3 Ensure chrony is enabled and running | None | - | No |
| 2.4.1.1 Ensure cron daemon is enabled and active | None | - | No |
| 2.4.1.2 Ensure permissions on /etc/crontab are configured | `mask``owner``group` | `0177``root``root` | Yes |
| 2.4.1.3 Ensure permissions on /etc/cron.hourly are configured | `mask``owner``group` | `0077``root``root` | Yes |
| 2.4.1.4 Ensure permissions on /etc/cron.daily are configured | `mask``owner``group``packageName``alternativePackageName` | `0077``root``root``cron``cronie` | Yes |
| 2.4.1.5 Ensure permissions on /etc/cron.weekly are configured | `mask``owner``group` | `0077``root``root` | Yes |
| 2.4.1.6 Ensure permissions on /etc/cron.monthly are configured | `mask``owner``group``alternativePackageName` | `0077``root``root``cronie` | Yes |
| 2.4.1.7 Ensure permissions on /etc/cron.d are configured | `mask``owner``group` | `0077``root``root` | Yes |
| 2.4.1.8 Ensure crontab is restricted to authorized users | `filenameEtcCronDeny``mask``owner``group``filenameEtcCronAllow` | `/etc/cron.deny``0137``root``root``/etc/cron.allow` | Yes |
| 2.4.2.1 Ensure at is restricted to authorized users | `mask``owner``group` | `0137``root``root\|daemon` | Yes |
| 3.1.1 Ensure IPv6 status is identified | None | - | No |
| 3.1.2 Ensure wireless interfaces are disabled | None | - | No |
| 3.1.3 Ensure bluetooth services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `bluetooth.service``enabled``active``bluez` | No |
| 3.2.1 Ensure dccp kernel module is not available | None | - | Yes |
| 3.2.2 Ensure tipc kernel module is not available | None | - | Yes |
| 3.2.3 Ensure rds kernel module is not available | None | - | Yes |
| 3.2.4 Ensure sctp kernel module is not available | None | - | Yes |
| 3.3.1 Ensure ip forwarding is disabled | None | - | No |
| 3.3.2 Ensure packet redirect sending is disabled | None | - | No |
| 3.3.3 Ensure bogus icmp responses are ignored | None | - | No |
| 3.3.4 Ensure broadcast icmp requests are ignored | None | - | No |
| 3.3.5 Ensure icmp redirects are not accepted | None | - | No |
| 3.3.6 Ensure secure icmp redirects are not accepted | None | - | No |
| 3.3.7 Ensure reverse path filtering is enabled | None | - | No |
| 3.3.8 Ensure source routed packets are not accepted | None | - | No |
| 3.3.9 Ensure suspicious packets are logged | None | - | No |
| 3.3.10 Ensure tcp syn cookies is enabled | None | - | No |
| 3.3.11 Ensure ipv6 router advertisements are not accepted | None | - | No |
| 4.1.1 Ensure ufw is installed | None | - | No |
| 4.1.2 Ensure iptables-persistent is not installed with ufw | None | - | No |
| 4.1.3 Ensure ufw service is enabled | None | - | No |
| 4.1.4 Ensure ufw loopback traffic is configured | None | - | No |
| 4.1.5 Ensure ufw outbound connections are configured | None | - | No |
| 4.1.6 Ensure ufw firewall rules exist for all open ports | None | - | No |
| 4.1.7 Ensure ufw default deny firewall policy | None | - | No |
| 4.2.1 Ensure nftables is installed | None | - | No |
| 4.2.2 Ensure ufw is uninstalled or disabled with nftables | None | - | No |
| 4.2.3 Ensure iptables are flushed with nftables | None | - | No |
| 4.2.4 Ensure a nftables table exists | None | - | No |
| 4.2.5 Ensure nftables base chains exist | None | - | No |
| 4.2.6 Ensure nftables loopback traffic is configured | None | - | No |
| 4.2.7 Ensure nftables outbound and established connections are configured | None | - | No |
| 4.2.8 Ensure nftables default deny firewall policy | None | - | No |
| 4.2.9 Ensure nftables service is enabled | None | - | No |
| 4.2.10 Ensure nftables rules are permanent | None | - | No |
| 4.3.1.1 Ensure iptables packages are installed | None | - | No |
| 4.3.1.2 Ensure nftables is not installed with iptables | None | - | No |
| 4.3.1.3 Ensure ufw is uninstalled or disabled with iptables | None | - | No |
| 4.3.2.1 Ensure iptables default deny firewall policy | None | - | No |
| 4.3.2.2 Ensure iptables loopback traffic is configured | None | - | No |
| 4.3.2.3 Ensure iptables outbound and established connections are configured | None | - | No |
| 4.3.2.4 Ensure iptables firewall rules exist for all open ports | None | - | No |
| 4.3.3.1 Ensure ip6tables default deny firewall policy | None | - | No |
| 4.3.3.2 Ensure ip6tables loopback traffic is configured | None | - | No |
| 4.3.3.3 Ensure ip6tables outbound and established connections are configured | None | - | No |
| 4.3.3.4 Ensure ip6tables firewall rules exist for all open ports | None | - | No |
| 5.1.1 Ensure permissions on /etc/ssh/sshd\_config are configured | `mask``owner``group` | `0177``root``root` | Yes |
| 5.1.2 Ensure permissions on SSH private host key files are configured | None | - | No |
| 5.1.3 Ensure permissions on SSH public host key files are configured | None | - | No |
| 5.1.4 Ensure sshd access is configured | `allowUsersValuePattern``allowGroupsValuePattern``denyUsersValuePattern``denyGroupsValuePattern` | `[^ \t]+``[^ \t]+``[^ \t]+``[^ \t]+` | No |
| 5.1.5 Ensure sshd Banner is configured | `bannerValue` | `\/[^ \t]+` | No |
| 5.1.6 Ensure sshd Ciphers are configured | `ciphersDisallowedValues` | `3des-cbc,aes128-cbc,aes192-cbc,aes256-cbc,arcfour,arcfour128,arcfour256,blowfish-cbc,cast128-cbc,rijndael-cbc@lysator\.liu\.se` | No |
| 5.1.7 Ensure sshd ClientAliveInterval and ClientAliveCountMax are configured | `clientalivecountmaxValue``clientaliveintervalValue` | `[1-9][0-9]*m?``[1-9][0-9]*m?` | No |
| 5.1.8 Ensure sshd DisableForwarding is enabled | None | - | No |
| 5.1.9 Ensure sshd GSSAPIAuthentication is disabled | None | - | No |
| 5.1.10 Ensure sshd HostbasedAuthentication is disabled | None | - | No |
| 5.1.11 Ensure sshd IgnoreRhosts is enabled | None | - | No |
| 5.1.12 Ensure sshd KexAlgorithms is configured | `kexalgorithmsDisallowedValues` | `diffie-hellman-group1-sha1,diffie-hellman-group14-sha1,diffie-hellman-group-exchange-sha1` | No |
| 5.1.13 Ensure sshd LoginGraceTime is configured | `logingracetimeValue` | `^(\b([1-9]\|[1-5][0-9]\|60)\b)$` | No |
| 5.1.14 Ensure sshd LogLevel is configured | `loglevelValue` | `(VERBOSE\|INFO)\b` | No |
| 5.1.15 Ensure sshd MACs are configured | `macsDisallowedValues` | `hmac-md5,hmac-md5-96,hmac-ripemd160,hmac-sha1-96,umac-64@openssh\.com,hmac-md5-etm@openssh\.com,hmac-md5-96-etm@openssh\.com,hmac-ripemd160-etm@openssh\.com,hmac-sha1-96-etm@openssh\.com,umac-64-etm@openssh\.com,umac-128-etm@openssh\.com` | No |
| 5.1.16 Ensure sshd MaxAuthTries is configured | `maxauthtriesValue` | `^([0-4]\b)$` | No |
| 5.1.17 Ensure sshd MaxSessions is configured | `maxsessionsValue` | `([1-9]\|10)\b` | No |
| 5.1.18 Ensure sshd MaxStartups is configured | `maxstartupsValue` | `^((10\|[1-9])[^ \t](30\|[1-2][0-9]\|[1-9])[^ \t](60\|[1-5][0-9]\|[1-9])\b)$` | No |
| 5.1.19 Ensure sshd PermitEmptyPasswords is disabled | None | - | No |
| 5.1.20 Ensure sshd PermitRootLogin is disabled | None | - | No |
| 5.1.21 Ensure sshd PermitUserEnvironment is disabled | None | - | No |
| 5.1.22 Ensure sshd UsePAM is enabled | None | - | No |
| 5.2.1 Ensure sudo is installed | None | - | No |
| 5.2.2 Ensure sudo commands use pty | None | - | No |
| 5.2.3 Ensure sudo log file exists | None | - | No |
| 5.2.4 Ensure users must provide password for privilege escalation | None | - | No |
| 5.2.5 Ensure re-authentication for privilege escalation is not disabled globally | None | - | No |
| 5.2.6 Ensure sudo authentication timeout is configured correctly | None | - | No |
| 5.2.7 Ensure access to the su command is restricted | None | - | No |
| 5.3.1.1 Ensure latest version of pam is installed | None | - | No |
| 5.3.1.2 Ensure libpam-modules is installed | None | - | No |
| 5.3.1.3 Ensure libpam-pwquality is installed | None | - | No |
| 5.3.2.1 Ensure pam\_unix module is enabled | None | - | No |
| 5.3.2.2 Ensure pam\_faillock module is enabled | None | - | No |
| 5.3.2.3 Ensure pam\_pwquality module is enabled | None | - | No |
| 5.3.2.4 Ensure pam\_pwhistory module is enabled | None | - | No |
| 5.3.3.1.1 Ensure password failed attempts lockout is configured | None | - | No |
| 5.3.3.1.2 Ensure password unlock time is configured | None | - | No |
| 5.3.3.1.3 Ensure password failed attempts lockout includes root account | None | - | No |
| 5.3.3.2.1 Ensure password number of changed characters is configured | None | - | No |
| 5.3.3.2.2 Ensure minimum password length is configured | None | - | No |
| 5.3.3.2.3 Ensure password complexity is configured | None | - | No |
| 5.3.3.2.4 Ensure password same consecutive characters is configured | None | - | No |
| 5.3.3.2.5 Ensure password maximum sequential characters is configured | None | - | No |
| 5.3.3.2.6 Ensure password dictionary check is enabled | None | - | No |
| 5.3.3.2.7 Ensure password quality checking is enforced | None | - | No |
| 5.3.3.2.8 Ensure password quality is enforced for the root user | None | - | No |
| 5.3.3.3.1 Ensure password history remember is configured | None | - | No |
| 5.3.3.3.2 Ensure password history is enforced for the root user | None | - | No |
| 5.3.3.3.3 Ensure pam\_pwhistory includes use\_authtok | None | - | No |
| 5.3.3.4.1 Ensure pam\_unix does not include nullok | None | - | No |
| 5.3.3.4.2 Ensure pam\_unix does not include remember | None | - | No |
| 5.3.3.4.3 Ensure pam\_unix includes a strong password hashing algorithm | None | - | No |
| 5.3.3.4.4 Ensure pam\_unix includes use\_authtok | None | - | No |
| 5.4.1.1 Ensure password expiration is configured | `maxDays``minDays` | `365``1` | Yes |
| 5.4.1.2 Ensure minimum password age is configured | `minDays` | `1` | No |
| 5.4.1.3 Ensure password expiration warning days is configured | `warnDays` | `7` | Yes |
| 5.4.1.4 Ensure strong password hashing algorithm is configured | `hashAlgorithm``fallbackHashAlgorithm` | `YESCRYPT``SHA512` | Yes |
| 5.4.1.5 Ensure inactive password lock is configured | None | - | No |
| 5.4.1.6 Ensure all users last password change date is in the past | None | - | No |
| 5.4.2.1 Ensure root is the only UID 0 account | None | - | No |
| 5.4.2.2 Ensure root is the only GID 0 account | None | - | No |
| 5.4.2.3 Ensure group root is the only GID 0 group | None | - | No |
| 5.4.2.4 Ensure root password is set | None | - | No |
| 5.4.2.5 Ensure root path integrity | None | - | No |
| 5.4.2.6 Ensure root user umask is configured | None | - | No |
| 5.4.2.7 Ensure system accounts do not have a valid login shell | None | - | No |
| 5.4.2.8 Ensure accounts without a valid login shell are locked | None | - | No |
| 5.4.3.1 Ensure nologin is not listed in /etc/shells | None | - | No |
| 5.4.3.2 Ensure default user shell timeout is configured | None | - | Yes |
| 5.4.3.3 Ensure default user umask is configured | None | - | Yes |
| 6.1.1 Ensure AIDE is installed | None | - | No |
| 6.1.2 Ensure filesystem integrity is regularly checked | None | - | No |
| 6.1.3 Ensure cryptographic mechanisms are used to protect the integrity of audit tools | None | - | No |
| 6.2.1.1.1 Ensure journald service is enabled and active | None | - | No |
| 6.2.1.1.2 Ensure journald log file access is configured | None | - | No |
| 6.2.1.1.3 Ensure journald log file rotation is configured | None | - | No |
| 6.2.1.1.4 Ensure journald ForwardToSyslog is disabled | `forwardToSyslogRegex` | `yes` | No |
| 6.2.1.1.5 Ensure journald Storage is configured | `storageRegex` | `persistent` | No |
| 6.2.1.1.6 Ensure journald Compress is configured | `compressRegex` | `yes` | No |
| 6.2.1.2.1 Ensure systemd-journal-remote is installed | None | - | No |
| 6.2.1.2.2 Ensure systemd-journal-remote authentication is configured | None | - | No |
| 6.2.1.2.3 Ensure systemd-journal-upload is enabled and active | None | - | No |
| 6.2.1.2.4 Ensure systemd-journal-remote service is not in use | None | - | No |
| 6.2.2.1 Ensure access to all logfiles has been configured | None | - | No |
| 6.4.1.1 Ensure auditd packages are installed | None | - | No |
| 6.4.1.2 Ensure auditd service is enabled and active | None | - | No |
| 6.4.1.3 Ensure auditing for processes that start prior to auditd is enabled | None | - | No |
| 6.4.1.4 Ensure audit\_backlog\_limit is sufficient | None | - | No |
| 6.4.2.1 Ensure audit log storage size is configured | None | - | No |
| 6.4.2.2 Ensure audit logs are not automatically deleted | None | - | No |
| 6.4.2.3 Ensure system is disabled when audit logs are full | None | - | No |
| 6.4.2.4 Ensure system warns when audit logs are low on space | None | - | No |
| 6.4.3.1 Ensure changes to system administration scope (sudoers) is collected | None | - | No |
| 6.4.3.2 Ensure actions as another user are always logged | None | - | No |
| 6.4.3.3 Ensure events that modify the sudo log file are collected | None | - | No |
| 6.4.3.4 Ensure events that modify date and time information are collected | None | - | No |
| 6.4.3.5 Ensure events that modify the system's network environment are collected | None | - | No |
| 6.4.3.6 Ensure use of privileged commands are collected | None | - | No |
| 6.4.3.7 Ensure unsuccessful file access attempts are collected | None | - | No |
| 6.4.3.8 Ensure events that modify user/group information are collected | None | - | No |
| 6.4.3.9 Ensure discretionary access control permission modification events are collected | None | - | No |
| 6.4.3.10 Ensure successful file system mounts are collected | None | - | No |
| 6.4.3.11 Ensure session initiation information is collected | None | - | No |
| 6.4.3.12 Ensure login and logout events are collected | None | - | No |
| 6.4.3.13 Ensure file deletion events by users are collected | None | - | No |
| 6.4.3.14 Ensure events that modify the system's Mandatory Access Controls are collected | None | - | No |
| 6.4.3.15 Ensure successful and unsuccessful attempts to use the chcon command are recorded | None | - | No |
| 6.4.3.16 Ensure successful and unsuccessful attempts to use the setfacl command are recorded | None | - | No |
| 6.4.3.17 Ensure successful and unsuccessful attempts to use the chacl command are recorded | None | - | No |
| 6.4.3.18 Ensure successful and unsuccessful attempts to use the usermod command are recorded | None | - | No |
| 6.4.3.19 Ensure kernel module loading unloading and modification is collected | None | - | No |
| 6.4.3.20 Ensure the audit configuration is immutable | None | - | No |
| 6.4.3.21 Ensure the running and on disk configuration is the same | None | - | No |
| 6.4.4.1 Ensure audit log files mode is configured | None | - | No |
| 6.4.4.2 Ensure audit log files owner is configured | None | - | No |
| 6.4.4.3 Ensure audit log files group owner is configured | None | - | No |
| 6.4.4.4 Ensure the audit log file directory mode is configured | None | - | No |
| 6.4.4.5 Ensure audit configuration files mode is configured | `directory``filePatternConf``mask``filePatternRules` | `/etc/audit/``*.conf``0137``*.rules` | No |
| 6.4.4.6 Ensure audit configuration files owner is configured | `directory``filePatternConf``owner``filePatternRules` | `/etc/audit/``*.conf``root``*.rules` | No |
| 6.4.4.7 Ensure audit configuration files group owner is configured | `directory``filePatternConf``group``filePatternRules` | `/etc/audit/``*.conf``root``*.rules` | No |
| 6.4.4.8 Ensure audit tools mode is configured | `filenameSbinAuditctl``mask``filenameSbinAureport``filenameSbinAusearch``filenameSbinAutrace``filenameSbinAuditd``filenameSbinAugenrules` | `/sbin/auditctl``0022``/sbin/aureport``/sbin/ausearch``/sbin/autrace``/sbin/auditd``/sbin/augenrules` | Yes |
| 6.4.4.9 Ensure audit tools owner is configured | `filenameSbinAuditctl``owner``filenameSbinAureport``filenameSbinAusearch``filenameSbinAutrace``filenameSbinAuditd``filenameSbinAugenrules` | `/sbin/auditctl``root``/sbin/aureport``/sbin/ausearch``/sbin/autrace``/sbin/auditd``/sbin/augenrules` | Yes |
| 6.4.4.10 Ensure audit tools group owner is configured | `filenameSbinAuditctl``group``filenameSbinAureport``filenameSbinAusearch``filenameSbinAutrace``filenameSbinAuditd``filenameSbinAugenrules` | `/sbin/auditctl``root``/sbin/aureport``/sbin/ausearch``/sbin/autrace``/sbin/auditd``/sbin/augenrules` | Yes |
| 7.1.1 Ensure permissions on /etc/passwd are configured | `mask``owner``group` | `0133``root``root` | Yes |
| 7.1.2 Ensure permissions on /etc/passwd- are configured | `mask``owner``group` | `0133``root``root` | Yes |
| 7.1.3 Ensure permissions on /etc/group are configured | `mask``owner``group` | `0133``root``root` | Yes |
| 7.1.4 Ensure permissions on /etc/group- are configured | `mask``owner``group` | `0133``root``root` | Yes |
| 7.1.5 Ensure permissions on /etc/shadow are configured | `mask``owner``group` | `0137``root``root\|shadow` | Yes |
| 7.1.6 Ensure permissions on /etc/shadow- are configured | `mask``owner``group` | `0137``root``root\|shadow` | Yes |
| 7.1.7 Ensure permissions on /etc/gshadow are configured | `mask``owner``group` | `0137``root``shadow\|root` | Yes |
| 7.1.8 Ensure permissions on /etc/gshadow- are configured | `mask``owner``group` | `0137``root``shadow\|root` | Yes |
| 7.1.9 Ensure permissions on /etc/shells are configured | `mask``owner``group` | `0133``root``root` | Yes |
| 7.1.10 Ensure permissions on /etc/security/opasswd are configured | `mask``owner``group` | `0177``root``root` | Yes |
| 7.1.11 Ensure world writable files and directories are secured | None | - | No |
| 7.1.12 Ensure no files or directories without an owner and a group exist | None | - | No |
| 7.1.13 Ensure SUID and SGID files are reviewed | None | - | No |
| 7.2.1 Ensure accounts in /etc/passwd use shadowed passwords | None | - | No |
| 7.2.2 Ensure /etc/shadow password fields are not empty | None | - | No |
| 7.2.3 Ensure all groups in /etc/passwd exist in /etc/group | None | - | No |
| 7.2.4 Ensure shadow group is empty | None | - | No |
| 7.2.5 Ensure no duplicate UIDs exist | None | - | No |
| 7.2.6 Ensure no duplicate GIDs exist | None | - | No |
| 7.2.7 Ensure no duplicate user names exist | None | - | No |
| 7.2.8 Ensure no duplicate group names exist | None | - | No |
| 7.2.9 Ensure local interactive user home directories are configured | None | - | No |
| 7.2.10 Ensure local interactive user dot files access is configured | None | - | No |

### Known assessment discrepancies

Note

These rules may produce assessment results that differ from CIS-CAT® Pro Assessor; our implementation may enforce stricter criteria. A rule is listed once if a discrepancy was observed in any tested scenario.

Comparison data with CIS-CAT Pro Assessor is not available for this benchmark in this release. Assessment differences and unimplemented rules cannot be determined from comparison results.

## CIS Debian Linux 12 Benchmark 1.1.0 Level 1 + Level 2 - Server

### Rules

| Rule | Parameters | Default values | Remediation |
| --- | --- | --- | --- |
| 1.1.1.1 Ensure cramfs kernel module is not available | None | - | Yes |
| 1.1.1.2 Ensure freevxfs kernel module is not available | None | - | Yes |
| 1.1.1.3 Ensure hfs kernel module is not available | None | - | Yes |
| 1.1.1.4 Ensure hfsplus kernel module is not available | None | - | Yes |
| 1.1.1.5 Ensure jffs2 kernel module is not available | None | - | Yes |
| 1.1.1.6 Ensure overlayfs kernel module is not available | None | - | Yes |
| 1.1.1.7 Ensure squashfs kernel module is not available | None | - | Yes |
| 1.1.1.8 Ensure udf kernel module is not available | None | - | Yes |
| 1.1.1.9 Ensure usb-storage kernel module is not available | None | - | Yes |
| 1.1.1.10 Ensure unused filesystems kernel modules are not available | None | - | No |
| 1.1.2.1.1 Ensure /tmp is a separate partition | `mountPoint` | `/tmp` | No |
| 1.1.2.1.2 Ensure nodev option set on /tmp partition | `mountPoint``requiredMountOptions` | `/tmp``nodev` | No |
| 1.1.2.1.3 Ensure nosuid option set on /tmp partition | `mountPoint``requiredMountOptions` | `/tmp``nosuid` | No |
| 1.1.2.1.4 Ensure noexec option set on /tmp partition | `mountPoint``requiredMountOptions` | `/tmp``noexec` | No |
| 1.1.2.2.1 Ensure /dev/shm is a separate partition | `mountPoint` | `/dev/shm` | No |
| 1.1.2.2.2 Ensure nodev option set on /dev/shm partition | `mountPoint``requiredMountOptions` | `/dev/shm``nodev` | No |
| 1.1.2.2.3 Ensure nosuid option set on /dev/shm partition | `mountPoint``requiredMountOptions` | `/dev/shm``nosuid` | No |
| 1.1.2.2.4 Ensure noexec option set on /dev/shm partition | `mountPoint``requiredMountOptions` | `/dev/shm``noexec` | No |
| 1.1.2.3.1 Ensure separate partition exists for /home | `mountPoint` | `/home` | No |
| 1.1.2.3.2 Ensure nodev option set on /home partition | `mountPoint``requiredMountOptions` | `/home``nodev` | No |
| 1.1.2.3.3 Ensure nosuid option set on /home partition | `mountPoint``requiredMountOptions` | `/home``nosuid` | No |
| 1.1.2.4.1 Ensure separate partition exists for /var | `mountPoint` | `/var` | No |
| 1.1.2.4.2 Ensure nodev option set on /var partition | `mountPoint``requiredMountOptions` | `/var``nodev` | No |
| 1.1.2.4.3 Ensure nosuid option set on /var partition | `mountPoint``requiredMountOptions` | `/var``nosuid` | No |
| 1.1.2.5.1 Ensure separate partition exists for /var/tmp | `mountPoint` | `/var/tmp` | No |
| 1.1.2.5.2 Ensure nodev option set on /var/tmp partition | `mountPoint``requiredMountOptions` | `/var/tmp``nodev` | No |
| 1.1.2.5.3 Ensure nosuid option set on /var/tmp partition | `mountPoint``requiredMountOptions` | `/var/tmp``nosuid` | No |
| 1.1.2.5.4 Ensure noexec option set on /var/tmp partition | `mountPoint``requiredMountOptions` | `/var/tmp``noexec` | No |
| 1.1.2.6.1 Ensure separate partition exists for /var/log | `mountPoint` | `/var/log` | No |
| 1.1.2.6.2 Ensure nodev option set on /var/log partition | `mountPoint``requiredMountOptions` | `/var/log``nodev` | No |
| 1.1.2.6.3 Ensure nosuid option set on /var/log partition | `mountPoint``requiredMountOptions` | `/var/log``nosuid` | No |
| 1.1.2.6.4 Ensure noexec option set on /var/log partition | `mountPoint``requiredMountOptions` | `/var/log``noexec` | No |
| 1.1.2.7.1 Ensure separate partition exists for /var/log/audit | `mountPoint` | `/var/log/audit` | No |
| 1.1.2.7.2 Ensure nodev option set on /var/log/audit partition | `mountPoint``requiredMountOptions` | `/var/log/audit``nodev` | No |
| 1.1.2.7.3 Ensure nosuid option set on /var/log/audit partition | `mountPoint``requiredMountOptions` | `/var/log/audit``nosuid` | No |
| 1.1.2.7.4 Ensure noexec option set on /var/log/audit partition | `mountPoint``requiredMountOptions` | `/var/log/audit``noexec` | No |
| 1.2.1.1 Ensure GPG keys are configured | None | - | No |
| 1.2.1.2 Ensure package manager repositories are configured | None | - | No |
| 1.2.2.1 Ensure updates, patches, and additional security software are installed | None | - | No |
| 1.3.1.1 Ensure AppArmor is installed | None | - | No |
| 1.3.1.2 Ensure AppArmor is enabled in the bootloader configuration | None | - | No |
| 1.3.1.3 Ensure all AppArmor Profiles are in enforce or complain mode | None | - | No |
| 1.3.1.4 Ensure all AppArmor Profiles are enforcing | None | - | No |
| 1.4.1 Ensure bootloader password is set | None | - | No |
| 1.4.2 Ensure access to bootloader config is configured | `filename``mask``owner``group` | `/boot/grub/grub.cfg``0177``root``root` | Yes |
| 1.5.1 Ensure address space layout randomization is enabled | None | - | No |
| 1.5.2 Ensure ptrace\_scope is restricted | None | - | No |
| 1.5.3 Ensure core dumps are restricted | None | - | No |
| 1.6.1 Ensure message of the day is configured properly | None | - | No |
| 1.6.2 Ensure local login warning banner is configured properly | None | - | No |
| 1.6.3 Ensure remote login warning banner is configured properly | None | - | No |
| 1.6.4 Ensure access to /etc/motd is configured | None | - | Yes |
| 1.6.5 Ensure access to /etc/issue is configured | `filename``mask``owner``group` | `/etc/issue``0133``root``root` | Yes |
| 1.6.6 Ensure access to /etc/issue.net is configured | None | - | Yes |
| 1.7.1 Ensure GDM is removed | None | - | No |
| 1.7.2 Ensure GDM login banner is configured | None | - | Yes |
| 1.7.3 Ensure GDM disable-user-list option is enabled | None | - | Yes |
| 1.7.4 Ensure GDM screen locks when the user is idle | None | - | No |
| 1.7.5 Ensure GDM screen locks cannot be overridden | None | - | No |
| 1.7.6 Ensure GDM automatic mounting of removable media is disabled | None | - | Yes |
| 1.7.7 Ensure GDM disabling automatic mounting of removable media is not overridden | None | - | No |
| 1.7.8 Ensure GDM autorun-never is enabled | None | - | Yes |
| 1.7.9 Ensure GDM autorun-never is not overridden | None | - | No |
| 1.7.10 Ensure XDMCP is not enabled | None | - | Yes |
| 2.1.1 Ensure autofs services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `autofs.service``enabled``active``autofs` | No |
| 2.1.2 Ensure avahi daemon services are not in use | `unitNameAvahiDaemonService``expectedUnitFileState``expectedActiveState``unitNameAvahiDaemonSocket``packageName` | `avahi-daemon.service``enabled``active``avahi-daemon.socket``avahi-daemon` | No |
| 2.1.3 Ensure dhcp server services are not in use | `unitNameIscDhcpServerService``expectedUnitFileState``expectedActiveState``unitNameIscDhcpServer6Service``packageName` | `isc-dhcp-server.service``enabled``active``isc-dhcp-server6.service``isc-dhcp-server` | No |
| 2.1.4 Ensure dns server services are not in use | `serviceName``expectedUnitFileState``expectedActiveState``packageName` | `named.service``enabled``active``bind9` | No |
| 2.1.5 Ensure dnsmasq services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `dnsmasq.service``enabled``active``dnsmasq` | No |
| 2.1.6 Ensure ftp server services are not in use | `serviceName``expectedUnitFileState``expectedActiveState``packageName` | `vsftpd.service``enabled``active``vsftpd` | No |
| 2.1.7 Ensure ldap server services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `slapd.service``enabled``active``slapd` | No |
| 2.1.8 Ensure message access server services are not in use | `packageNameDovecotImapd``packageNameDovecotPop3d``unitNameDovecotService``expectedUnitFileState``expectedActiveState``unitNameDovecotSocket` | `dovecot-imapd``dovecot-pop3d``dovecot.service``enabled``active``dovecot.socket` | No |
| 2.1.9 Ensure network file system services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `nfs-server.service``enabled``active``nfs-kernel-server` | No |
| 2.1.10 Ensure nis server services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `ypserv.service``enabled``active``ypserv` | No |
| 2.1.11 Ensure print server services are not in use | `unitNameCupsService``expectedUnitFileState``expectedActiveState``unitNameCupsSocket``packageName` | `cups.service``enabled``active``cups.socket``cups` | No |
| 2.1.12 Ensure rpcbind services are not in use | `unitNameRpcbindService``expectedUnitFileState``expectedActiveState``unitNameRpcbindSocket``packageName` | `rpcbind.service``enabled``active``rpcbind.socket``rpcbind` | No |
| 2.1.13 Ensure rsync services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `rsync.service``enabled``active``rsync` | No |
| 2.1.14 Ensure samba file server services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `smbd.service``enabled``active``samba` | No |
| 2.1.15 Ensure snmp services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `snmpd.service``enabled``active``snmpd` | No |
| 2.1.16 Ensure tftp server services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `tftpd-hpa.service``enabled``active``tftpd-hpa` | No |
| 2.1.17 Ensure web proxy server services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `squid.service``enabled``active``squid` | No |
| 2.1.18 Ensure web server services are not in use | `unitNameApache2Service``expectedUnitFileState``expectedActiveState``unitNameApache2Socket``packageNameApache2``unitNameNginxService``packageNameNginx` | `apache2.service``enabled``active``apache2.socket``apache2``nginx.service``nginx` | No |
| 2.1.19 Ensure xinetd services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `xinetd.service``enabled``active``xinetd` | No |
| 2.1.20 Ensure X window server services are not in use | None | - | No |
| 2.1.21 Ensure mail transfer agent is configured for local-only mode | None | - | No |
| 2.1.22 Ensure only approved services are listening on a network interface | None | - | No |
| 2.2.1 Ensure NIS Client is not installed | None | - | No |
| 2.2.2 Ensure rsh client is not installed | None | - | No |
| 2.2.3 Ensure talk client is not installed | None | - | No |
| 2.2.4 Ensure telnet client is not installed | `packageName` | `telnet` | No |
| 2.2.5 Ensure ldap client is not installed | None | - | No |
| 2.2.6 Ensure ftp client is not installed | None | - | No |
| 2.3.1.1 Ensure a single time synchronization daemon is in use | None | - | No |
| 2.3.2.1 Ensure systemd-timesyncd configured with authorized timeserver | None | - | No |
| 2.3.2.2 Ensure systemd-timesyncd is enabled and running | None | - | No |
| 2.3.3.1 Ensure chrony is configured with authorized timeserver | None | - | No |
| 2.3.3.2 Ensure chrony is running as user \_chrony | None | - | No |
| 2.3.3.3 Ensure chrony is enabled and running | None | - | No |
| 2.4.1.1 Ensure cron daemon is enabled and active | None | - | No |
| 2.4.1.2 Ensure permissions on /etc/crontab are configured | `mask``owner``group` | `0177``root``root` | Yes |
| 2.4.1.3 Ensure permissions on /etc/cron.hourly are configured | `mask``owner``group` | `0077``root``root` | Yes |
| 2.4.1.4 Ensure permissions on /etc/cron.daily are configured | `mask``owner``group``packageName``alternativePackageName` | `0077``root``root``cron``cronie` | Yes |
| 2.4.1.5 Ensure permissions on /etc/cron.weekly are configured | `mask``owner``group` | `0077``root``root` | Yes |
| 2.4.1.6 Ensure permissions on /etc/cron.monthly are configured | `mask``owner``group``alternativePackageName` | `0077``root``root``cronie` | Yes |
| 2.4.1.7 Ensure permissions on /etc/cron.d are configured | `mask``owner``group` | `0077``root``root` | Yes |
| 2.4.1.8 Ensure crontab is restricted to authorized users | `filenameEtcCronAllow``owner``group``mask``filenameEtcCronDeny` | `/etc/cron.allow``root``root\|crontab``0137``/etc/cron.deny` | Yes |
| 2.4.2.1 Ensure at is restricted to authorized users | `mask``owner``group` | `0137``root``root\|daemon` | Yes |
| 3.1.1 Ensure IPv6 status is identified | None | - | No |
| 3.1.2 Ensure wireless interfaces are disabled | None | - | No |
| 3.1.3 Ensure bluetooth services are not in use | `unitName``expectedUnitFileState``expectedActiveState``packageName` | `bluetooth.service``enabled``active``bluez` | No |
| 3.2.1 Ensure dccp kernel module is not available | None | - | Yes |
| 3.2.2 Ensure tipc kernel module is not available | None | - | Yes |
| 3.2.3 Ensure rds kernel module is not available | None | - | Yes |
| 3.2.4 Ensure sctp kernel module is not available | None | - | Yes |
| 3.3.1 Ensure ip forwarding is disabled | None | - | No |
| 3.3.2 Ensure packet redirect sending is disabled | None | - | No |
| 3.3.3 Ensure bogus icmp responses are ignored | None | - | No |
| 3.3.4 Ensure broadcast icmp requests are ignored | None | - | No |
| 3.3.5 Ensure icmp redirects are not accepted | None | - | No |
| 3.3.6 Ensure secure icmp redirects are not accepted | None | - | No |
| 3.3.7 Ensure reverse path filtering is enabled | None | - | No |
| 3.3.8 Ensure source routed packets are not accepted | None | - | No |
| 3.3.9 Ensure suspicious packets are logged | None | - | No |
| 3.3.10 Ensure tcp syn cookies is enabled | None | - | No |
| 3.3.11 Ensure ipv6 router advertisements are not accepted | None | - | No |
| 4.1.1 Ensure a single firewall configuration utility is in use | None | - | No |
| 4.2.1 Ensure ufw is installed | None | - | No |
| 4.2.2 Ensure iptables-persistent is not installed with ufw | None | - | No |
| 4.2.3 Ensure ufw service is enabled | None | - | No |
| 4.2.4 Ensure ufw loopback traffic is configured | None | - | No |
| 4.2.5 Ensure ufw outbound connections are configured | None | - | No |
| 4.2.6 Ensure ufw firewall rules exist for all open ports | None | - | No |
| 4.2.7 Ensure ufw default deny firewall policy | None | - | No |
| 4.3.1 Ensure nftables is installed | None | - | No |
| 4.3.2 Ensure ufw is uninstalled or disabled with nftables | None | - | No |
| 4.3.3 Ensure iptables are flushed with nftables | None | - | No |
| 4.3.4 Ensure a nftables table exists | None | - | No |
| 4.3.5 Ensure nftables base chains exist | None | - | No |
| 4.3.6 Ensure nftables loopback traffic is configured | None | - | No |
| 4.3.7 Ensure nftables outbound and established connections are configured | None | - | No |
| 4.3.8 Ensure nftables default deny firewall policy | None | - | No |
| 4.3.9 Ensure nftables service is enabled | None | - | No |
| 4.3.10 Ensure nftables rules are permanent | None | - | No |
| 4.4.1.1 Ensure iptables packages are installed | None | - | No |
| 4.4.1.2 Ensure nftables is not in use with iptables | None | - | No |
| 4.4.1.3 Ensure ufw is not in use with iptables | None | - | No |
| 4.4.2.1 Ensure iptables default deny firewall policy | None | - | No |
| 4.4.2.2 Ensure iptables loopback traffic is configured | None | - | No |
| 4.4.2.3 Ensure iptables outbound and established connections are configured | None | - | No |
| 4.4.2.4 Ensure iptables firewall rules exist for all open ports | None | - | No |
| 4.4.3.1 Ensure ip6tables default deny firewall policy | None | - | No |
| 4.4.3.2 Ensure ip6tables loopback traffic is configured | None | - | No |
| 4.4.3.3 Ensure ip6tables outbound and established connections are configured | None | - | No |
| 4.4.3.4 Ensure ip6tables firewall rules exist for all open ports | None | - | No |
| 5.1.1 Ensure permissions on /etc/ssh/sshd\_config are configured | `mask``owner``group` | `0177``root``root` | Yes |
| 5.1.2 Ensure permissions on SSH private host key files are configured | None | - | No |
| 5.1.3 Ensure permissions on SSH public host key files are configured | None | - | No |
| 5.1.4 Ensure sshd access is configured | `allowUsersValuePattern``allowGroupsValuePattern``denyUsersValuePattern``denyGroupsValuePattern` | `[^ \t]+``[^ \t]+``[^ \t]+``[^ \t]+` | No |
| 5.1.5 Ensure sshd Banner is configured | `bannerExpectedValueT``bannerDisallowedValuesNone` | `\/[^ \t]+``none` | No |
| 5.1.6 Ensure sshd Ciphers are configured | `ciphersDisallowedValues` | `3des-cbc,aes128-cbc,aes192-cbc,aes256-cbc,arcfour,arcfour128,arcfour256,blowfish-cbc,cast128-cbc,rijndael-cbc@lysator\.liu\.se` | No |
| 5.1.7 Ensure sshd ClientAliveInterval and ClientAliveCountMax are configured | `clientalivecountmaxThreshold``clientaliveintervalThreshold` | `0``0` | No |
| 5.1.8 Ensure sshd DisableForwarding is enabled | None | - | No |
| 5.1.9 Ensure sshd GSSAPIAuthentication is disabled | None | - | No |
| 5.1.10 Ensure sshd HostbasedAuthentication is disabled | None | - | No |
| 5.1.11 Ensure sshd IgnoreRhosts is enabled | None | - | No |
| 5.1.12 Ensure sshd KexAlgorithms is configured | `kexalgorithmsDisallowedValues` | `diffie-hellman-group1-sha1,diffie-hellman-group14-sha1,diffie-hellman-group-exchange-sha1` | No |
| 5.1.13 Ensure sshd LoginGraceTime is configured | `logingracetimeThresholdValue60``logingracetimeThresholdValue0` | `60``0` | No |
| 5.1.14 Ensure sshd LogLevel is configured | `loglevelExpectedValue` | `verbose,info` | No |
| 5.1.15 Ensure sshd MACs are configured | `macsDisallowedValues` | `hmac-md5,hmac-md5-96,hmac-ripemd160,hmac-sha1-96,umac-64@openssh\.com,hmac-md5-etm@openssh\.com,hmac-md5-96-etm@openssh\.com,hmac-ripemd160-etm@openssh\.com,hmac-sha1-96-etm@openssh\.com,umac-64-etm@openssh\.com,umac-128-etm@openssh\.com` | No |
| 5.1.16 Ensure sshd MaxAuthTries is configured | `maxauthtriesThreshold` | `4` | No |
| 5.1.17 Ensure sshd MaxSessions is configured | `maxsessionsThreshold` | `10` | No |
| 5.1.18 Ensure sshd MaxStartups is configured | `maxstartupsExpectedValue` | `10:30:60` | No |
| 5.1.19 Ensure sshd PermitEmptyPasswords is disabled | None | - | No |
| 5.1.20 Ensure sshd PermitRootLogin is disabled | None | - | No |
| 5.1.21 Ensure sshd PermitUserEnvironment is disabled | None | - | No |
| 5.1.22 Ensure sshd UsePAM is enabled | None | - | No |
| 5.2.1 Ensure sudo is installed | None | - | No |
| 5.2.2 Ensure sudo commands use pty | None | - | No |
| 5.2.3 Ensure sudo log file exists | None | - | No |
| 5.2.4 Ensure users must provide password for privilege escalation | None | - | No |
| 5.2.5 Ensure re-authentication for privilege escalation is not disabled globally | None | - | No |
| 5.2.6 Ensure sudo authentication timeout is configured correctly | None | - | No |
| 5.2.7 Ensure access to the su command is restricted | None | - | No |
| 5.3.1.1 Ensure latest version of pam is installed | None | - | No |
| 5.3.1.2 Ensure libpam-modules is installed | None | - | No |
| 5.3.1.3 Ensure libpam-pwquality is installed | None | - | No |
| 5.3.2.1 Ensure pam\_unix module is enabled | None | - | No |
| 5.3.2.2 Ensure pam\_faillock module is enabled | None | - | No |
| 5.3.2.3 Ensure pam\_pwquality module is enabled | None | - | No |
| 5.3.2.4 Ensure pam\_pwhistory module is enabled | None | - | No |
| 5.3.3.1.1 Ensure password failed attempts lockout is configured | None | - | No |
| 5.3.3.1.2 Ensure password unlock time is configured | None | - | No |
| 5.3.3.1.3 Ensure password failed attempts lockout includes root account | None | - | No |
| 5.3.3.2.1 Ensure password number of changed characters is configured | None | - | No |
| 5.3.3.2.2 Ensure minimum password length is configured | None | - | No |
| 5.3.3.2.3 Ensure password complexity is configured | None | - | No |
| 5.3.3.2.4 Ensure password same consecutive characters is configured | None | - | No |
| 5.3.3.2.5 Ensure password maximum sequential characters is configured | None | - | No |
| 5.3.3.2.6 Ensure password dictionary check is enabled | None | - | No |
| 5.3.3.2.7 Ensure password quality checking is enforced | None | - | No |
| 5.3.3.2.8 Ensure password quality is enforced for the root user | None | - | No |
| 5.3.3.3.1 Ensure password history remember is configured | None | - | No |
| 5.3.3.3.2 Ensure password history is enforced for the root user | None | - | No |
| 5.3.3.3.3 Ensure pam\_pwhistory includes use\_authtok | None | - | No |
| 5.3.3.4.1 Ensure pam\_unix does not include nullok | None | - | No |
| 5.3.3.4.2 Ensure pam\_unix does not include remember | None | - | No |
| 5.3.3.4.3 Ensure pam\_unix includes a strong password hashing algorithm | None | - | No |
| 5.3.3.4.4 Ensure pam\_unix includes use\_authtok | None | - | No |
| 5.4.1.1 Ensure password expiration is configured | `maxDays``minDays` | `365``1` | Yes |
| 5.4.1.2 Ensure minimum password days is configured | `minDays` | `1` | No |
| 5.4.1.3 Ensure password expiration warning days is configured | `warnDays` | `7` | Yes |
| 5.4.1.4 Ensure strong password hashing algorithm is configured | `hashAlgorithm``fallbackHashAlgorithm` | `YESCRYPT``SHA512` | Yes |
| 5.4.1.5 Ensure inactive password lock is configured | None | - | No |
| 5.4.1.6 Ensure all users last password change date is in the past | None | - | No |
| 5.4.2.1 Ensure root is the only UID 0 account | None | - | No |
| 5.4.2.2 Ensure root is the only GID 0 account | None | - | No |
| 5.4.2.3 Ensure group root is the only GID 0 group | None | - | No |
| 5.4.2.4 Ensure root account access is controlled | None | - | No |
| 5.4.2.5 Ensure root path integrity | None | - | No |
| 5.4.2.6 Ensure root user umask is configured | None | - | No |
| 5.4.2.7 Ensure system accounts do not have a valid login shell | None | - | No |
| 5.4.2.8 Ensure accounts without a valid login shell are locked | None | - | No |
| 5.4.3.1 Ensure nologin is not listed in /etc/shells | None | - | No |
| 5.4.3.2 Ensure default user shell timeout is configured | None | - | Yes |
| 5.4.3.3 Ensure default user umask is configured | None | - | Yes |
| 6.1.1.1 Ensure journald service is enabled and active | None | - | No |
| 6.1.1.2 Ensure journald log file access is configured | None | - | No |
| 6.1.1.3 Ensure journald log file rotation is configured | None | - | No |
| 6.1.1.4 Ensure only one logging system is in use | None | - | No |
| 6.1.2.1.1 Ensure systemd-journal-remote is installed | None | - | No |
| 6.1.2.1.2 Ensure systemd-journal-upload authentication is configured | None | - | No |
| 6.1.2.1.3 Ensure systemd-journal-upload is enabled and active | None | - | No |
| 6.1.2.1.4 Ensure systemd-journal-remote service is not in use | None | - | No |
| 6.1.2.2 Ensure journald ForwardToSyslog is disabled | `forwardToSyslogRegex` | `no` | No |
| 6.1.2.3 Ensure journald Compress is configured | `compressRegex` | `yes` | No |
| 6.1.2.4 Ensure journald Storage is configured | `storageRegex` | `persistent` | No |
| 6.1.3.1 Ensure rsyslog is installed | None | - | No |
| 6.1.3.2 Ensure rsyslog service is enabled and active | None | - | No |
| 6.1.3.3 Ensure journald is configured to send logs to rsyslog | `forwardToSyslogRegex` | `yes` | No |
| 6.1.3.4 Ensure rsyslog log file creation mode is configured | None | - | No |
| 6.1.3.5 Ensure rsyslog logging is configured | None | - | No |
| 6.1.3.6 Ensure rsyslog is configured to send logs to a remote log host | None | - | No |
| 6.1.3.7 Ensure rsyslog is not configured to receive logs from a remote client | None | - | No |
| 6.1.3.8 Ensure logrotate is configured | None | - | No |
| 6.1.4.1 Ensure access to all logfiles has been configured | None | - | No |
| 6.2.1.1 Ensure auditd packages are installed | None | - | No |
| 6.2.1.2 Ensure auditd service is enabled and active | None | - | No |
| 6.2.1.3 Ensure auditing for processes that start prior to auditd is enabled | None | - | No |
| 6.2.1.4 Ensure audit\_backlog\_limit is sufficient | None | - | No |
| 6.2.2.1 Ensure audit log storage size is configured | None | - | No |
| 6.2.2.2 Ensure audit logs are not automatically deleted | None | - | No |
| 6.2.2.3 Ensure system is disabled when audit logs are full | None | - | No |
| 6.2.2.4 Ensure system warns when audit logs are low on space | None | - | No |
| 6.2.3.1 Ensure changes to system administration scope (sudoers) is collected | None | - | No |
| 6.2.3.2 Ensure actions as another user are always logged | None | - | No |
| 6.2.3.3 Ensure events that modify the sudo log file are collected | None | - | No |
| 6.2.3.4 Ensure events that modify date and time information are collected | None | - | No |
| 6.2.3.5 Ensure events that modify the system's network environment are collected | None | - | No |
| 6.2.3.6 Ensure use of privileged commands are collected | None | - | No |
| 6.2.3.7 Ensure unsuccessful file access attempts are collected | None | - | No |
| 6.2.3.8 Ensure events that modify user/group information are collected | None | - | No |
| 6.2.3.9 Ensure discretionary access control permission modification events are collected | None | - | No |
| 6.2.3.10 Ensure successful file system mounts are collected | None | - | No |
| 6.2.3.11 Ensure session initiation information is collected | None | - | No |
| 6.2.3.12 Ensure login and logout events are collected | None | - | No |
| 6.2.3.13 Ensure file deletion events by users are collected | None | - | No |
| 6.2.3.14 Ensure events that modify the system's Mandatory Access Controls are collected | None | - | No |
| 6.2.3.15 Ensure successful and unsuccessful attempts to use the chcon command are collected | None | - | No |
| 6.2.3.16 Ensure successful and unsuccessful attempts to use the setfacl command are collected | None | - | No |
| 6.2.3.17 Ensure successful and unsuccessful attempts to use the chacl command are collected | None | - | No |
| 6.2.3.18 Ensure successful and unsuccessful attempts to use the usermod command are collected | None | - | No |
| 6.2.3.19 Ensure kernel module loading unloading and modification is collected | None | - | No |
| 6.2.3.20 Ensure the audit configuration is immutable | None | - | No |
| 6.2.3.21 Ensure the running and on disk configuration is the same | None | - | No |
| 6.2.4.1 Ensure audit log files mode is configured | None | - | No |
| 6.2.4.2 Ensure audit log files owner is configured | None | - | No |
| 6.2.4.3 Ensure audit log files group owner is configured | None | - | No |
| 6.2.4.4 Ensure the audit log file directory mode is configured | None | - | No |
| 6.2.4.5 Ensure audit configuration files mode is configured | `directory``filePatternConf``mask``filePatternRules` | `/etc/audit/``*.conf``0137``*.rules` | No |
| 6.2.4.6 Ensure audit configuration files owner is configured | `directory``filePatternConf``owner``filePatternRules` | `/etc/audit/``*.conf``root``*.rules` | No |
| 6.2.4.7 Ensure audit configuration files group owner is configured | `directory``filePatternConf``group``filePatternRules` | `/etc/audit/``*.conf``root``*.rules` | No |
| 6.2.4.8 Ensure audit tools mode is configured | `filenameSbinAuditctl``mask``filenameSbinAureport``filenameSbinAusearch``filenameSbinAutrace``filenameSbinAuditd``filenameSbinAugenrules` | `/sbin/auditctl``0022``/sbin/aureport``/sbin/ausearch``/sbin/autrace``/sbin/auditd``/sbin/augenrules` | Yes |
| 6.2.4.9 Ensure audit tools owner is configured | `filenameSbinAuditctl``owner``filenameSbinAureport``filenameSbinAusearch``filenameSbinAutrace``filenameSbinAuditd``filenameSbinAugenrules` | `/sbin/auditctl``root``/sbin/aureport``/sbin/ausearch``/sbin/autrace``/sbin/auditd``/sbin/augenrules` | Yes |
| 6.2.4.10 Ensure audit tools group owner is configured | `filenameSbinAuditctl``group``filenameSbinAureport``filenameSbinAusearch``filenameSbinAutrace``filenameSbinAuditd``filenameSbinAugenrules` | `/sbin/auditctl``root``/sbin/aureport``/sbin/ausearch``/sbin/autrace``/sbin/auditd``/sbin/augenrules` | Yes |
| 6.3.1 Ensure AIDE is installed | None | - | No |
| 6.3.2 Ensure filesystem integrity is regularly checked | None | - | No |
| 6.3.3 Ensure cryptographic mechanisms are used to protect the integrity of audit tools | None | - | Yes |
| 7.1.1 Ensure permissions on /etc/passwd are configured | `mask``owner``group` | `0133``root``root` | Yes |
| 7.1.2 Ensure permissions on /etc/passwd- are configured | `mask``owner``group` | `0133``root``root` | Yes |
| 7.1.3 Ensure permissions on /etc/group are configured | `mask``owner``group` | `0133``root``root` | Yes |
| 7.1.4 Ensure permissions on /etc/group- are configured | `mask``owner``group` | `0133``root``root` | Yes |
| 7.1.5 Ensure permissions on /etc/shadow are configured | `mask``owner``group` | `0137``root``root\|shadow` | Yes |
| 7.1.6 Ensure permissions on /etc/shadow- are configured | `mask``owner``group` | `0137``root``root\|shadow` | Yes |
| 7.1.7 Ensure permissions on /etc/gshadow are configured | `mask``owner``group` | `0137``root``shadow\|root` | Yes |
| 7.1.8 Ensure permissions on /etc/gshadow- are configured | `mask``owner``group` | `0137``root``shadow\|root` | Yes |
| 7.1.9 Ensure permissions on /etc/shells are configured | `mask``owner``group` | `0133``root``root` | Yes |
| 7.1.10 Ensure permissions on /etc/security/opasswd are configured | `mask``owner``group` | `0177``root``root` | Yes |
| 7.1.11 Ensure world writable files and directories are secured | None | - | No |
| 7.1.12 Ensure no files or directories without an owner and a group exist | None | - | No |
| 7.1.13 Ensure SUID and SGID files are reviewed | None | - | No |
| 7.2.1 Ensure accounts in /etc/passwd use shadowed passwords | None | - | No |
| 7.2.2 Ensure /etc/shadow password fields are not empty | None | - | No |
| 7.2.3 Ensure all groups in /etc/passwd exist in /etc/group | None | - | No |
| 7.2.4 Ensure shadow group is empty | None | - | No |
| 7.2.5 Ensure no duplicate UIDs exist | None | - | No |
| 7.2.6 Ensure no duplicate GIDs exist | None | - | No |
| 7.2.7 Ensure no duplicate user names exist | None | - | No |
| 7.2.8 Ensure no duplicate group names exist | None | - | No |
| 7.2.9 Ensure local interactive user home directories are configured | None | - | No |
| 7.2.10 Ensure local interactive user dot files access is configured | None | - | No |

### Known assessment discrepancies

Note

These rules may produce assessment results that differ from CIS-CAT® Pro Assessor; our implementation may enforce stricter criteria. A rule is listed once if a discrepancy was observed in any tested scenario.

No discrepancies found among compared rules.
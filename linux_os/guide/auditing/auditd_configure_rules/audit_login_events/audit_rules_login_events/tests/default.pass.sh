#!/bin/bash
# packages = audit
# variables = var_accounts_passwords_pam_faillock_dir=/var/log/faillock

echo "-w /var/log/faillock -p wa -k logins" >> /etc/audit/rules.d/logins.rules
echo "-w /var/log/lastlog -p wa -k logins" >> /etc/audit/rules.d/logins.rules
echo "-w /var/log/tallylog -p wa -k logins" >> /etc/audit/rules.d/logins.rules

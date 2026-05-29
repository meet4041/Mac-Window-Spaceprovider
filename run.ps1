param(
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$Args
)
#
# Minimal PowerShell launcher for Safe Mac Cleaner
# Usage:
#   .\run.ps1 arg1 arg2

python -m script @Args

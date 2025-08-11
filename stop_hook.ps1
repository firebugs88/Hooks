$input | ConvertFrom-Json | ForEach-Object { 
    $logLine = (Get-Date -Format 'yyyy-MM-dd HH:mm:ss') + ' | Stop event triggered | Session: ' + $_.session_id
    Add-Content -Path "C:\Users\User\Desktop\mis-hooks\.claude\claude_stop_log.txt" -Value $logLine 
}
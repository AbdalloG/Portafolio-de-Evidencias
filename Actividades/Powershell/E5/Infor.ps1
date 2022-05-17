Import-Module 'C:\Program Files\WindowsPowerShell\Modules\Info\InfoM.psm1' -Verbose
Function showmenu {
    Clear-Host
    Write-Host "1. Usuarios"
    Write-Host "2. OS Specs"
    Write-Host "3. Hardware Specs"
    Write-Host "4. PortScaner"
    Write-Host "5. Exit"
}
 
showmenu
 
while(($inp = Read-Host -Prompt "Select an option") -ne "5"){
 
switch($inp){
        1 {
            Users #https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/get-localgroup?view=powershell-5.1
            pause;
            break
        }
        2 {
            OSpecs #https://docs.microsoft.com/es-es/powershell/scripting/samples/collecting-information-about-computers?view=powershell-7.2 
            pause; 
            break
        }
        3 {
            HardW #https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-5.1
            pause;
            break
            }
        4 {
            PortScan #https://docs.microsoft.com/es-es/powershell/scripting/samples/performing-networking-tasks?view=powershell-7.2
            pause;
            break
            }
        5 {"Exit"; break}
        default {Write-Host  "Opcion Invaida.";pause}
        
    }
 
showmenu
}
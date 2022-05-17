function Users{
    $strComputer = $env:COMPUTERNAME
    $computer = [ADSI]("WinNT://" + $strComputer + ",computer")
    $Group = $computer.psbase.children.find("Administradores")
    $members= $Group.psbase.invoke("Members") | %{$_.GetType().InvokeMember("Name", 'GetProperty', $null, $_, $null)}
    Write-Host "Usuarios Administradores: "
    $members
}
function OSpecs{
    $env:username
    Write-Host "Nombre de la PC: $env:COMPUTERNAME"
    Write-Host "Sistema Operativo:" (Get-WMIObject win32_operatingsystem).name
    Write-Host "Tipo de Arquitectura:"(Get-WmiObject Win32_OperatingSystem).OSArchitecture
}
function HardW{
    Get-WmiObject -class "Win32_Processor" | % {
        Write-Host "CPU ID: " $_.DeviceID
        Write-Host "CPU Model: " $_.Name
        Write-Host "CPU Cores: " $_.NumberOfCores
        Write-Host "CPU Max Speed: " $_.MaxClockSpeed
        Write-Host "CPU Status:  " $_.Status
        Write-Host
    }
}
function PortScan{
    $SP = Read-Host "Puerto Inicial: "
    $FP = Read-Host "Puerto Final: "
    $IP = (Get-NetIPAddress -AddressFamily IPV4 -InterfaceAlias Ethernet).IPAdress
    $SP..$FP | % {echo ((new-object Net.Sockets.TcpClient).Connect("$IP",$_)) "Port $_ is open!"} 2>$null
}
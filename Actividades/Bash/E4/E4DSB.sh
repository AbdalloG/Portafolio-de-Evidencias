#! /bin/bash

if type -t wevtutil &> /dev/null 
then 
    OS=MSWin 
elif type -t scutil &> /dev/null 
then 
    OS=macOS 
else 
    OS=Linux 
fi 
echo $OS >> Scan.txt

firstport=22
lastport=80
function portscan(){ 
for ((counter=$firstport; counter<=$lastport; counter++)) 
do 
    (echo >/dev/tcp/$linea/$counter) > /dev/null 2>&1 && echo "$counter open" 
done 
} 

while IFS= read -r linea
do
    portscan '$linea' >> Scan.txt
done < IPs.txt
#!/bin/bash  

if [ $# -ne 2 ]
    then echo "Usage: ./gethostsbyasn.sh [ASN number without 'AS' prefix] [--get-ip/--get-hosts]"
    exit
fi

ASN=$1

function getCidr() {
    cidr=`curl "https://api.bgpview.io/asn/$ASN/prefixes" -s | jq '.data.ipv4_prefixes | .[].prefix' | sed -e 's/^"//' -e 's/"$//'`
}

function getIpFromCidr() {
    getCidr
    for i in $(echo $cidr)
    do
        ipw=$(echo $i | cut -d '.' -f 1)
        ipx=$(echo $i | cut -d '.' -f 2)
        ipy=$(echo $i | cut -d '.' -f 3)
        ipz=$(echo $i | cut -d '.' -f 4 | awk -F '/' '{ print $1 }')
        mask=$(echo $i | awk -F '/' '{print $2}')
        
        IFS='<br>'
        for i in $(curl -s 'http://magic-cookie.co.uk/cgi-bin/iplist-cgi.pl' -H 'Connection: keep-alive' -H 'Cache-Control: max-age=0' -H 'Origin: http://magic-cookie.co.uk' -H 'Upgrade-Insecure-Requests: 1' -H 'Content-Type: application/x-www-form-urlencoded' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' -H 'Referer: http://magic-cookie.co.uk/iplist.html' -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' --data "ipw=$ipw&ipx=$ipx&ipy=$ipy&ipz=$ipz&mask=$mask&submitbutton=List+addresses" --compressed --insecure)
            do
                echo $i | awk '/^[0-9]{1,3}(\.[0-9]{1,3}){3}$/'
            done
    done
}

function getHostsFromIp() {
    getCidr
    IFS=$'\n'
    for i in $(cat /tmp/ip);
        do 
            host $i | grep "domain name pointer" | awk '{print $5}' | sed -e 's/.$//'
        done
}

case $2 in
    "--get-hosts") getIpFromCidr > /tmp/ip; getHostsFromIp; rm /tmp/ip;;
    "--get-ip") getIpFromCidr;;
    "*") echo "Usage: ./gethostsbyasn.sh [ASN number without 'AS' prefix] [--get-ip/--get-hosts]";;
esac
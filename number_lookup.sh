#!/bin/bash
#Powered by xLit
cyan='\033[0;36m'
green='\e[92m'
red='\033[0;31m'
ijo="\e[92m"
putih="\e[97m"
apikey="cb19814b86164e24b738ee07fb2332a8"
function ngecek() {
  check=`curl -s -X GET \
   --header "Content-Type: application/json" \
   --header "Accept: application/json" \
   --header "Authorization: Bearer KEY0181A421398B13602AE34B6C694C2B0C_9CJlytbbA5aIbHD0Q55rTc" \
   "https://api.telnyx.com/v2/number_lookup/1$1?type=carrier&type=caller-name" --compressed | jq .data.portability.spid_carrier_name`
        if [[ "$check" == "" ]] || [[ "$check" == "null" ]]; then
                echo "$1 => GA BENER ANJING!  => $check"
        elif [[ "$check" =~ "T-MOBILE" ]]; then
                echo "$1 => Carrier => $check"
                echo "$1 => Carrier => $check" >> TMOBILE.txt
        elif [[ "$check" =~ "VERIZON" ]]; then
                echo "$1 => Carrier => $check"
                echo "$1 => Carrier => $check" >> Verizon.txt
        else
                echo "$1 => Carrier => $check"
                echo "$1 => Carrier => $check" >> carrier_lookup.txt
        fi
}
read -p "Your Email : " email
persend="30"
delay=""
hitung=0
 
IFS=$'\r\n' GLOBIGNORE='*' command eval 'list=($(cat $email))'
for (( i = 0; i <"${#list[@]}"; i++ )); do
  emails="${list[$i]}"
  ngesend=$(expr $hitung % $persend)
  if [[ $ngesend == 0 && $hitung > 0 ]]; then
    sleep $delay
  fi
 
  ngecek $emails &
    hitung=$[$hitung+1]
done
wait




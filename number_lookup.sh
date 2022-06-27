#!/bin/bash
#rois ganteng
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
   --header "Authorization: Bearer KEY0181842FC47E171B85AF3891804A9093_vn8shTx5d6fIHWKW6R9IC7" \
   "https://api.telnyx.com/v2/number_lookup/$1?type=carrier&type=caller-name" --compressed | jq .data.portability.spid_carrier_name`
        if [[ "$check" == "" ]] || [[ "$check" == "null" ]]; then
                echo "$1 => GA BENER ANJING ! = $check"
        else
                echo "$1 => Carrier => $check"
                echo "$1 => Carrier => $check" >> carrier_lookup.txt
        fi
}
read -p "Your list : " email
persend="50"
delay="2"
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




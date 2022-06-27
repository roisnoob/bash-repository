read -p "Your domain : " masookk
for domain in $(cat $masookk);do
    user=`shuf -i 0-50 -n1`
    domains=`echo $domain`
    userz=`echo shrt$user`
    whmapi1 --output=jsonpretty \
    createacct \
    username=$userz \
    domain=$domains
done
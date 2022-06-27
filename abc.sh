read -p "Masukan Nama File : " sontolz
for i in $(cat $sontolz);do
	echo "

	{
		host	:	\"smtp.office365.com\",
		port	:	\"587\",
		auth	:	true,
		user	:	\"$i\",
		pass	:	\"Badut123\",
		mail	:	\"$i\"
	},
	" >> config.txt
echo "Plase Wait . . . .";sleep 0.3
done
sed -i 's/\r//g' config.txt
echo "Done : config.txt :)"
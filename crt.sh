curl "https://crt.sh/?q=%25.$1" | grep "<TD>" | grep $1 | cut -d ">" -f 2 | cut -d "<" -f 1 | sort | uniq

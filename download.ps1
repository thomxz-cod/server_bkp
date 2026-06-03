$websitecom = "http://192.168.127.132:8080/"
$res = Invoke-WebRequest $websitecom

foreach ($i in $res.links | foreach {[URI]::new([URI]$websitecom, $_.href).AbsoluteUri}){
    curl.exe -O $i
}

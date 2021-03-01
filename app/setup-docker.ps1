$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath

Set-Location $dir

docker build -t weather-buddy .
docker run --name weather-buddy-app -p 5000:5000 weather-buddy

docker kill weather-buddy-app
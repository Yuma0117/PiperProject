
#!/bin/sh
fn=$(date +%Y%m%d%H%M%S)
raspistill -o /home/pi/YO/pics/evidence.jpg -t 1000
#video = ${fn}.h264
#MP4Box -fps 30 -add $video ${fn}.mp4

raspivid -o /home/pi/YO/movie/data.h264 -t 10000
MP4Box -fps 30 -add /home/pi/YO/movie/data.h264 /home/pi/YO/movie/${fn}.mp4


sleep 10
rm -f /home/pi/YO/movie/data.h264

curl -X POST -H "Authorization: Bearer $LINE_ACCESS_TOKEN" -F 'message=煽られています。いざというときのエビデンス' -F 'imageFile=@/home/pi/YO/pics/evidence.jpg' https://notify-api.line.me/api/notify
rm -f /home/pi/YO/pics/evidence.jpg

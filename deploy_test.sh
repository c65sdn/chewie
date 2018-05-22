ssh $1 'rm -r /tmp/chewie'
scp -rq ./*.py $1:/tmp/
scp -rq ./chewie $1:/tmp/
ssh -t $1 'docker stop chewie;\
           docker rm chewie;\
           docker run --cap-add=ALL\ --name chewie\
           --network wpasupplicant-net --ip 172.23.0.112\
           -v /tmp:/tmp -it chewie python3 /tmp/run.py;\
           sleep 1; docker ps -a'
#ssh -t $1 'cd /tmp; sudo python3 run.py'

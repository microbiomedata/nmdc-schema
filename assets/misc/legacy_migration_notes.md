1. create a 24-hour ssh key wiht NERSC sshproxy
1. ssh -i ~/.ssh/nersc -L27777:mongo-loadbalancer.nmdc.production.svc.spin.nersc.org:27017 -o ServerAliveInterval=60 mam@dtn01.nersc.gov

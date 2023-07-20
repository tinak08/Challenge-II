# Challenge-II
 This repository has code for the challenge II : To query the ec2 instance metadata from within the instance.
 Querying the ec2 metatdata relies mainly on the service IMDS ( Instance metatdata service) which works mainly on the request and response.
 But recently with the new upgrade, the IMDSV2 is by default set as required when a new instance is created.
 It works on the TOKEN based authentication.
 Following is the command for both the approaches :
 IMDS : 
 curl http://169.254.169.254/latest/meta-data/    
 IMDSV2 :
 TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/   

In case we need to set the IMDS as the desired way to retrieve the data , we can make the following changes in the instance : 

![image](https://github.com/tinak08/Challenge-II/assets/20789670/12830636-64d4-48f4-9777-9396eedd571f)


I have set up the code on the basis of IMDS and the output is getting displayed in json format.


Also setup a small utility(shell scripting)to retrieve the metadata information for any particular key
It first displays the list of keys , reads any key input from the user and then displays the information.

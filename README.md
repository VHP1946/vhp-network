# General parts of OUR template
- Our template currently launches 6 EC2 instances. It automatically sets thier security groups, alarms, and private IP addresses. It features a public and private subnet with a NAT gateway and elastic IP associated with with webserver instance. 

# Specific Configs
## deploy-me.yml file should look something like this:

### template-file-path: vhp-network-launch.yml
### parameters: 
###   keypairName: "christian-key"
###   instanceType: t2.micro
###   environment: dev
### tags: {}

# Procedure
- In the deploy-me.yml file on the main branch, make sure to include what parameters you'd like to use. (Values cannot be null)

- To change AMIs you would like to use, go to the parameters folder and open the amiMap file. Replace the AMI IDs you would like to use with the ones that are in the file.


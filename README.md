# General parts of OUR template
- Our template currently launches 6 EC2 instances. It automatically sets thier security groups, alarms, and private IP addresses. It features a public and private subnet with a NAT gateway and elastic IP associated with with webserver instance. 

# Specific Configs
## deploy-net.yml file should look something like this:

### template-file-path: ./vhp-network-launch.yml
### parameters: 
###   keypairName: "christian-key"
###   instanceType: t2.micro
###   environment: dev
### tags: {}

# Procedure
- In the deploy-net.yml file on the main branch, make sure to include what parameters you'd like to use. (Values cannot be null)

- To change AMIs you would like to use, go to the parameters folder and open the amiMap file. Replace the AMI IDs you would like to use with the ones that are in the file.

## Steps to deploy our VHP network through cloudformation. 

1. Go to AWS website and navigate to cloudformation. (Make sure you are in the region you’d like to create your network in)

2. In cloudformation select create stack. Select “with new resources.”

3. Choose “template is ready” and “sync from git” options in the create stack page. Click next. 

4. Enter a name for your stack, Choose “I am providing my own file in my repository.” Select your linked repository and the branch you’d like to pull your deploy from. Create a new IAM role. In deployment file parameters put the name of the deployment file in the repository, ours currently is “deploy-net.yml.” Click next.

5. assign a IAM role that gives enough permissions to create the stack. Select roll back all stack resources and delete all newly created resources. Click next.

6. Review and click submit.
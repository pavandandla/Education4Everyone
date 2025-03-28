from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct
from aws_cdk import aws_iam as iam
import os

class EC2Stack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc(self, "MyVpc", max_azs=2)

        security_group = ec2.SecurityGroup(
            self, "WebServerSG", vpc=vpc, allow_all_outbound=True
        )
        security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(22), "Allow SSH access"
        )
        security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(80), "Allow HTTP access"
        )
         # Allow HTTP access only from the EC2 instance itself (dynamic IP)
        security_group.add_ingress_rule(
            ec2.Peer.ipv4(), ec2.Port.tcp(30325), "Allow Kubernetes from EC2 only"
        )

        # Use the existing IAM role ARN
        existing_role_arn = ('arn:aws:iam::288761772602:role/dsp-user')

        # Create an IAM role from the existing ARN
        existing_role = iam.Role.from_role_arn(self, "ExistingRole", existing_role_arn)

        key_pair_name = "test-learn"

        ec2_instance = ec2.Instance(
            self, "EC2Instance",
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            security_group=security_group,
            role=existing_role,
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.LARGE),
            machine_image=ec2.GenericLinuxImage({"us-east-1": "ami-084568db4383264d4"}),
            key_pair=ec2.KeyPair.from_key_pair_name(self, "KeyPair", key_pair_name),
        )

         # Fetch the public IP dynamically
        #ec2_public_ip = ec2_instance.instance_public_ip

        # Allow HTTP access only from the EC2 instance itself (dynamic IP)
        #security_group.add_ingress_rule(
            #ec2.Peer.ipv4(f"{ec2_public_ip}/32"), ec2.Port.tcp(30325), "Allow HTTP from EC2 only"
       # )
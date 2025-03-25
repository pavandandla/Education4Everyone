from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    CfnOutput
)
from constructs import Construct  

class EC2Stack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # 1. Reference existing EC2 instance
        instance = ec2.Instance.from_instance_attributes(
            self, "ExistingInstance",
            instance_id="i-06a682ac329b5a73a",  
            security_group=ec2.SecurityGroup.from_security_group_id(
                self, "SecurityGroup", "sg-0f9cd5dedbf2c1b44"  
            ),
        )

        # 3. Outputs
        CfnOutput(
            self, "InstancePublicIP",
            value=instance.instance_public_ip,
            description="Public IP address of the EC2 instance"
        )

from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    CfnOutput
)
from constructs import Construct  

class EC2Stack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Reference existing VPC (modify if needed)
        vpc = ec2.Vpc.from_lookup(self, "VPC", is_default=True)

        # Reference existing EC2 instance correctly
        instance = ec2.Instance.from_instance_attributes(
            self, "MyInstance",
            instance_id="i-06a682ac329b5a73a",
            vpc=vpc
        )

        # Output instance public IP
        CfnOutput(
            self, "InstancePublicIP",
            value=instance.instance_public_ip,
            description="Public IP address of the EC2 instance"
        )

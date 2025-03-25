from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    CfnOutput
)
from constructs import Construct  

class EC2Stack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # ✅ Reference an existing VPC (Make sure the account and region are set in app.py)
        vpc = ec2.Vpc.from_lookup(self, "VPC", is_default=True)

        # ✅ Reference an existing EC2 instance
        instance = ec2.Instance.from_lookup(self, "MyInstance", instance_id="i-06a682ac329b5a73a")

        # ✅ Output the Public IP of the referenced EC2 instance
        CfnOutput(
            self, "InstancePublicIP",
            value=instance.instance_public_ip,
            description="Public IP address of the EC2 instance"
        )

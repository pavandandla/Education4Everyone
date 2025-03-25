from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,  # Import IAM if needed for future enhancements
    CfnOutput
)
from constructs import Construct  # Import Construct for scope typing

class EC2Stack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # 1. Reference existing EC2 instance
        instance = ec2.Instance.from_instance_id(
            self, "ExistingInstance",
            instance_id="i-06a682ac329b5a73a"  # Replace with your instance ID
        )

        # 2. Add security group rules
        instance.connections.allow_from_any_ipv4(
            ec2.Port.tcp(5001), "Allow incoming traffic on port 5001"
        )

        # 3. Outputs
        CfnOutput(
            self, "InstancePublicIP",
            value=instance.instance_public_ip,
            description="Public IP address of the EC2 instance"
        )

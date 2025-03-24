from aws_cdk import (
    core,
    aws_ec2 as ec2,
    aws_iam as iam,
)

class EC2Stack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # 1. Reference existing EC2 instance
        instance = ec2.Instance.from_instance_attributes(
            self, "ExistingInstance",
            instance_id="i-1234567890abcdef0",  # Replace with your instance ID
            availability_zone="us-east-1a"  # Replace with your instance's AZ
        )

        # 3. Add security group rules
        instance.connections.allow_from_any_ipv4(
            ec2.Port.tcp(5001), "Allow incoming traffic on port 5001"
        )

        # 4. Outputs
        new_output = core.CfnOutput(
            self, "InstancePublicIP",
            value=instance.instance_public_ip,
            description="Public IP address of the EC2 instance"
        )

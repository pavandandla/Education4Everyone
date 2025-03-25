from aws_cdk import (
    core,
    aws_ec2 as ec2,
    aws_iam as iam,
)

class EC2Stack(core.Stack):
    def __init__(self, scope: core.Stack, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # 1. Reference existing EC2 instance
        instance = ec2.Instance.from_instance_attributes(
            self, "ExistingInstance",
            instance_id="i-06a682ac329b5a73a",  # Replace with your instance ID
            availability_zone="us-east-1"  # Replace with your instance's AZ
        )

        # 2. Add security group rules
        instance.connections.allow_from_any_ipv4(
            ec2.Port.tcp(5001), "Allow incoming traffic on port 5001"
        )

        # 3. Outputs
        core.CfnOutput(
            self, "InstancePublicIP",
            value=instance.instance_public_ip.apply(lambda ip: ip if ip else "N/A"),
            description="Public IP address of the EC2 instance"
        )

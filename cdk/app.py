from aws_cdk import core
from cdk.lib.ec2_stack import EC2Stack

app = core.App()
EC2Stack(app, "EC2Stack")

app.synth()

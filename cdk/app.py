"""from aws_cdk import App
from lib.ec2_stack import EC2Stack 

app = App()
EC2Stack(app, "EC2Stack")
app.synth()"""

#!/usr/bin/env python3
import aws_cdk as cdk
from lib.ec2_stack import EC2Stack

app = cdk.App()

# Set AWS environment explicitly
env = cdk.Environment(
    account="288761772602",
    region="us-east-1"  # Replace with your AWS region
)

EC2Stack(app, "EC2Stack", env=env)

app.synth()

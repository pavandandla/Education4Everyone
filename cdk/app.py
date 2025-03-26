from aws_cdk import core
from lib.ec2_stack import EC2Stack  # Ensure this module exists and is accessible

app = core.App()
EC2Stack(app, "EC2Stack")  # Instantiate EC2Stack with app and ID
app.synth()  # Synthesize the CloudFormation templates

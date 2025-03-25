from aws_cdk import App
from lib.ec2_stack import EC2Stack 

app = App()
EC2Stack(app, "EC2Stack")
app.synth()
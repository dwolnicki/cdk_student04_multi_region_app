from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2
    # aws_sqs as sqs,
)
from constructs import Construct

class CdkStudent04MultiRegionAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, owner :str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        my_vpc = ec2.Vpc(self, owner+'-vpc',
            cidr='10.0.0.0/16',
            max_azs=1,
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(name=owner+'-priv-', subnet_type=ec2.SubnetType.PRIVATE_ISOLATED, cidr_mask=24)
            ]
        )


        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkStudent04MultiRegionAppQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_student04_multi_region_app.cdk_student04_multi_region_app_stack import CdkStudent04MultiRegionAppStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_student04_multi_region_app/cdk_student04_multi_region_app_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkStudent04MultiRegionAppStack(app, "cdk-student04-multi-region-app")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

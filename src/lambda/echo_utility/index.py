# lambda/echo_utility/index.py
from crhelper import CfnResource

cfn_helper = CfnResource(
    json_logging=True,
    log_level='DEBUG',
    boto_level='CRITICAL'
)


def handler(event: dict, context) -> dict:
    '''
    :param event: Cloudformation custom resource event. Example:
        {
            "RequestType": "Create",
            ...
            "ResourceProperties": {
                "ServiceToken": "arn:aws:lambda:eu-central-1:123456789012:function:echo-utility-prod",
                "variable1": "someValueX",
                "anotherVariable": "42"
            }
        }
    :type event: dict
    '''
    return cfn_helper(event, context)


@cfn_helper.create
def create(event, context):
    cfn_helper.Data.update({
        **event['ResourceProperties']
    })


@cfn_helper.update
def update(event, context):
    cfn_helper.Data.update({
        **event['ResourceProperties']
    })


@cfn_helper.delete
def delete(event, context):
    cfn_helper.Data.update({
        **event['ResourceProperties']
    })

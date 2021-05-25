from aws_cdk import core as cdk
from aws_cdk import aws_lambda as _lambda

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class OracleLayerCdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        cx_oracle_layer = _lambda.LayerVersion(self,
            "cxOracleLayer",
            code = _lambda.AssetCode('layers/cx_Oracle'),
            compatible_runtimes = [_lambda.Runtime.PYTHON_3_8]
        )

        client_oracle_layer = _lambda.LayerVersion(self,
            "oracleClientLayer",
            code = _lambda.AssetCode('layers/oracle_client'),
            compatible_runtimes = [_lambda.Runtime.PYTHON_3_8]
        )

        my_lambda = _lambda.Function(
            self, 'oracle-select',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.asset('functions'),
            handler='lambda_handler.handler',
            timeout=core.Duration.seconds(120),
            ## vpc=my_vpc,
            ## vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE),
            layers=[cx_oracle_layer, client_oracle_layer],
            environment={
                'ENDPOINT': 'desa.ceew8uinvwg5.us-east-1.rds.amazonaws.com',
                'PORT': '1521',
                'DBUSER': 'admin',
                'DBPASSWORD': 'cbYVh6uoGjaGtJrYAvRs',
                'DATABASE': 'devdb'
            }
        )



# CDK Python project to connect to an RDS Oracle Database from a Lambda Function

Creation of two Lambda Layers to import external libraries to the Lambda Fuction. The directory structure should be like this:

~~~
layers
| cx_Oracle
    | python
        | lib
            | python3.8
                | site-packages
                    | <external dependencies>
| oracle_client
    | lib
        | <external dependencies>
~~~

<br>

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

## Useful links
 
 * Creating a function with runtime dependencies: https://docs.aws.amazon.com/lambda/latest/dg/python-package-create.html#python-package-create-with-dependency
 * Using AWS Lambda environment variables: https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html
 * cx_Oracle 8 Installation: https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html
 * AWS Lambda Construct Library: https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_lambda/README.html
 * How to provision Lambda and Lambda Layer using CDK: https://dev.to/upupkenchoong/how-to-provision-lambda-and-lambda-layer-with-cdk-2ff4

Enjoy!

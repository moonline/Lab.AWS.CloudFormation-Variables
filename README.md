# Lab.AWS.CloudFormation-Variables

AWS Cloudformation variables using parameters, mappings, sub-stacks or Custom Resources.

* Parameters: [parameters.yml](./src/parameters.yml) 
* Mappings: [mappings.yml](./src/mappings.yml)
* Sub-stacks:
    * [sub-stacks-parent.yml](./src/sub-stacks-parent.yml)
    * [sub-stacks-child.yml](./src/sub-stacks-child.yml)
* Custom resources:

    ```mermaid
    ---
    title: Custom Resource Variables Helper
    ---
    %% Icons see https://fontawesome.com/search?m=free
    flowchart LR
        classDef stack stroke:black,fill:white;
        classDef lambda stroke:none,fill:#ED7100,color:white;
        classDef customResource stroke:none,fill:#E7157B,color:white;
        classDef policies stroke:#DD344C,stroke-width:3px,fill:white;


        subgraph customResourcesStack ["fa:fa-layer-group Custom Resources CF Stack"]
            direction TB
                echoUtilityFunction[λ\nEcho utility\nfunction]
                    echoUtilityFunction:::lambda

                customResourceHelperLayer[fa:fa-cubes\nCustom resource\nhelper layer]
                    customResourceHelperLayer:::lambda

                lambdaExecutionPolicy(fa:fa-list-check\nAWSLambdaExecute\npolicy)
                    lambdaExecutionPolicy:::policies

                echoUtilityFunction --- customResourceHelperLayer
                echoUtilityFunction --- lambdaExecutionPolicy
        end
            customResourcesStack:::stack
        

        subgraph mainStack ["fa:fa-layer-group Main CF Stack"]
            direction TB
            variablesResource["fa:fa-cube\nVariables\nresource"]
                variablesResource:::customResource

                variablesResource --- somethingHandlerFunction["fa:fa-cube\nSomething handler\nfunction"]
                    somethingHandlerFunction:::lambda
        end
            mainStack:::stack
            customResourcesStack -.- mainStack
    ```

    * [custom-resources.yml](./src/custom-resources.yml)
    * [custom-resource-variables.yml](./src/custom-resource-variables.yml)


## Deployment

```sh
cd src
sam build
sam deploy
```


## Cleanup

```sh
sam delete
```
pipeline {
    agent any

    parameters {
        string defaultValue: 'main', description: 'Name of chosen branch.', name: 'branch_name'
          text defaultValue: '''
tree(5)''', description: 'Adds value to tree.py file', name: 'value'
        
    }
    
    stages {

        stage('prin_parameters'){
            steps{
                echo "Branch name: ${params.branch_name} "
                echo "Value to add: ${params.value} "
            }
        }         


        // stage('tree') {
        //     steps {
        //         bat 'python tree.py'
        //     }
        //     }

        // stage('git') {
        //     steps {
        //         bat 'git branch'
        //     }
        //     }

    }
}

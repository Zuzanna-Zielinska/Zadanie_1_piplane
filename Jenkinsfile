pipeline {
    agent any

//     parameters {
//         string defaultValue: 'main', description: 'Name of chosen branch.', name: 'branch_name'
//           text defaultValue: '''
// tree(5)''', description: 'Adds value to tree.py file', name: 'value'
        
//     }
    
    stages {

        // stage('print_parameters'){
        //     steps{
        //         echo "Branch name: ${params.branch_name} "
        //         echo "Value to add: ${params.value} "
        //     }
        // }         

        stage('git') {
            steps {
                // def name = 3
                // var check_branch = 'aa'
                // checkout([$class: 'GitSCM', branches: [[name: '*/branch2]], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Zuzanna-Zielinska/Zadanie_1_piplane.git']]])
                // bat 'git checkout branch2'

                // exists = `git show-ref refs/main/branch-name`
                // if [ -n "$exists" ]; then
                //     echo 'branch exists!'
                // fi

                // withEnv(['exists=git --verify branch2']) {
                //     echo " $exists "
                //     if [ -n "$exists" ]; then
                //         echo 'branch exists!'
                //     fi
                // }

                // if git --quiet --verify branch2; then
                //     echo develop branch exists
                // fi

                // bat 'git --quiet --verify branch2'
                bat 'printenv'

                // bat 'git --verify branch2'
                bat 'git branch'
            }
            }

    }
}

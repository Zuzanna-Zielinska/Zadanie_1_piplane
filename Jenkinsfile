pipeline {
    agent any

    parameters {
        string defaultValue: 'main', description: 'Name of chosen branch.', name: 'branch_name'
          text defaultValue: '''
tree(5)''', description: 'Adds value to tree.py file', name: 'value'
        
    }
    
    stages {

        stage('clean_directory'){
            steps{
                bat 'RMDIR /S /q Zadanie_1_piplane'
            }
        }
        
        stage('git_log_in'){
            steps{
                bat 'git config --global user.name "Zuzanna-Zielinska"'
                bat 'git config --global user.email "zzielinska@student.agh.edu.pl"'
            }
        }

        stage('git_clone'){
            steps{
                bat 'git clone https://github.com/Zuzanna-Zielinska/Zadanie_1_piplane.git'

            }
        }
        
        stage('git_barnch'){
            
            steps{

                dir('Zadanie_1_piplane') {
                    bat "cd C:/Mine/Jenkins_workspace/workspace/Zadanie_1/Zadanie_1_piplane"
                    bat 'git checkout main'
                    bat 'git branch'
                    }

                
            }
        }

        stage('git_add_to_file'){
            steps{

                dir('Zadanie_1_piplane'){
                    bat 'echo "${params.value}" >> Newfile.txt'
                    bat 'git add Newfile.txt'
                    bat 'git commit -m "changing file"'                       
                }
             
            }
        }

        // stage('push_to_origin'){
        //     steps{
        //         dir('Zadanie_1_piplane'){
        //             // bat 'git push origin main' 
        //             bat "git push https://github.com/Zuzanna-Zielinska/Zadanie_1_piplane.git HEAD:main"
        //         }          
        //     }
        // }
        
        //---------------------------------------------------------------------------------
        // stage('git') {
        //     steps {
        //         // def name = 3
        //         // var check_branch = 'aa'
        //         // checkout([$class: 'GitSCM', branches: [[name: '*/branch2]], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Zuzanna-Zielinska/Zadanie_1_piplane.git']]])
        //         // bat 'git checkout branch2'

        //         // exists = `git show-ref refs/main/branch-name`
        //         // if [ -n "$exists" ]; then
        //         //     echo 'branch exists!'
        //         // fi

        //         // withEnv(['exists=git --verify branch2']) {
        //         //     echo " $exists "
        //         //     if [ -n "$exists" ]; then
        //         //         echo 'branch exists!'
        //         //     fi
        //         // }

        //         // if git --quiet --verify branch2; then
        //         //     echo develop branch exists
        //         // fi

        //         // bat 'git --quiet --verify branch2'
        //         // bat 'printenv'

        //         // bat 'git --verify branch2'
    
        //     }
        // }

    }
}

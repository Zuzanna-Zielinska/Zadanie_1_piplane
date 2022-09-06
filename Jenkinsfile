node{

    parameters {
        string defaultValue: 'main', description: 'Name of chosen branch.', name: 'branch_name'
          text defaultValue: '''
tree(5)''', description: 'Adds value to tree.py file', name: 'value'
        
    }

    // stage('clean_directory'){

    //     bat 'RMDIR /S /q Zadanie_1_piplane'

    // }

    stage('Example') {
        if (env.BRANCH_NAME == '${params.branch_name}') {
            echo 'I only execute on the master branch'
        } else {
            echo 'I execute elsewhere'
        }
    }

    stage('git_log_in'){

        bat 'git config --global user.name "Zuzanna-Zielinska"'
        bat 'git config --global user.email "zzielinska@student.agh.edu.pl"'

    }

    stage('git_clone'){

        bat 'git clone https://github.com/Zuzanna-Zielinska/Zadanie_1_piplane.git'

    }

    post{
        always{
            echo "Jej!"
        }
    }    

    stage('git_add_to_file'){

        dir('Zadanie_1_piplane'){
            bat 'echo "${params.value}" >> Newfile.txt'
            bat 'git add Newfile.txt'
            bat 'git commit -m "changing file"'                       
        }

    }

    stage('clean_directory'){

        bat 'RMDIR /S /q Zadanie_1_piplane'

    }

    // stage('push_to_origin'){

    //     dir('Zadanie_1_piplane'){
    //         // bat 'git push origin main' 
    //         bat "git push https://github.com/Zuzanna-Zielinska/Zadanie_1_piplane.git HEAD:main"
    //     }          
    // }-
}
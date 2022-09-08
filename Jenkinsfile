node{

    parameters {
        string defaultValue: 'main', description: 'Name of chosen branch.', name: 'branch_name'
          text defaultValue: '''
tree(5)''', description: 'Adds value to tree.py file', name: 'value'
        
    }

    stage('clean_directory'){

        // bat "echo 'garbage_text' >>Zadanie_1_piplane/garbage_file.txt"
        bat 'RMDIR /S /q Zadanie_1_piplane'

    }

    stage('Example') {
        if (env.BRANCH_NAME == '${params.branch_name}') {
            echo "This is ${params.branch_name}"
            
        } else {
            echo "This is NOT ${params.branch_name}!"
            bat "git checkout ${params.branch_name}"
        }
    }

    // stage('git_log_in'){

    //     bat 'git config --global user.name "Zuzanna-Zielinska"'
    //     bat 'git config --global user.email "zzielinska@student.agh.edu.pl"'

    // }

    stage('git_clone'){

        bat 'git clone https://github.com/Zuzanna-Zielinska/Zadanie_1_piplane.git'

    }

    // post{
    //     always{
    //         echo "Jej!"
    //     }
    // }    

    stage('git_add_to_file'){

        dir('Zadanie_1_piplane'){

            bat "git checkout master"

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

// node {
//     stage ("Hello"){
//        cleanWs()
//        echo "Hello World!"
//     }
//     stage ("git tests"){
//         // sh "rm -r workspace"
//         sh "git config --global user.name kowalskiPL"
//         sh "git config --global user.email patf117@gmail.com"
//         dir ('workspace'){
//             checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'patrykPass', url: 'git@github.com:kowalskiPL/jenkins_test.git']]])
//             dir ('jenkins_test'){
//                 sh "touch test-1.txt"
//                 echo "something > test-1.txt"
//                 sh "git checkout master"
//                 sh "git add ."
//                 sh "git commit -a -m 'some changes'"
//                 sh "git branch"
//                 sshagent(credentials: ['patrykPass']){
//                     sh "git push origin master"
//                 }
//             }
//         }
//     }
// }


}
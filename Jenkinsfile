node{

    parameters {
        string defaultValue: 'main', description: 'Name of chosen branch.', name: 'branch_name'
          text defaultValue: '''
tree(5)''', description: 'Adds value to tree.py file', name: 'value'
        
    }

    stage ("Hello"){
       cleanWs()
       echo "Hello World!"
    }

    // stage('clean_directory'){

    //     cleanWs()

    // }

    // stage('Example') {
    //     if (env.BRANCH_NAME == '${params.branch_name}') {
    //         echo "This is ${params.branch_name}"
            
    //     } else {
    //         echo "This is NOT ${params.branch_name}!"
    //         // bat "git checkout ${params.branch_name}"
    //     }
    // }

    stage('git_log_in'){

        bat 'git config --global user.name "Zuzanna-Zielinska"'
        bat 'git config --global user.email "zzielinska@student.agh.edu.pl"'

    }

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

            // bat "git checkout main"
            checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: []])

            bat 'echo "${params.value}" >> Newfile.txt'
            bat 'git add Newfile.txt'
            bat 'git commit -m "changing file"'                       
        }

    }

    stage('push_to_origin'){

        // dir('Zadanie_1_piplane'){
        //         sshUserPrivateKey(credentials: [private_key]){

        //             // bat "git push origin main"
        //             echo "aaa"
        //         }
        //     // bat 'git push origin main' 
        //     // checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [url: git@github.com:Zuzanna-Zielinska/Zadanie_1_piplane.git]])
        //     // bat "git push https://github.com/Zuzanna-Zielinska/Zadanie_1_piplane.git HEAD:main"
        // }          
    }

//b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
// QyNTUxOQAAACCH6D4GzCtGrL/nyTVLOjBbq+P3xxhuJTHbs1831eQeHwAAAKAk+8HIJPvB
// yAAAAAtzc2gtZWQyNTUxOQAAACCH6D4GzCtGrL/nyTVLOjBbq+P3xxhuJTHbs1831eQeHw
// AAAEDePiscY9TisyThik54RZOsbVn/XUCFcmsjYA5Wbymu14foPgbMK0asv+fJNUs6MFur
// 4/fHGG4lMduzXzfV5B4fAAAAHXp6aWVsaW5za2FAc3R1ZGVudC5hZ2guZWR1LnBs
//private_key


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
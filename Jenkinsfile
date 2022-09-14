node{

    parameters {
        string defaultValue: 'main', description: 'Name of chosen branch.', name: 'branch_name'
          text defaultValue: '''
tree(5)''', description: 'Adds value to tree.py file', name: 'value'
        
    }

    stage ("Hello"){
       echo "Hello World!"
    }

    stage("git"){
        // checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [[$class: 'CleanBeforeCheckout']], userRemoteConfigs: [[url: 'https://github.com/Zuzanna-Zielinska/Zadanie_1_piplane.git']]])
        checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Zuzia_git2', url: 'git@github.com:Zuzanna-Zielinska/Zadanie_1_piplane.git']]])

        sh 'git config --global user.name "Zuzanna-Zielinska"'
        sh 'git config --global user.email "zzielinska@student.agh.edu.pl"'
        sh "git checkout main" 
        
        sh "git reset --hard origin/main"

        sh "echo 'Tekst ' >> Newfile.txt"
        sh "ls"
        sh "git add Newfile.txt"
        sh "git commit -m 'changing file'"  
    }

    stage("push"){
        // withCredentials([sshUserPrivateKey(credentialsId: 'Zuzia_git', keyFileVariable: '')]) {
        //     echo "Is working?"
        //     sh "git push"
        //     // sh "git push"
        //     sh "ls"            

        // }

        sshagent(['Zuzia_git_ssh']) {
            echo "Is working?"
            sh "git status"
            sh "git remote show origin"
            sh "git pull"
            sh "git push"
            // sh "git push"
            sh "ls"   
        }
        // withCredentials([gitUsernamePassword(credentialsId: 'adaff42c-0a52-4ab3-84bc-6c4522150435')]) {
        //     sh "git push"
        //     sh "ls" 
        // }
        // sshagent(credentials: ['Zuzia_git_ssh']){
        //     echo "Is working?"
        //     sh "git push origin main"
        // }
    }

     
}

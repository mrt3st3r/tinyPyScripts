cat /var/lib/jenkins/config.xml | grep version
sudo service jenkins stop
cd /usr/share/jenkins
sudo rm jenkins.war.old
sudo mv jenkins.war jenkins.war.old
sudo wget https://updates.jenkins-ci.org/latest/jenkins.war
sudo service jenkins star
cat /var/lib/jenkins/config.xml | grep version

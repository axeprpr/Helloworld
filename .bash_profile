#add this into ~/.bash_profile
#sudo su - ??
echo "****************************************"
echo "1-->A"
echo "2-->B"
echo "3-->C"
read -p "Please select an user to login:" user
case $user in
  1)sudo su - A;;
  2)sudo su - B;;
  3)sudo su - C;;
  *)return;;
esac

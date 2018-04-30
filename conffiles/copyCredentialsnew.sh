#!/bin/bash
#loads the content from the input file
source $1
#the values are replaced with other name for our confert
baseUsername=$Mysql_username
basePassword=$Mysql_password
baseAccesskey=$aws_key
baseSecretkey=$aws_secret
echo $baseUsername
echo $basePassword
#takes all the files that has the extension as .conf in the given directory
files=$(find conffiles -type f -name "*.conf") 
#for loop takes the file one by one  and checks for the word given and replace it with new value from $1(input file)
for file in $files 
do
  sed -i  's#dbuser#'$baseUsername'#g; s#dbPass#'$basePassword'#g; s#awskey#'$baseAccesskey'#g; s#awssecret#'$baseSecretkey'#g' $file 
done




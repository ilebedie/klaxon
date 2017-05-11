# klaxon

   ******   **                                    
  **////** /**                                    
 **    //  /**  ******   **   **  ******  ******* 
/**        /** //////** //** **  **////**//**///**
/**        /**  *******  //***  /**   /** /**  /**
//**    ** /** **////**   **/** /**   /** /**  /**
 //******  ***//******** ** //**//******  ***  /**
  //////  ///  //////// //   //  //////  ///   // 

Take me to the flow

Todo:
- Learn how to enter and leave container properly(clarify, automate)
- Setup mysql container
- Setup apache webserver
- Allow access to site for everyone


How to enter machine:
`ssh -i "ivan-lab-ami.pem" ec2-user@ec2-52-59-214-5.eu-central-1.compute.amazonaws.com`

How to run webserver container:
`cd ~/git/klaxon
docker run -p 8080:8080  -v "$PWD":/root/klaxon -it ilebedie/ubuntu_klax bash`

How to run webserver:
`python manage.py 0:8080`

Check site: type in browser
`ec2-user@ec2-52-59-214-5.eu-central-1.compute.amazonaws.com:8080`


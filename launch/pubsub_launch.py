
from launch import LaunchDescription 
from launch_ros.actions import Node 


def generate_launch_description(): 
     
       
	node1 = Node( 
    	package="simple_pub_sub", 
    	executable="pub", 
    	name="number_publisher" 
  	) 
     
	node2 = Node( 
    	package="simple_pub_sub", 
    	executable="sub", 
    	name="number_counter" 
  	)
  
	nodes = [ 
			node1, 
        	node2
	] 
  
	return LaunchDescription(nodes) 
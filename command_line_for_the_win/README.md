Command line for the win

This project's screenshots were uploaded to the sandbox environment using the SFTP (Secure File Transfer Protocol) command-line tool. I followed these steps to upload them :-
	1 - I connected to the sandbox from my local machine using this command:
		sftp user@server_ipaddress
	2 - After that I entered the password which was provided by the sandboxes interface.
	3 - After I connected to the sandbox using though my local machine, I used this command to navigate to the project directory:
		cd alx-system_engineering-devops/command_line_for_the_win/
	4 - After that I uploaded the images using the command put like:
		put image
	5 - I disconnected from the sandbox using this command:
		exit

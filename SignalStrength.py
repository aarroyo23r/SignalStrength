#Dependencias

#Pip
#sudo apt-get install python-pip python-dev build-essential 
#sudo pip install --upgrade pip 


#Wireless
#sudo pip install wireless
#Si el comando anterior da problemas de instalacion ejecutar antes los 2 siguientes
#sudo pip install --upgrade setuptools
#sudo pip install ez_setup
#---------------------------------------------------------------

import subprocess 
import time 


rate=0.2 #Tasa de muestreo
wirelessDevice= " wlp2s0 " #Cambiar por su dispositivo wireless (ver con ifconfig)


def RateConfig(): #Configuracion de la tasa de muestreo de potencia
	
 	rate=input("Ingrese la nueva tasa de muestreo")
	
	

def Connect(): #Conectar a una red

	
 	option=raw_input("\n Desea Conectarse a alguna red? \n s=Si    n=No \n" )

	yes= "s" or "S"
	no= "n" or "N"

	if option == yes:	

		ssid=raw_input("\n Ingrese el SSID de la red\n")
		password=raw_input("\n Contrasenna\n")

		from wireless import Wireless
		wireless = Wireless()
		wireless.connect(ssid=ssid, password=password)
		
		
		
		if wireless :
			print "\n Conexion establecida"
		else:
			print "\n No se pudo conectar a la red, verifique el SSID y la  contrasena ingresada"


	elif option==no:
		pass
	else: 
		
		print "\n Ingrese una opcion correcta"
		Connect()



def Scan(): # Escanear redes disponibles

  		cmd = subprocess.Popen( "sudo iw dev " + wirelessDevice +		   " scan",shell=True,stdout=subprocess.PIPE)
		print "Redes detectadas"
    		for line in cmd.stdout:
     			 if 'SSID:' in line:
		 		 print line.lstrip(' '), 
     		 	 elif 'Not-Associated' in line:
				 print 'No se detectaron redes' 
		Connect()
    	
		 
def Power(): #Medir potencia de la red a la que se esta conectado
	cont=0
	f = open ('Data.txt','w')
	try:
	    while True:
	    
  		cmd = subprocess.Popen( "iwconfig "+ wirelessDevice,shell=True,stdout=subprocess.PIPE)
    		for line in cmd.stdout:
     			 if 'Link Quality' in line:

				 cont=cont + 1
                                 print "Medicion", cont, line.lstrip(' ')
				
                                 f.write(" Medicion ") #Escritura en archivo .txt
			         f.write(line.lstrip(' '))
				 
     		 	 elif 'Not-Associated' in line:
				 print 'Sin senal' 
    			 time.sleep(rate)
	except (KeyboardInterrupt, SystemExit): #Exit with ctrl+C
	    pass
 

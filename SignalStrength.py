import subprocess 
import time 


rate=0.2


def RateConfig():
	print "Ingrese la nueva tasa de muestreo"
 	rate=input()


def Scan():

  		cmd = subprocess.Popen( "sudo iw dev wlp2s0 		   scan",shell=True,stdout=subprocess.PIPE)
		print "Redes detectadas"
    		for line in cmd.stdout:
     			 if 'SSID:' in line:
		 		 print line.lstrip(' '), 
     		 	 elif 'Not-Associated' in line:
				 print 'No se detectaron redes' 
    			 
def Power():
	cont=0
	f = open ('Data.txt','w')
	try:
	    while True:
	    
  		cmd = subprocess.Popen( "iwconfig wlp2s0 ",shell=True,stdout=subprocess.PIPE)
    		for line in cmd.stdout:
     			 if 'Link Quality' in line:

				 cont=cont + 1
                                 print "Medicion", cont, line.lstrip(' ')
				
                                 f.write(" Medicion ")
			         f.write(line.lstrip(' '))
				 
     		 	 elif 'Not-Associated' in line:
				 print 'Sin senal' 
    			 time.sleep(rate)
	except (KeyboardInterrupt, SystemExit):
	    pass
			 


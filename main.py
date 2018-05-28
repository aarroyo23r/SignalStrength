import SignalStrength


menuStrings=["________________________________ \n","Seleccione una opcion: \n","1-Buscar Redes","2-Medir Potencia", "3-Configuracion","4-Salir"]


while True:

#Menu Principal

	from wireless import Wireless
	wireless = Wireless()
	currentConection=wireless.current()

	
	print  menuStrings[0], "Conectado a la red ", currentConection,"\n", menuStrings[0]
	for i in range (1,len(menuStrings)):
		print menuStrings[i]
	print  menuStrings[0]

	  
      
	option=input()


	options = {1 : SignalStrength.Scan,
           	   2 : SignalStrength.Power,
	   	   3 : SignalStrength.RateConfig,
		   4 : exit, 
	  	  

	}

	options[option]()

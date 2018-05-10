import SignalStrength




while True:

#Menu Principal
	print  "________________________________ \n", "Seleccione una opcion: \n \n","1-Buscar Redes \n","2-Medir Potencia \n", "3-Configuracion \n","4-Salir \n","________________________________"




	option=input()


	options = {1 : SignalStrength.Scan,
           	   2 : SignalStrength.Power,
	   	   3 : SignalStrength.RateConfig,
		   4 : exit, 
	  	  

	}

	options[option]()

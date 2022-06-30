package chamorro.edisson.reto2;

public class Peaje {
	// EN ESTE ESPACIO SE ESCRIBEN LOS ATRIBUTOS DE LA CLASE Peaje
	private String[] filaCoches;
	private String[] cochesFlyPass;
	private boolean estadoPeaje = true;
	private int cantidadCochesAtendidos = 1, cocheEnAtencion = 0;
	// A CONTINUACI�N, BAJO LOS ATRIBUTOS, SE ESCRIBEN LOS M�TODOS DEFINIDOS
	// EN EL ENUNCIADO DEL PROBLEMA:

	public Peaje(String[] filaCoches) {
		// COMPLETE AQU� LA L�GICA DEL CONSTRUCTOR SEG�N EL ENUNCIADO DEL PROBLEMA
		this.filaCoches = filaCoches;
		cochesFlyPass= new String[filaCoches.length];
		for(int i=0;i<filaCoches.length;i++) {
			cochesFlyPass[i]=" ";
		}
	}

	public void proximoCoche() {
		// COMPLETE AQU� LA L�GICA DE ESTE M�TODO SEG�N EL ENUNCIADO DEL PROBLEMA
		if (estadoPeaje) {
			cocheEnAtencion++;
			cantidadCochesAtendidos++;
		}
	}

	// NO SE DEBE PREOCUPAR POR DESARROLLAR ESTE M�TODO. �NO ELIMINARLO NI
	// MODIFICARLO!
	public void agregarCocheFlyPass() {
		String cocheABuscar = filaCoches[cocheEnAtencion];
		for (String coche : cochesFlyPass) {
			if (coche.equals(cocheABuscar)) {
				break;
			}
			if (" ".equals(coche)) {
				coche = cocheABuscar;
			}
		}
	}

	public void cambiarEstadoPeaje() {
		// COMPLETE AQU� LA L�GICA DE ESTE M�TODO SEG�N EL ENUNCIADO DEL PROBLEMA
		estadoPeaje = (estadoPeaje) ? false : true;
	}

	// INSERTE LOS GETTERS Y SETTERS A PARTIR DE AC�:
	public String[] getFilaCoches() {
		return filaCoches;
	}

	public void setFilaCoches(String[] filaCoches) {
		this.filaCoches = filaCoches;
	}

	public String[] getCochesFlyPass() {
		return cochesFlyPass;
	}

	public void setCochesFlyPass(String[] cochesFlyPass) {
		this.cochesFlyPass = cochesFlyPass;
	}

	public boolean isEstadoPeaje() {
		return estadoPeaje;
	}

	public void setEstadoPeaje(boolean estadoPeaje) {
		this.estadoPeaje = estadoPeaje;
	}

	public int getCantidadCochesAtendidos() {
		return cantidadCochesAtendidos;
	}

	public void setCantidadCochesAtendidos(int cantidadCochesAtendidos) {
		this.cantidadCochesAtendidos = cantidadCochesAtendidos;
	}

	public int getCocheEnAtencion() {
		return cocheEnAtencion;
	}

	public void setCocheEnAtencion(int cocheEnAtencion) {
		this.cocheEnAtencion = cocheEnAtencion;
	}

}

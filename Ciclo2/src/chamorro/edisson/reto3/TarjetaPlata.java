package chamorro.edisson.reto3;

public class TarjetaPlata extends TarjetaCine{
//Atributos
    
	private int cantidadVisitas=0;
	private boolean elegibleOro=false;
    //Constructor
    public TarjetaPlata(String idTarjeta, String nombreCompleto, String email, String telefono, int edad) {
      super(idTarjeta, nombreCompleto, email, telefono, edad, 10);
    }

    //Método
    @Override
    public double pagar(String[] cuenta){
		cantidadVisitas++;
		elegibleOro=(cantidadVisitas>=5)?true:false;
		double totalCompra=0.0; 
		for(String item:cuenta) {
			if (item.equals("Boleta")) totalCompra+=6000;
			if (item.equals("Combo 1 - Crispetas + Gaseosa")) totalCompra+=8000;
			if (item.equals("Combo 2 - Perro + Gaseosa")) totalCompra+=12000;
		}
    	return totalCompra*(1-(this.getPorcentajeDescuento()/100));
    }

    //Getters y Setters
    public int getCantidadVisitas() {
		return cantidadVisitas;
        
    }

    public void setCantidadVisitas(int cantidadVisitas) {
        this.cantidadVisitas=cantidadVisitas;
    }

    public boolean isElegibleOro() {
		return elegibleOro;
        
    }

    public void setElegibleOro(boolean elegibleOro) {
        this.elegibleOro=elegibleOro;
    }
}

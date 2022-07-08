package chamorro.edisson.reto3;

public class cine {

	public static void main(String[] args) {
		// TODO Auto-generated method stub[]   []
		String [] cuenta1= {"Boleta", "Combo 1 - Crispetas + Gaseosa"};
		String [] cuenta2= {"Boleta", "Boleta", "Combo 1 - Crispetas + Gaseosa", "Combo 2 - Perro + Gaseosa"};
		String []compra = {"Boleto","Boleto","Boleto","Combo 1","Combo 2"};
		TarjetaCine tarjetaNormal = new TarjetaCine("1234", "Edisson Chamorro", "edison.chamorro@correo.com", "30087632", 28, 0);
		TarjetaOro tarjetaOro = new TarjetaOro("1234", "Edisson Chamorro", "edison.chamorro@correo.com", "30087632", 28);
		TarjetaPlata tarjetaPlata = new TarjetaPlata("1234", "Edisson Chamorro", "edison.chamorro@correo.com", "30087632", 28);
		
		System.out.println("porcentaje descuento normal "+tarjetaNormal.getPorcentajeDescuento());
		System.out.println("porcentaje descuento plata "+tarjetaPlata.getPorcentajeDescuento());
		System.out.println("porcentaje descuento oro "+tarjetaOro.getPorcentajeDescuento());
		
		System.out.println("Compra con tarjeta oro "+tarjetaOro.pagar(cuenta1));
		System.out.println("Compra con tarjeta plata "+tarjetaPlata.pagar(cuenta2));
		System.out.println("Compra con tarjeta normal "+tarjetaNormal.pagar(compra));
		
		System.out.println("Cantidad Visitas "+tarjetaPlata.getCantidadVisitas());
		System.out.println("Elegible oro? "+tarjetaPlata.isElegibleOro());
		
		System.out.println("Redimir beneficio "+tarjetaOro.redimirBeneficio(2));
		
	}

}

package chamorro.edisson.reto1;

import java.util.Arrays;

public class EstadisticasTienda {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int [] ventas = {2700,9500,300,15000,1800,10000,400,3000,400};
		int [] respuesta= Solution.reporte(ventas);
		for (int i=0; i< respuesta.length;i++) {
			System.out.print(respuesta[i]+"\n");
		}
	}

}

class Solution{
    //ESTA CLASE NO TIENE MAIN
    
    
    public static int [] reporte(int [] compra){
        //EN ESTE ESPACIO PONER SU LÓGICA
        
       int []estadistica=new int[3];
       
       java.util.Arrays.sort(compra);
       estadistica[0]=java.util.Arrays.stream(compra).sum();
       estadistica[1]=compra[0];
       estadistica[2]=compra[compra.length -1];
       return estadistica;
       
        
    }
}
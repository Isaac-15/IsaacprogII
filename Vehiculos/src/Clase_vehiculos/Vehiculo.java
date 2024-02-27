package Clase_vehiculos;

public class Vehiculo {

    public static void main(String[] args) {
        

        Vehiculos v = new Vehiculos();

        v.setMarca("toyota");
        v.setModelo("pollito");
        v.setCaballosDeFuerza(730);
        v.setTraccion("6 ruedas");
        v.setVelocidad_maxima("730 Kmh");

        System.out.println(" la marca del auto es: " + v.getMarca()+ "\n el modelo del auto es el: "+v.getModelo()+ "\n los caballos de fuerza son: "+v.getCaballosDeFuerza()+"\n la velocidad maxima es: "+ v.getVelocidad_maxima()+ "\n la traccion del auto es de: " +v.getTraccion());
        

    }

    
    
}

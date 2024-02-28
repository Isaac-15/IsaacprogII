package Clase_vehiculos;

public class Vehiculo {

    public static void main(String[] args) {
        

        Vehiculos v = new Vehiculos();

        v.setMarca("Bugatti");
        v.setModelo("Chiron super sport");
        v.setCaballosDeFuerza(1577);
        v.setTraccion("traccion integral");
        v.setVelocidad_maxima("490 Kmh");

        System.out.println(" la marca del auto es: " + v.getMarca()+ "\n el modelo del auto es el: "+v.getModelo()+ "\n los caballos de fuerza son: "+v.getCaballosDeFuerza()+"\n la velocidad maxima es: "+ v.getVelocidad_maxima()+ "\n la traccion del auto es: " +v.getTraccion());
        

    }

    
    
}

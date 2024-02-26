
package persona;


public class Persona {

  
    public static void main(String[] args) {
        
        Personas P = new Personas();
        
        P.setNombre("isaac");
        P.setCedula(1043967918);
        P.setTelefono("3016191461");
        P.setCorreo("isaaccarmona281@gmail.com");
        
        
        System.out.println("mi nombre es "+ P.nombre); System.out.println("mi cedula "+ P.cedula); System.out.println("por si me quieres llamar "+ P.telefono); System.out.println("mi correo "+ P.correo);
        
    }
    
   
    
}

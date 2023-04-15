public class Effect
{
    private string element;

    public Effect(string element)
    {
        this.element = element;
    }

    public (string, bool, int, int) ElementalEffect(string name, int shifts, int damage, int missProb, bool freeze)
    {
        if (this.element == "FIRE")
        {
            /*
             *  Aplica QUEMADURA (versión en Inglés está por revisar):
             *  Quita 20HP (aún está por revisar) cantidad de vida durante 3 turnos.
             */

            if (shifts > 0)
            {
                shifts = shifts - 1;
                damage = 20;
                Console.WriteLine(" ");
                Console.WriteLine("¡", name, " está bajo efecto de QUEMADURA!");
                Console.WriteLine("¡La QUEMADURA ha aplicado ", damage, " Puntos de daño a ", name, "!");
                Console.WriteLine("¡", shifts, " turnos de QUEMADURA restantes!");
                Console.WriteLine(" ");
                return (this.element, true, damage, shifts);
            }

            else
            {
                Console.WriteLine(" ");
                Console.WriteLine("¡", name, " ya no está bajo efecto de QUEMADURA!");
                Console.WriteLine(" ");
                return (this.element, false, 0, 0);
            }
        }

        else if (this.element == "WATER")
        {
            /*
             * Aplica TSUNAMI (versión en Inglés está por revisar):
             * "Arrastra" al enemigo a una gran distancia, reduciendo su precisión,
             * aumentando su probabilidad de fallar en 60 Puntos (aún está por revisar).
             */

            if (shifts > 0)
            {
                if (shifts == 3)
                {
                    missProb = missProb + 60;
                }

                shifts = shifts - 1;
                Console.WriteLine(" ");
                Console.WriteLine("¡", name, " fue arrojado por TSUNAMI!");
                Console.WriteLine("¡La probabilidad de fallar de ", name, " pasa a ", missProb, " Puntos!");
                Console.WriteLine("¡", shifts, " turnos de TSUNAMI restantes!");
                Console.WriteLine(" ");
                return (this.element, true, missProb, shifts);
            }

            else
            {
                Console.WriteLine(" ");
                Console.WriteLine("¡", name, " ya no está bajo efecto de TSUNAMI!");
                Console.WriteLine("¡La probabilidad de fallar de ", name, " vuelve a la normalidad!");
                Console.WriteLine(" ");
                return (this.element, false, 0, 0);
            }
        }

        if (this.element == "ICE")
        {
            /*
             * Aplica CONGELAMIENTO (versión en Inglés está por revisar):
             * "Congela" al rival, lo que le impide hacer algo durante el
             * siguiente turno.
             */

            if (freeze == false)
            {
                Console.WriteLine(" ");
                Console.WriteLine("¡", name, " está bajo efecto de CONGELAMIENTO!");
                Console.WriteLine("¡", name, " no puede hacer nada durante este turno!");
                Console.WriteLine(" ");
                freeze = true;
            }

            else
            {
                Console.WriteLine(" ");
                Console.WriteLine("¡", name, " ya no está bajo efecto de CONGELAMIENTO!");
                Console.WriteLine(" ");
                freeze = false;
            }

            return (this.element, freeze, 0, 0);
        }

        else
        {
            return ("NORMAL", false, 0, 0);
        }
    }
}

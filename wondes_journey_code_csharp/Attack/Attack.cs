public class Attack
{
    private int element;
    public int damage;
    private string elementName;
    private int baseDamage;
    private int elementDamage;
    private int criticDamage;
    private int criticProb;
    private int missProb;
    private bool criticAttack;
    private bool elementalAttack;

    public Attack(
        int element,
        int baseDamage,
        int elementDamage,
        int cricticDamage,
        int criticProb,
        int missProb)
    {
        this.element = element;
        this.baseDamage = baseDamage;
        this.elementDamage = elementDamage;
        this.criticDamage = cricticDamage;
        this.criticProb = criticProb;
        this.missProb = missProb;
        this.criticAttack = false;
        this.elementalAttack = false;
    }

    public void SetElementName()
    {
        if (this.element == 1)
        {
            this.elementName = "FIRE";
            this.elementalAttack = true;
        }

        else if (this.element == 2)
        {
            this.elementName = "WATER";
            this.elementalAttack = true;
        }

        else if (this.element == 3)
        {
            this.elementName = "ICE";
            this.elementalAttack = true;
        }

        else
        {
            this.elementName = "NORMAL";
            this.elementalAttack = false;
        }
    }

    public bool ItsCritic(int numberForProbs)
    {
        if (numberForProbs <= this.criticProb)
        {
            this.criticAttack = true;
        }

        else
        {
            this.criticAttack = false;
        }

        return this.criticAttack;
    }

    public bool AttackMissed(int numberForProbs)
    {
        if (numberForProbs <= this.missProb)
        {
            return true;
        }

        else
        {
            return false;
        }
    }

    public void CalcAttackDamage()
    {
        Random rand = new Random();
        if (this.AttackMissed(rand.Next(0, 100)) == false)
        {
            this.damage = this.baseDamage;

            if (this.element == 1 || this.element == 2 || this.element == 3)
            {
                this.damage += this.elementDamage;
            }

            if (this.ItsCritic(rand.Next(0, 100)) == true)
            {
                this.damage += this.criticDamage;
                Console.WriteLine(" ");
                Console.WriteLine("¡EL ATAQUE HA SIDO CRÍTICO!");
                Console.WriteLine(" ");
            }
        }

        else
        {
            this.damage = 0;
            Console.WriteLine(" ");
            Console.WriteLine("¡EL ATAQUE HA FALLADO!");
            Console.WriteLine(" ");
        }

        Console.WriteLine("¡EL ATAQUE INFLIGIDO ", this.damage, " DE DAÑO!");
        Console.WriteLine(" ");
    }
}
public class Character
{
    private string name;
    private int life;
    private int damage;
    private bool hasAnEffect;
    private int Attack;

    public Character(string name, int life, int damage)
    {
        this.name = name;
        this.life = life;
        this.damage = damage;
        this.hasAnEffect = false;
    }

    public void PrintStats()
    {
        Console.WriteLine("Nombre: ", this.name);
        Console.WriteLine("PS: ", this.life);
        Console.WriteLine(" ");
    }

    public void SetAttack(int attack)
    {
        this.Attack = attack;
    }

    public void SetDamage(int attack)
    {
        this.life = this.life - attack;

        if (this.life < 0)
        {
            this.life = 0;
        }
    }
}
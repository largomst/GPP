
class Breed
{
private:
    int health_;
    const char *attack_;

public:
    Breed(int health, const char *attack) : health_(health), attack_(attack) {}
    int getHealth() { return health_; }
    const char *getAttack() { return attack_; }
    Monster *newMonster()
    {
        return new Monster(*this);
    }
};

class Monster
{
    friend class Breed; // Breed 成为 Monster 的友元从而能够访问 Monster 的构造方法。

private:
    int health_;
    Breed &breed_;

private:
    Monster(Breed &breed) : health_(breed.getHealth()), breed_(breed) {}
};

// 修改前的创建怪物方法
// Monster *monster = new Monster(someBreed);

// 修改后的代码：
// Monster *monster = someBreed.newMonster()；

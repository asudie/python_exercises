import random

def turrets_generator():
    cut_points = sorted(random.sample(range(101), 4))

    trait_values = [cut_points[0]] + \
                   [cut_points[i] - cut_points[i-1] for i in range(1, len(cut_points))] + \
                   [100 - cut_points[-1]]

    traits = ['neuroticism', 'openness', 'conscientiousness', 'extraversion', 'agreeableness']

    TurretClass = type('Turret', (), {
        'personality': dict(zip(traits, trait_values)),
        'shoot': lambda self: print("Shooting"),
        'search': lambda self: print("Searching"),
        'talk': lambda self: print("Talking")
    })

    return TurretClass()

def main():
    turret = turrets_generator()
    print("Personality:", turret.personality)
    turret.shoot()
    turret.search()
    turret.talk()

if __name__ == "__main__":
    main()

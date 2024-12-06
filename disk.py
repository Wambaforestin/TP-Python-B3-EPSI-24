# Modélisation
# Vous travaillez sur un outil de supervision. Vous devez faciliter le
# travail de collecte et de stockage des informations relatives à votre
# environnement supervisé.
# Nous nous occupons ici de l’espace stockage et plus particulièrement
# des disques.
# Créer une classe Disk qui représente un disque de stockage et qui a
# les propriétés suivantes lors de sa création :
# •espace total : total
# •espace occupé : used
# Des nouveaux accesseurs
# Créer un accesseur pour obtenir l’espace libre (free). Attention, cette
# valeur ne doit jamais être stockée.
# Affichage
# Modifier la classe Disk pour permettre l’affichage d’une instance qui
# renseigne les informations suivantes du disque
# disk = Disk(10, 2)
# print(disk) # Disk[total: 10 Gb, used: 2 Gb]
# Tri personnalisé
# Pour terminer, nous souhaitons trier une liste de disques en fonction
# de l’espace disque utilisé. A partir d’une liste a priori non trié, nous
# voulons obtenir une liste de disques rangée par ordre croissant de
# ratio d’espace disque utilisé.
# Pour réaliser ce tri, nous utiliserons la fonction sorted. Il faut donc
# modifier la classe Disk pour permettre ce tri.
# Regardez du côté de la documentation technique de datamodele

# SUPERVISION (5 POINTS)
# Exemple d’utilisation
# Exemple de code opérationnel avec la classe à créer
# disk1 = Disk(total = 10, used = 2)
# disk2 = Disk(total = 20, used = 5)
# print(disk1.free) # 8
# print(disk2.free) # 15
# print(disk1.used_perc) # 0.2
# print(disk2.used_perc) # 0.25
# disks = [disk1, disk2]
# disks_sorted = sorted(disks) # trié selon le pourcentage

class Disk:
    def __init__(self, total, used):
        self.__total = total
        self.__used = used

    @property
    def free(self):
        return self.__total - self.__used

    @property
    def used_perc(self):
        return self.__used / self.__total

    def __str__(self):
        return f"Disk[total: {self.__total} Gb, used: {self.__used} Gb]"

    def __lt__(self, other):
        return self.used_perc < other.used_perc

    def __eq__(self, other):
        return self.used_perc == other.used_perc

    def __gt__(self, other):
        return self.used_perc > other.used_perc

    def __le__(self, other):
        return self.used_perc <= other.used_perc

    def __ge__(self, other):
        return self.used_perc >= other.used_perc

    def __ne__(self, other):
        return self.used_perc != other.used_perc
    
if __name__ == '__main__':
    disk1 = Disk(total = 10, used = 2)
    disk2 = Disk(total = 20, used = 5)
    print(disk1.free) # 8
    print(disk2.free) # 15
    print(disk1.used_perc) # 0.2
    print(disk2.used_perc) # 0.25
    disks = [disk1, disk2]
    disks_sorted = sorted(disks) # trié selon le pourcentage
    print(disks_sorted) # [Disk[total: 10 Gb, used: 2 Gb], Disk[total: 20 Gb, used: 5 Gb]]
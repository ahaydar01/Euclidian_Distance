import itertools
import math

# 1. Noktaların Tanımlanması
points = [(1, 2), (4, 6), (7, 8), (2, 3), (9, 10)]

# 2. Öklid Mesafesi İçin Fonksiyon Yazma
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# 3. Mesafelerin Hesaplanması
distances = []
point_pairs = list(itertools.combinations(points, 2))  # Tüm nokta çiftlerini oluştur

for p1, p2 in point_pairs:
    distance = euclideanDistance(p1, p2)
    distances.append(distance)

# 4. Minimum Mesafenin Bulunması (Boş liste kontrolü)
if distances:
    min_distance = min(distances)
    print(f"Tüm noktalar arasındaki minimum Öklid mesafesi: {min_distance:.2f}")
else:
    print("Mesafe hesaplanacak yeterli nokta yok!")

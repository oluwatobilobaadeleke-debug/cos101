print("PHYSICS FORMULAS")
print("1. Force")
print("2. Speed")
print("3. Acceleration")
print("4. Density")
print("5. Pressure")

choice = input("Enter your choice (1-5): ")

if choice == "1":
    mass = float(input("Enter mass: "))
    acc = float(input("Enter acceleration: "))
    result = mass * acc
    print("Force =", result)

elif choice == "2":
    distance = float(input("Enter distance: "))
    time = float(input("Enter time: "))
    result = distance / time
    print("Speed =", result)

elif choice == "3":
    vf = float(input("Enter final velocity: "))
    vi = float(input("Enter initial velocity: "))
    time = float(input("Enter time: "))
    result = (vf - vi) / time
    print("Acceleration =", result)

elif choice == "4":
    mass = float(input("Enter mass: "))
    volume = float(input("Enter volume: "))
    result = mass / volume
    print("Density =", result)

elif choice == "5":
    force = float(input("Enter force: "))
    area = float(input("Enter area: "))
    result = force / area
    print("Pressure =", result)

else:
    print("Invalid choice")

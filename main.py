# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet (name, greeting='Hello, <name>!'):
    hoi = greeting.replace("<name>", name)
    return hoi

print (greet("Landlubber", "Ahoy, <name>!"))

bodies = {
        "sun" : 274,
        "jupiter" : 24.92, 
        "neptune" : 11.15,
        "saturn" : 10.44,
        "earth" : 9.8,
        "uranus" : 8.87,
        "venus" : 8.87,
        "mars" : 3.71,
        "mercury" : 3.7,
        "moon" : 1.62,
        "pluto" : 0.58
    }

def force(mass, body="earth"):
    force = mass * round(bodies[body], 1)
    return force

G = 6.674 * (10 ** -11)

def pull(m1, m2, d):
    pull = G * ((m1 * m2) / (d*d))
    return pull


print (bodies["pluto"])
print (G)
print (pull(0.1, 5.972*(10 ** 24), (6.371 * (10 ** 6))))
print(force(4, "pluto"))


from random import randint


def generate_random_ip():
    return '.'.join(
        str(randint(0, 255)) for _ in range(4)
    )


random_ip = generate_random_ip()
print(random_ip) 
